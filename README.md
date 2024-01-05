# 🛡️ DLP Alert System with Jira Integration

Developed by **Dhruv Jayesh Patel**, this project showcases a lightweight, Python-based Data Loss Prevention (DLP) monitoring system designed to detect suspicious file access and automatically raise security alerts in **Jira**.

---

## 🔍 Overview

This tool continuously monitors critical file paths for sensitive data access (e.g., firmware files, binaries), classifies alerts by type (USB, email, general file access), and creates tickets in Jira for security teams to investigate. It is ideal for small-to-mid-sized organizations looking to implement low-cost internal DLP measures.

---

## 🎯 Key Features

- 🧠 **Behavior-based alert tagging** (`#USB`, `#Email`, `#FileCopy`)
- 🗃️ **auditd-based log monitoring** (Linux)
- ⚙️ **Jira REST API integration** for real-time incident reporting
- 📈 Improves visibility and accountability for internal data access
- ✅ Helps enforce compliance and protect intellectual property (IP)

---

## 🛠️ Technologies Used

- Python 3.x
- auditd (Linux audit logging)
- Jira Cloud REST API
- JSON / subprocess / requests modules

---

## 🔐 Security Use Case

This project is designed for environments where sensitive intellectual property or firmware needs to be monitored for unauthorized access or exfiltration. It helps:

- Detect data leaks or suspicious activity (USB transfers, outbound copies)
- Ensure audit-readiness and compliance
- Enable faster incident response through Jira-based workflows

---

## ⚙️ How It Works

```
+-------------+     +-----------------+     +-------------------------+
| auditd Log  | --> | Python Script    | --> | Jira Cloud (Incident DB) |
| (/var/log)  |     | (parse + post)   |     | via REST API             |
+-------------+     +-----------------+     +-------------------------+
```

1. `auditd` tracks file access in protected directories
2. Python script parses logs, detects file types (e.g., `.bin`, `.zip`)
3. Alerts are tagged and sent to Jira as incidents

---

## 🚀 Installation

### 1. Configure auditd rule

```bash
sudo nano /etc/audit/rules.d/dlp.rules
```

Paste the following:

```
-w /home/engineering/firmware -p rwxa -k dlp_monitor
```

Then restart auditd:

```bash
sudo service auditd restart
```

### 2. Install requirements

```bash
pip install requests
```

### 3. Set your Jira credentials and project key in `dlp_monitor.py`:
- `your_email@example.com`
- `your_jira_api_token`
- `https://your-domain.atlassian.net`
- `"SEC"` or your Jira project key

### 4. Run the script

```bash
python3 dlp_monitor.py
```

---

## 🧪 Example Output

```
[#USB] Suspicious activity: /media/removable/firmware.zip by admin1
[+] Jira ticket created successfully.
```

---

## 📂 File Structure

```
.
├── dlp_monitor.py        # Main script
├── README.md             # This file
└── (optional) dlp.rules  # Audit rule config
```

---

## 📌 Notes

- Intended for Linux environments (Debian, Ubuntu, CentOS)
- Jira Cloud account with API token is required
- Use `cron` or `systemd` to automate execution

---

## 🧠 Future Enhancements

- Email/SIEM integration (e.g., Microsoft Sentinel, Slack alerts)
- Windows version using Sysmon
- Live dashboard with incident tracking

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋 About the Developer

Dhruv Jayesh Patel is a cybersecurity engineer with hands-on experience in DLP, incident response, access control, and forensic analysis. Passionate about building secure and scalable systems that protect data and reduce organizational risk.
