from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

#creating a flask app instance
app = Flask(__name__)

@app.route("/createJIRA". methods=['POST'])
def createJIRA():
    url = "https://<username>.atlassian.net/rest/api/3/issue"

    API_TOKEN=""

    auth = HTTPBasicAuth("<email>", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {

        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10003"
        },
        "project": {
        "key": "SCRUM"
        },
        "summary": "First JIRA Ticket",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0', port=5000)
