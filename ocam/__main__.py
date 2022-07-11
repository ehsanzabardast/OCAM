import requests
import core
import argparse

def read_token_from_file(filename: str) -> str:
    try:
        access_token = open(filename,'r').readline().rstrip()
        return access_token
    except:
        print('Unable to read "', filename, '" file')
        return ''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', help='GitHub token to access GitHub API')
    parser.add_argument('repo', help='Repository that shall be analyzed')
    args = parser.parse_args()

    access_token = args.token
    if not access_token:
        access_token = read_token_from_file('token')
    if not access_token:
        print('Unable to continue. No GitHub access token was provided!')
        quit()

    print("OCAM", core.get_version())
    repo = args.repo
    headers = {'Authorization': "Token " + access_token}

    url = f'https://api.github.com/repos/{repo}/pulls?state=all'
    total_pr_json = requests.get(url, headers=headers).json()
    print('All PRs for repository', repo, ':')
    for pr in total_pr_json:
        print(pr['url'])
