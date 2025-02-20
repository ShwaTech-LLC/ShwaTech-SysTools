# https://learn.microsoft.com/en-us/powershell/microsoftgraph/get-started?view=graph-powershell-1.0
param(
    [Parameter(Mandatory)]
    [string]
    $Path,
    [Parameter(Mandatory)]
    [string]
    $Tenant,
    [Parameter(Mandatory)]
    [string]
    $Certificate
)

# Validate and fetch the staff metadata
if( Test-Path $Path ) {
    # OK
} else {
    throw "Staff member CSV file $Path does not exist"
}
$staff = Import-Csv $Path

# Validate the tenant
if( $Tenant -contains '.' ) {
    throw "Tenant name must contain only the root hostname"
}

# Validate and fetch the certificate metadata
if( Test-Path $Certificate ) {
    # OK
} else {
    throw "Certificate metadata file $Certficiate does not exist"
}
. (Join-Path -Path $PSScriptRoot -ChildPath 'Read-EntraAppCert.ps1')
$cert = Read-EntraAppCert -Path $Certificate
if( $cert.CertThumb ) {
    # OK
} else {
    throw "Certificate metadata file $Certificate does not include a thumbprint"
}