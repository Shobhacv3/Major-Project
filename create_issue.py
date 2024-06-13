
from st2common.runners.base_action import Action
import requests

class CreateIssueAction(Action):
    def run(self, repo_owner, repo_name, title, body, github_token):
        # url = f"https://api.github.com/{repo_owner}/{repo_name}"
        url=f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
        headers = {
            "Authorization": f"Bearer {github_token}",
            # "Accept": "application/vnd.github.v3+json"
            "Accept": "application/vnd.github+json"
        }
        payload = {
            "title": title,
            "body": body
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 201:
            return True, response.json()
        else:
            return False, response.text



