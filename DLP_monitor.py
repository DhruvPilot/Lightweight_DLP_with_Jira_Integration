import subprocess
import json
import requests

# Function to check audit logs for suspicious file access
def check_audit_logs():
    try:
        logs = subprocess.check_output(['ausearch', '-k', 'dlp_monitor', '--format', 'json'])
        log_entries = json.loads(logs)

        for entry in log_entries:
            user = entry['user']['name']
            filepath = entry['paths'][0]['name']
            if filepath.endswith(('.bin', '.hex', '.zip')):
                trigger_dlp_alert(user, filepath)

    except subprocess.CalledProcessError as e:
        print(f"Error fetching audit logs: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON from ausearch output.")
    except Exception as ex:
        print(f"Unexpected error: {ex}")

# Function to classify and trigger alert
def trigger_dlp_alert(user, file):
    if "usb" in file.lower() or "removable" in file.lower():
        tag = "#USB"
    elif "@gmail.com" in file.lower() or "outbound" in file.lower():
        tag = "#Email"
    else:
        tag = "#FileCopy"

    summary = f"{tag} Suspicious activity: {file} by {user}"
    description = f"User {user} accessed or attempted to exfiltrate: {file}. Review required."

    create_jira_ticket(summary, description)

# Function to create a Jira ticket
def create_jira_ticket(summary, description):
    url = "https://your-domain.atlassian.net/rest/api/2/issue"
    auth = ("your_email@example.com", "your_jira_api_token")  # Use Jira API token, not password
    headers = {"Content-Type": "application/json"}

    data = {
        "fields": {
            "project": {"key": "SEC"},  # Replace with your actual project key
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Incident"}
        }
    }

    response = requests.post(url, auth=auth, headers=headers, json=data)
    if response.status_code == 201:
        print("✅ Jira ticket created successfully.")
    else:
        print(f"❌ Failed to create Jira ticket. Status code: {response.status_code}")
        print(response.text)

# Run the script
if __name__ == "__main__":
    check_audit_logs()
