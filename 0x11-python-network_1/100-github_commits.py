#!/usr/bin/python3
"""Dsiplay commits by sha and author
"""
import requests
import sys


def github_commits():
    """Display last ten commits by sha and author
    """
    repo = sys.argv[1]
    owner = sys.argv[2]
    api = f'https://api.github.com/repos/{owner}/{repo}/commits'
    try:
        req = requests.get(api)
        sha = req.json()
        commits = []
        for i in sha:
            commits.append(i)
        new = commits[-10:]
        for i in new:
            print(f"{i['sha']}: {i['commit']['author']['name']}")
    except:
        pass

if __name__ == "__main__":
    github_commits()
