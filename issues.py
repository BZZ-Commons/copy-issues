import os
import time

from github import Github, Repository  # needs PyGitHub

GITHUB_SECRET = os.environ['GHSECRET']
FROM_REPO_NAME = os.environ['SOURCE_REPO']
TO_REPO_NAME = os.environ['TARGET_REPO']
ADD_LABELS = os.getenv('ADD_LABELS', 'false')


def main():
    token = Github(GITHUB_SECRET)
    source_repo = token.get_repo(FROM_REPO_NAME)
    target_repo = token.get_repo(TO_REPO_NAME)

    if ADD_LABELS == 'true':
        copy_labels(source_repo, target_repo)
    copy_issues(source_repo, target_repo)


def copy_issues(source_repo: Repository, target_repo: Repository):
    """
    copies the issues from the source repository
    :param source_repo:
    :param target_repo:
    :return:
    """
    source_issues = source_repo.get_issues(state='open', sort='created', direction='asc')
    target_issues = target_repo.get_issues(state='open', sort='created', direction='asc')
    for issue in source_issues:
        if not issue_exists(target_issues, issue.title):
            if ADD_LABELS == 'true':
                target_repo.create_issue(
                    title=issue.title,
                    body=issue.body,
                    labels=issue.labels
                )
            else:
                target_repo.create_issue(
                    title=issue.title,
                    body=issue.body
                )
            time.sleep(3)


def copy_labels(source_repo: Repository, target_repo: Repository):
    """
    copies the labels from the source repository
    :param source_repo:
    :param target_repo:
    :return:
    """
    source_labels = source_repo.get_labels()
    target_labels = target_repo.get_labels()
    for label in source_labels:
        if not label_exists(target_labels, label.name):
            print('new label: ' + label.name)
            target_repo.create_label(
                name=label.name,
                color=label.raw_data.get('color'),
                description=label.raw_data.get('description')
            )
            time.sleep(3)
        else:
            print('old label: ' + label.name)


def issue_exists(target_issues, title):
    """
    checks if the issue already exists in target
    :param target_issues:
    :param title:
    :return:
    """
    for issue in target_issues:
        if issue.title == title:
            return True
    return False


def label_exists(target_labels, label_name):
    """
    checks if the label already exists in target
    :param target_labels:
    :param label_name:
    :return:
    """
    for label in target_labels:
        if label.name == label_name:
            return True
    return False


if __name__ == '__main__':
    main()
