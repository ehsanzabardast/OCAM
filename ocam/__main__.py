import requests
import core

if __name__ == '__main__':
    print("OCAM", core.get_version())

    try:
        access_token = open('token','r').readline().rstrip()
    except:
        print('Unable to read "./token" file')
        quit()
    headers = {'Authorization': "Token " + access_token}

    repo = 'PerssonAlbin/file-editor_OWN_CPP'
    url = f'https://api.github.com/repos/{repo}/pulls?state=all'
    total_pr_json = requests.get(url, headers=headers).json()
    print('All PRs for repository', repo, ':')
    for pr in total_pr_json:
        print(pr['url'])
