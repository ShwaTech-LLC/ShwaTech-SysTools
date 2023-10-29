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

# Get all the items in the current directory including all the subfolders and files
$children = Get-ChildItem -Recurse -File

# Generate a manifest of file hashes for every file, this will take a while for large directory trees
$total = $children.Length
$counter = 0
foreach( $child in $children ) {

    # Skip zero-length files
    if( $child.Length -gt 0 ) {

        # Calculate the file hash
        $hash = (Get-FileHash ($child.FullName)).Hash

        # Check the manifest for a file with the same hash
        if( $manifest.ContainsKey( $hash ) ) {

            # Flag the duplicate file and pair it to the original
            $original = $manifest[$hash]
            $notes = [PSCustomObject]@{
                Original = $original.FullName
                Duplicate = $child.FullName
            }
            $duplicates += $notes
        } else {
            # Add the original file to the manifest
            $manifest.Add( $hash, $child )
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
    $duplicates | ForEach-Object {
        Export-Csv -InputObject $_ -Path "duplicates.csv" -Append
    }
}