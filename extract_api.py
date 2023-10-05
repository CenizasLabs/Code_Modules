# REQUIREMENTS
import requests

#GLOBAL VARIABLES
# Replace these variables with your GitHub repository details
github_user = "CenizasLabs"
repository_name = "Code_Modules"

#SETUP INSTRUCTIONS
# Define the GitHub API endpoint for the repository's contents
api_url = f"https://api.github.com/repos/{github_user}/{repository_name}/contents"

# FUNCTIONS
# Function to fetch the contents of a specific file from the repository
def get_file_content(file_path):
    response = requests.get(f"{api_url}/{file_path}")
    if response.status_code == 200:
        content = response.json()
        # Decode content if it's base64-encoded (GitHub API returns base64-encoded content)
        if content.get("encoding") == "base64":
            import base64
            return base64.b64decode(content["content"]).decode("utf-8")
        else:
            return content["content"]
    else:       
        return None

# EXAMPLE USAGE:
file_path = "compute_gcd.py"
file_content = get_file_content(file_path)

if file_content:
    print(f"Content of '{file_path}':")
    print(file_content)
else:
    print(f"File '{file_path}' not found in the repository.")
