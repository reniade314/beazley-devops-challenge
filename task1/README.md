
This project uses Terraform to deploy a secure and scalable 3-tier architecture in Azure. It provisions separate Virtual Machine Scale Sets (VMSS) for Web, App, and DB tiers, with high availability achieved through distribution across Azure availability zones.

VM size, instance count, and region are fully configurable using input variables. Admin credentials are passed securely via a `terraform.tfvars` file to avoid hardcoding sensitive data.

To get started, log into Azure using `az login` and ensure your subscription is selected using `az account set`. Create a `terraform.tfvars` file with your admin password and desired instance count:

```hcl
admin_password = ""
instance_count  = 3
```

Then run the standard Terraform workflow:
terraform init
terraform plan -out=tfplan
terraform apply tfplan

All Terraform resources are defined in main.tf, with input variables declared in variables.tf