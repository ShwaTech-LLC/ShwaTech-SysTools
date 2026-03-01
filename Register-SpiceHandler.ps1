<#
    .SYNOPSIS
    Registers the spice://server:port protocol handler in the Windows registry if it is not already registered.
    .NOTES
    This script requires Windows PowerShell 5.0 and must be run as an administrator because it modifies the registry.
    .LINK
    https://virt-manager.org/download.html
#>
if( $PSVersionTable.PSVersion.Major -ne 5 ) {
    Write-Warning "This script requires Windows PowerShell 5.0"
    exit
}
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Warning "You must run this script as an administrator because it modifies the registry."
    exit
}
$download = 'https://virt-manager.org/download.html'
$target = 'remote-viewer.exe'
$found = $env:ProgramFiles,${env:ProgramFiles(x86)} | ForEach-Object {
    Get-ChildItem -Path $_ -Filter $target -Recurse -ErrorAction SilentlyContinue
}
if( $found ) {
    "Found [$target] at [$($found.FullName)]"
}
else {
    Write-Warning "Could not find [$target] target application, please download from $download"
    exit
}
if( $found.Length -gt 1 ) {
    # 64-bit application takes priority
    $found = $found[0]
    "Registering [$found] as spice handler"
}
$spicy = Get-ChildItem -Path Registry::HKEY_CLASSES_ROOT | Where-Object { $_.Name -like '*spice' }
if( $spicy ) {
    "Spice handler already registered at [$spicy]"
    exit
}
$null = New-Item -Path Registry::HKEY_CLASSES_ROOT\spice -Force
$null = New-ItemProperty -Path Registry::HKEY_CLASSES_ROOT\spice -Name 'URL Protocol' -PropertyType String -Value '' -Force
$null = New-Item -Path Registry::HKEY_CLASSES_ROOT\spice\shell -Force
$null = New-Item -Path Registry::HKEY_CLASSES_ROOT\spice\shell\open -Force
$null = New-Item -Path Registry::HKEY_CLASSES_ROOT\spice\shell\open\command -Force
$runTarget = "`"$($found.FullName)`" `"%1`""
Set-ItemProperty -Path Registry::HKEY_CLASSES_ROOT\spice\shell\open\command -Name '(default)' -Value $runTarget -Force