<#
    .SYNOPSIS
    Checks for duplicate files in ths current directory tree.
#>
param(
    [Parameter(Mandatory=$false)]
    [int]$HardLimit = [Int32]::MaxValue
)

# Declare the item manifest table
$manifest = @{}

# Declare the table for storing duplicates
$duplicates = @()

function Write-FileHash {
    param(
        [Parameter(Mandatory=$true)]
        $File,
        [Parameter(Mandatory=$true)]
        [string]
        $Hash
    )
    # Check the manifest for a file with the same hash
    if( $script:manifest.ContainsKey( $Hash ) ) {

        # Flag the duplicate file and pair it to the original
        $original = $script:manifest[$Hash]
        $notes = [PSCustomObject]@{
            Original = $original.FullName
            Duplicate = $File.FullName
        }
        $script:duplicates += $notes
    } else {
        # Add the original file to the manifest
        $script:manifest.Add( $Hash, $File )
    }
}

# Get all the items in the current directory including all the subfolders and files
$children = Get-ChildItem -Recurse -File

# Generate a manifest of file hashes for every file, this will take a while for large directory trees
$total = $children.Length
$counter = 0
foreach( $child in $children ) {
    # Skip zero-length files
    if( $child.Length -gt 0 ) {
        # Calculate the file hash
        $hash = $null
        try {
            $hash = (Get-FileHash ($child.FullName)).Hash
        } catch {
            $hash = $null
        }
        # Report the file hash or warning
        if( $hash ) {
            Write-FileHash -File $child -Hash $hash
        } else {
            Write-Warning "Failed to read file $($child.FullName)"
        }
    } else {
        # Treat all zero-length files as trash
        $notes = [PSCustomObject]@{
            Original = "zero-length file"
            Duplicate = $child.FullName
        }
        $duplicates += $notes
    }
    # Increment the file counter and report progress, stop if the hard limit is reached
    $counter++
    if( $counter -gt $HardLimit ) {
        break
    }
    Write-Progress -Activity "Searching for Duplicates" -Status "In Progress ($counter of $total)" -PercentComplete ($counter / $total * 99.9)
}

# Output the report of all the duplicate files, if any were found
if( $duplicates ) {
    Write-Host "Exporting duplicates to duplicates.csv"
    $duplicates | ForEach-Object {
        Export-Csv -InputObject $_ -Path "duplicates.csv" -Append
    }
} else {
    Write-Host "No duplicate files found"
}