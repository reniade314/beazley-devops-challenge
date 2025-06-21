output "vmss_names" {
  value = [
    azurerm_linux_virtual_machine_scale_set.tiers["web"].name,
    azurerm_linux_virtual_machine_scale_set.tiers["app"].name,
    azurerm_linux_virtual_machine_scale_set.tiers["db"].name
  ]
}
