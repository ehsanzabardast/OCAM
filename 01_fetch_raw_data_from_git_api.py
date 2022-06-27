import requests
import pandas as pd

owner = 'apache'
access_token = 'UNKNOWN'

try:
    access_token = open('token','r').readline().rstrip()
except:
    print('Unable to read "./token" file')
    quit()

headers = {'Authorization': "Token " + access_token}

repos = []
for page_num in range(1, 300):
    try:
        #  to find all the repos' names from each page
        url = f"https://api.github.com/users/{owner}/repos?page={page_num}"
        repo = requests.get(url, headers=headers).json()
        repos.append(repo)
    except:
        repos.append(None)

df_repos = pd.json_normalize(repos)
df_repos.to_csv(f'repos.csv')

for page in repos:
    if not page:
        print(repos.index(page))
        break

print(len(repos[1]))

all_repo_names = []
for page in repos:
    for repo in page:
        try:
            all_repo_names.append(repo['full_name'].split("/")[1])
        except:
            pass

print(len(all_repo_names))
