import requests
import pandas as pd

BASE_URL = 'https://api.github.com'
MAX_PAGE_NUM = 100


def __headers(token: str):
    return {
        'Accept': 'application/vnd.github+json',
        'Authorization': "Token " + token}


def __req(url: str, token: str) -> pd.DataFrame:
    df = pd.DataFrame()
    for page_num in range(1, MAX_PAGE_NUM):
        url_page = url + '&page=' + str(page_num)
        total_pr_json = requests.get(url_page, headers=__headers(token)).json()
        df_page = pd.DataFrame(total_pr_json)

        is_empty = df_page.shape[0] == 0
        if is_empty:
            break

        df = pd.concat([df, df_page], ignore_index=True)
    return df


def all(token: str, repo: str):
    pull_requests(token, repo)
    issues(token, repo)


def pull_requests(token: str, repo: str) -> pd.DataFrame:
    print('Fetch pull requests from', repo)
    url = f'{BASE_URL}/repos/{repo}/pulls?state=all'
    df = __req(url, token)
    print('Fetched pull requests:', df.shape[0])
    return df


def issues(token: str, repo: str) -> pd.DataFrame:
    print('Fetch issues from', repo)
    url = f'{BASE_URL}/repos/{repo}/issues?state=all'
    df = __req(url, token)
    print('Fetched issues:', df.shape[0])
    return df
