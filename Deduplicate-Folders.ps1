param(
    [Parameter(Mandatory=$true)]
    [string]$Master,
    [Parameter(Mandatory=$true)]
    [string]$Duplicate,
    [Parameter(Mandatory=$false)]
    [ValidateRange(1,999999999)]
    [int]$HardLimit = [Int32]::MaxValue,
    [Parameter(Mandatory=$false)]
    [switch]$TreatZeroAsDuplicate
)
if( -not (Test-Path $Master) ) {
    Write-Error "Path specified as Master $Master does not exist or cannot be accessed"
    exit
}
if( -not (Test-Path $Duplicate) ) {
    Write-Error "Path specified as Duplicate $Duplicate does not exist or cannot be accessed"
    exit
}
$master = @{}
$duplicates = @()
$children = Get-ChildItem -Path $Master -Recurse -File
$total = $children.Length
$counter = 0
foreach( $child in $children ) {
    if( $child.Length -gt 0 ) {
        $hash = (Get-FileHash ($child.FullName)).
        if( $hash ) {
            if( $master.ContainsKey( $hash ) ) {
                $duplicates += $child
            } else {
                $master.Add( $hash, $child )
            }
        } else {

        }
    } else {
        if( $TreatZeroAsDuplicate ) {
            $duplicates += $child
        }
    }
    $counter++
    if( $counter -gt $HardLimit ) {
        break
    }
    Write-Progress -Activity "Searching for Duplicates" -Status "In Progress ($counter of $total)" -PercentComplete ($counter / $total * 99.9)
}
if( $duplicates ) {
    $duplicates | ForEach-Object {
        Export-Csv -InputObject $_ -Path "duplicates.csv" -Append
    }
} else {
    Write-Host "No duplicates found"
}