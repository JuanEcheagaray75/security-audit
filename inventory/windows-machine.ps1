Write-Output "Hello! Fear not, user. I'm just a script that will list all the installed software on this machine"
$alias = Read-Host -Prompt "Please give me an alias for you"
Write-Output "Thank you, $alias. I will now list all the installed software on this machine"
$INSTALLED = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |  Select-Object DisplayName, DisplayVersion, Publisher, InstallDate
$INSTALLED += Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate
$INSTALLED | Where-Object{ $_.DisplayName -ne $null } | sort-object -Property DisplayName -Unique | Format-Table -AutoSize
# Write the output to a file named $alias.txt
$DIR = Get-Location
$INSTALLED | Export-CSV "$DIR\$($alias).csv" -Append -NoTypeInformation -Force
Write-Output "I've saved the list of installed software, thank you $alias"