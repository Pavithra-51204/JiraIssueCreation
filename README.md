# 🚀 Automating JIRA Issue Creation via GitHub Events

This project automates JIRA issue creation whenever a specific event occurs in a GitHub repository. It uses **Flask**, **GitHub Webhooks**, and the **JIRA API** to streamline issue tracking and project management.

## 📌 Features
- ✅ Automatically creates JIRA issues based on GitHub events (e.g., new PRs, issues, or commits).
- ✅ Uses **GitHub Webhooks** to trigger JIRA issue creation in real time.
- ✅ Implements secure API communication with JIRA using authentication tokens.
- ✅ Supports **customizable issue templates** for different event types.

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **APIs**: GitHub Webhooks, JIRA REST API
- **Security**: Environment variables for API keys

---

## 🚀 Installation & Setup


```bash
1️⃣ Clone the repository
git clone https://github.com/your-username/JiraIssueCreation.git
cd JiraIssueCreation

2️⃣ Create a Virtual Environment (Optional but Recommended)

python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file and add:

JIRA_API_TOKEN="your_jira_api_token"
JIRA_DOMAIN="yourcompany.atlassian.net"
JIRA_PROJECT_KEY="PROJ"
GITHUB_SECRET="your_github_webhook_secret"

Replace values accordingly.
⚡ Usage
1️⃣ Run the Flask App

python flask-app.py

2️⃣ Set Up GitHub Webhook

    Go to your GitHub Repository → Settings → Webhooks.

    Click "Add webhook".

    Set the Payload URL to your Flask server's endpoint (e.g., http://your-server-url/webhook).

    Select events to trigger (e.g., Pull Requests, Issues).

    Use the same secret key set in the .env file.

📌 Example Webhook Payload (GitHub)

{
  "action": "opened",
  "issue": {
    "title": "Bug: Fix API timeout issue",
    "body": "The API response time exceeds 5 seconds in production."
  },
  "repository": {
    "name": "MyRepo"
  }
}

🎯 Future Enhancements

    🔹 Add support for multiple JIRA projects.

    🔹 Implement AI-based issue categorization.

    🔹 Deploy as a serverless function for better scalability.


🚀 Happy Coding! 🚀


---

### **📌 Instructions to Save**
1. Open your project directory.
2. Create a new file named **`README.md`**.
3. Copy and paste the above content into the file.
4. Save the file.
