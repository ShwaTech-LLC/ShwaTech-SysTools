<#
    .SYNOPSIS
    Generates a 256-bit RSA public and private key for app-based authentication with Microsoft Azure Entra ID.
    .PARAMETER AppRegistrationName
    The name of the App Registration in Microsoft Azure Entra ID.
    This must match the name exactly.
#>
param(
    [Parameter(Mandatory)]
    [string]
    $AppRegistrationName
)

# Assert preconditions
if( $PSVersionTable.PSVersion.Major -ne 5 ) {
    throw "You must use PowerShell 5"
}
if( -not $AppRegistrationName ) {
    throw "You must specify an app registration name"
}

# Create a password for the certificate file
Add-Type -AssemblyName "System.Web"
$certSec = [System.Web.Security.Membership]::GeneratePassword( 32, 0 )
$certStr = ConvertTo-SecureString -String $certSec -Force -AsPlainText

# Generate the certificate
$cert = New-SelfSignedCertificate -CertStoreLocation "Cert:\CurrentUser\My" -Subject "CN=$AppRegistrationName" -KeyExportPolicy Exportable -KeySpec Signature -KeyLength 2048 -KeyAlgorithm RSA -HashAlgorithm SHA256
if( -not $cert ) {
    throw "Certificate was not generated"
}

# Export the certificate files
$cer = Export-Certificate -Cert $cert -FilePath (Join-Path -Path $PSScriptRoot -ChildPath "$AppRegistrationName-public.cer")
$pfx = Export-PfxCertificate -Cert $cert -FilePath (Join-Path -Path $PSScriptRoot -ChildPath "$AppRegistrationName-private.pfx") -Password $certStr

# Exporting the thumbprint
Write-Host "App registration name:  $AppRegistrationName"
Write-Host "Certificate password:   $certSec"
Write-Host "Certificate thumbprint: $($cert.Thumbprint)"
Write-Host "Private key file:       $($pfx.FullName)"
Write-Host "Public key file:        $($cer.FullName)"
Write-Host "Certificate details:    $PSScriptRoot\certificate.json"

# Save the details to a file
$certDetails = [PSCustomObject]@{
    CertApp = $AppRegistrationName
    CertPw = $certSec
    CertThumb = $cert.Thumbprint
    CertPvt = $pfx.FullName
    CertPub = $cer.FullName
    CertDetails = "$PSScriptRoot\certificate.json"
}
$certDetails | ConvertTo-Json | Out-File "$PSScriptRoot\certificate.json" -Force