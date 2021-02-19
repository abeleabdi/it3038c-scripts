
#$Hello = "Hello, PowerShell!"
#Write-Host($Hello)
funcation getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

Write-Host(getIP)
$IP = getIP
$Date = ""
$Body = "This machine's IP is $IP. User is $env:usernam. Hostname is $. PowerShell Version. Today's date is $Date"

write-host($Body)

#Send-MailMessage -To "abeleabdi@gmail.com" -From "abeleabdi@gmail.com" -Subject "IT3038c windows SysInfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Certificatel) 




