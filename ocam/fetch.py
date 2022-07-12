import requests
import pandas as pd

BASE_URL = 'https://api.github.com'


def __headers(token: str):
    return {
        'Accept': 'application/vnd.github+json',
        'Authorization': "Token " + token
    }


def all(token: str, repo: str):
    pull_requests(token, repo)
    issues(token, repo)


def pull_requests(token: str, repo: str) -> pd.DataFrame:
    print('Fetch pull requests from', repo)
    url = f'{BASE_URL}/repos/{repo}/pulls?state=all'
    total_pr_json = requests.get(url, headers=__headers(token)).json()
    df = pd.DataFrame(total_pr_json)
    print('Fetched pull requests:', df.shape[0])
    return df


def issues(token: str, repo: str) -> pd.DataFrame:
    print('Fetch issues from', repo)
    url = f'{BASE_URL}/repos/{repo}/issues?state=all'
    total_issues_json = requests.get(url, headers=__headers(token)).json()
    df = pd.DataFrame(total_issues_json)
    print('Fetched issues:', df.shape[0])
    return df
