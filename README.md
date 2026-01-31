# ShwaTech-SysTools
A collection of PowerShell scripts and modules for administering various on-prem and cloud systems.

## Clear-WatchFolder.ps1
* Purpose: To retain files locked by the SharePoint Timer Service.

|Requirements|Version|
|-|-|
|Environment|SharePoint On-Prem|
|PowerShell Version|5.1|
|Scheduled|Yes|

This script must be executed on short intervals by the Windows Task Scheduler.
It will check a `WatchFolder` for files that are older than `CutoffMinutes`.
If any files are found, it will restart the SharePoint Timer Service and move them to the `SafetyFolder`.
This script was created to work-around an incoming email problem with SharePoint Server Subscription Edition.

## Compare-FileTrees.ps1
* Purpose: To deduplicate files contained in separate directories

|Requirements|Version|
|-|-|
|Environment|Any file system|
|PowerShell Version|Any|
|Operating System|Any|
|Scheduled|No, manual script|

This script will compare files in the `Master` directory to those in the `Duplicate` directory and output a report of all identical files to a CSV file named `DuplicateFiles.csv` (by default) into the script directory which can be imported into Excel or imported into a PowerShell variable using `Import-Csv`.
The `Duplicate` property will tell you the full path of the duplicate file.
File comparison is performed using the full contents of the file via `Get-FileHash` so the dates and times are ignored.
Only files whose contents are IDENTICAL will be marked as duplicates.

## Compare-TreeStructures.ps1
* Purpose: To identify files in one directory tree that no longer exist in another directory tree

|Requirements|Version|
|-|-|
|Environment|Any file system|
|PowerShell Version|7|
|Operating System|Any|
|Scheduled|No, manual script|

This script will compare the `Destination` directory tree contents to those in the `Source` directory tree.
Any files found in `Destination` that do not exist in `Source` will be reported.
This script is useful for removing deprecated files when synchronizing contents of a directory that is in active use over long periods of time.

### _Warnings_
* On MacOS and Linux, do not use this script with root paths that are duplicated in subdirectories, for example `/home/user/docs/home/user`. The report results will not be accurate because the script uses the String-Replace method to re-root files into the source tree by replacing the `Destination` with the `Source`. If the `Destination` path appears more than once in the `Source` path, the re-rooted file will contain an incorrect path and the file will be reported to be missing even if it is not. This issue does not occur on Windows because all root paths begin with a drive letter and colon which are only found at the root of the path.

## Deduplicate-Files.ps1
* Purpose: To deduplicate files contained in a single directory tree

|Requirements|Version|
|-|-|
|Environment|Any file system|
|PowerShell Version|Any|
|Operating System|Any|
|Scheduled|No, manual script|

This script will compare files in the `Path` or `LiteralPath` directory and output a report of all identical files to a CSV file named `DuplicateFiles.csv` (by default) into the script directory which can be imported into Excel or imported into a PowerShell variable using `Import-Csv`.
The `Duplicate` property will tell you the full path of the duplicate file.
File comparison is performed using the full contents of the file via `Get-FileHash` so the dates and times are ignored.
Only files whose contents are IDENTICAL will be marked as duplicates.

## Generate-Files.ps1
* Purpose: To generate random files for testing

|Requirements|Version|
|-|-|
|Environment|Any file system|
|PowerShell Version|Any|
|Operating System|Any|
|Scheduled|No, manual script|

Give this script a `Path` and `NumberOfFiles` and it will generate that many random binary files between `MinimumFileSize` and `MaximumFileSize` in the specified path.
You can also created random subfolders with the `RandomSubFolders` switch.

## New-EntraAppCert.ps1
* Purpose: To create Microsoft Entra ID app-based authentication certificates

|Requirements|Version|
|-|-|
|Environment|Windows|
|PowerShell Version|5.1|
|Operating System|Windows|
|Scheduled|No, manual script|

This script will create a self-signed public and private key pair __FOR THE CURRENT USER__ given the name of an app registration.
The public key can then be uploaded to Microsoft Entra ID in the App Registrations certificates section to allow the current user to authentcate as the app.
This is necessary for modern authentication of custom scripts and applications which access Microsoft 365 resources from command line tools or other code which is not running under the context of a logged in user with an access token.

The script requires an `AppRegistrationName` which should match the name of the Enterprise Application you created in Microsoft Entra ID so that the common name of the certificate matches the app name.  The public and private key are saved to the current directory, a `certificate.json` file is created which contains the thumbprint needed for applications to find the certificate, and the certificate is saved into the `My` store for the current user. You can delete the private key file as it is not needed, but it is generated in case you do need it. The private key is protected by a random password which you can find the `certificate.json` file.

## Prune-Path.ps1
* Purpose: To remove empty directories from a file tree

|Requirements|Version|
|-|-|
|Environment|Any file system|
|PowerShell Version|Any|
|Operating System|Any|
|Scheduled|No, manual script|

This script will recursively remove all empty directories at the directory specified by `Path`. By default, this script will echo all deleted directories to the console. To suppress this, include the `Quiet` parameter.

## Remove-Duplicates.ps1
* Purpose: To remove duplicate files detected by `Compare-FileTrees.ps1` or `Deduplicate-Files.ps1`

|Requirements|Version|
|-|-|
|Environment|Any file system|
|PowerShell Version|Any|
|Operating System|Any|
|Scheduled|No, manual script|

This script will open the `DuplicateFiles.csv` report and delete all the duplicate files, prompting for confirmation before proceeding.

## Run-NetworkStabilityTest.ps1
* Purpose: To confirm stable network connectivity between two hosts over a long period of time

|Requirements|Version|
|-|-|
|Environment|Local network or Internet|
|PowerShell Version|7|
|Operating System|Any|
|Scheduled|No, manual script|

This script will run in client mode or `HostMode`.
When in client mode, the default mode, it will open a TCP listener at the specified `Port` and await a connection from the host.
When in host mode, you specify the `Target` client to connect with.
Once connected the script will periodically send data back and forth between the devices until the connection is interrupted.
The amount of connections and data sent will be written to the console upon disconnection.
This has only been tested on PowerShell 7, but it may work on PowerShell 5.1 as well.

## Test-TcpConnection.ps1
* Purpose: To inspect a TCP data payload

|Requirements|Version|
|-|-|
|Environment|Local network or Internet|
|PowerShell Version|7|
|Operating System|Any|
|Scheduled|No, manual script|

This handy script can run in client mode (default) or `HostMode`.
In client mode, you can send an arbitrary `Data` payload to any network target and the response will be echoed to the console.
This can be used for port scanning and service discovery.

In host mode, the script will open a TCP listener on the `Port` you specify and echo the first incoming data payload to the console then close.
This can be used to see what a particular client is sending a host upon connection.
This has only been tested on PowerShell 7, but it may work on PowerShell 5.1 as well.

# License
The software in this repository is provided free of charge under the [MIT license](https://github.com/ShwaTech-LLC/ShwaTech-SysTools/blob/main/LICENSE).

# References
## Microsoft Graph
### [https://learn.microsoft.com/en-us/powershell/microsoftgraph/get-started?view=graph-powershell-1.0](https://learn.microsoft.com/en-us/powershell/microsoftgraph/get-started?view=graph-powershell-1.0)