import requests
import sys
import json

repos = "loopchain"
url = f"https://api.github.com/repos/icon-project/{repos}/pulls"
pr_list = requests.get(url, verify=False).json()
# pr_list = open("test.json").read()
# pr_list = json.loads(pr_list)
# print(type(pr_list))


all_notifications = [f"*=====오늘의 '{repos}' PR 리스트 ({len(pr_list)} 개)=====*\n"]

for idx, pr in enumerate(pr_list, start=1):
    all_notifications.append(f"*{pr['title']}*\n> {pr['html_url']}\n\n")

with open("results", "w") as f:
    f.writelines(all_notifications)
