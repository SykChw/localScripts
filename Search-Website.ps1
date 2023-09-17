# Define the search query
#for string arguments that have whitespaces, replace whitespace with +
param (
    [Parameter(Mandatory = $True)][String] $company,
    [Parameter(Mandatory = $True)][String] $role,
    [String] $site = "linkedin.com"
)

# Define the URL for the search
$searchUrl = "https://www.google.com/search?client=firefox-b-d&q=inurl%3A$site+%22$company%22+%22$role%22"

# Start Firefox with the search URL
Start-Process "firefox.exe" -ArgumentList $searchUrl

# Optionally, you can add a delay to allow Firefox to open before closing the script
Start-Sleep -Seconds 5  # Wait for 5 seconds (adjust as needed)

# You can add more code here to interact with the Firefox window if needed
# For example, you can use the Send-Keys cmdlet to send keys to the Firefox window.

# Close the script
Exit
