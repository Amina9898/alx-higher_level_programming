#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    URL = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repo_name)

    response = requests.get(URL)
    commits = response.json()

    for i in commits[:10]:
        sha = i['sha']
        author_name = i['commit']['author']['name']
        print(f"{sha}: {author_name}")
