provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-beazley-reni"
  location = var.location
}

resource "azurerm_virtual_network" "vnet" {
  name                = "beazley-reni-vnet"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
  address_space       = ["10.0.0.0/16"]
}

resource "azurerm_subnet" "subnets" {
  count               = length(var.tiers)
  name                = "subnet-${count.index + 1}"
  resource_group_name = azurerm_resource_group.rg.name
  virtual_network_name= azurerm_virtual_network.vnet.name
  address_prefixes    = ["10.0.${count.index + 1}.0/24"]
}

locals {
  tiers = var.tiers
}

resource "azurerm_linux_virtual_machine_scale_set" "tiers" {
  for_each            = toset(local.tiers)

  name                = "${each.key}-vmss"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = var.vm_size
  instances           = var.instance_count
  zone_balance        = true
  zones               = var.zones

  admin_username      = var.admin_username
  disable_password_authentication = false
  admin_password      = var.admin_password

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  network_interface {
    name    = "${each.key}-nic"
    primary = true

    ip_configuration {
      name      = "${each.key}-ipconfig"
      subnet_id = element(azurerm_subnet.subnets[*].id, index(local.tiers, each.key))
    }
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  upgrade_mode = "Manual"
  computer_name_prefix = "${each.key}vm"
}
