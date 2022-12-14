import time
import os

from github import Github   # needs PyGitHub

github_secret = os.environ['GHSECRET']
from_repo_name = os.environ['SOURCE_REPO']
to_repo_name = os.environ['TARGET_REPO']

print('From: ' + from_repo_name)
print('To:   ' + to_repo_name)


def main():

    token = Github(github_secret)
    source_repo = token.get_repo(from_repo_name)
    target_repo = token.get_repo(to_repo_name)
    source_issues = source_repo.get_issues(state='open', sort='created', direction='asc')
    target_issues = target_repo.get_issues(state='open', sort='created', direction='asc')
    for issue in source_issues:
        if not issue_exists(target_issues, issue.title):
            target_repo.create_issue(
                issue.title,
                issue.body
            )
            print(issue.title)
            time.sleep(5)


def issue_exists(target_issues, title):
    for issue in target_issues:
        if issue.title == title:
            return True
    return False


if __name__ == '__main__':
    main()
