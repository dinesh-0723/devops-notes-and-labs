### Azure Projects List Names
az extension add --name azure-devops
az devops configure --defaults organization=https://dev.azure.com/YourOrg
az devops project list
az devops project list --organization https://dev.azure.com/YourOrg
az devops project list --organization https://dev.azure.com/YourOrg --query "value[].name" -o tsv | sort

### Azure Agent List Names

az pipelines pool list --organization https://dev.azure.com/YourOrg --query "[].{Name:name, ID:id, Type:poolType, Auto:isHosted, Owner:owner.displayName}" --output table | sort