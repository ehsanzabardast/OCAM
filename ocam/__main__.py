import core
import fetch
import argparse


def read_token_from_file(filename: str) -> str:
    try:
        access_token = open(filename, 'r').readline().rstrip()
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
    repo = args.repo
    if not access_token:
        access_token = read_token_from_file('token')
    if not access_token:
        print('Unable to continue. No GitHub access token was provided!')
        quit()

    print("OCAM", core.get_version())

    fetch.all(access_token, repo)
