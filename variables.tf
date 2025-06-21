variable "location" {
  description = "Azure region to deploy resources in"
  type        = string
  default     = "centralus"  # You can override this in terraform.tfvars if needed
}

variable "admin_username" {
  description = "Admin username for VMSS instances"
  type        = string
  default     = "azureuser"
}

variable "admin_password" {
  description = "Admin password for VMSS instances"
  type        = string
  sensitive   = true
}

variable "instance_count" {
  description = "Number of VM instances per tier"
  type        = number
  default     = 3
}

variable "vm_size" {
  description = "Azure VM size to use for scale sets"
  type        = string
  default     = "Standard_B1ms"
}

variable "tiers" {
  description = "Tier names for the 3-tier architecture"
  type        = list(string)
  default     = ["web", "app", "db"]
}

variable "zones" {
  description = "Availability zones to distribute instances across"
  type        = list(string)
  default     = ["1", "2", "3"]
}
