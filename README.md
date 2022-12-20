

# copy-issues

Scripts and workflows to copy issues from a source repository to a target repository.

I made this script and the workflows to work with GitHub Classrooms. When the user accepts an assignment, he gets a copy of the template repository without the issues. 

I couldn't find an easy solution to import all the issues from the template to the users copy. As any good software engineer would, I wrote my own solution.
So far the workflows work only if the source repository is *public*.

## Stand alone

The python file can be run directly with the settings in the .env-file.
If you create a personal access token and enter it in the .env-file, this should work with private repositories.

 1. Copy the files `issue.py`, `requirements.txt` and `.env` to your machine
 2. Install the requirements
 3. Change the settings in the .env-file

## GitHub manual workflow

In `/.github/workflows/manual-copy.yml` you find the manual GitHub workflow. 
1. Copy this workflow to the target repository
2. Execute the workflow
  2.1. Enter the **owner/repo-name** of the public repository with the issues you want to copy
  2.2. Select if you want to copy the labels

## GitHub automatic workflow

In `/.github/workflows/auto-copy.yml` you find the automatic GitHub workflow.
This workflow is executed when the classroom-bot creates the repository for an accepted assignment.
1. Copy this workflow to the template repository
2. Change the **SOURCE_REPO** to the **owner/name** of your template
3. Create an assignment with this template
4. When the students accept the assignment, they get a copy of the repository. The workflow will then import all the issues.

## Settings
| Setting | Format | Description |
|--|--|--|
| GHSECRET | String | (personal) access token |
| SOURCE_REPO | owner/name | the source repository the issues (and labels) will be copied from |
| TARGET_REPO | owner/name | the target repository the issues (and labels) will be copied to |
| ADD_LABELS | "true" / "false" | shall the labels be copied too |

When using one of the workflows, the GHSECRET and TARGET_REPO are set from the repository in which the action is executed.

## Remarks
- If a script sends too many requests to GitHub, it will get a "secondary rate limit" exception. To avoid this, the 'time.sleep(n)'-command slows down the execution.
