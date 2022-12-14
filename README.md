# copy-issues

Scripts to copy issues from a source repository to a target repository.

I made this script and the workflows to work with GitHub Classrooms. When the user accepts an assignment, he get's a copy of the repo without the issues.
So far the workflows work only if the source repository is *public*.

**Stand alone**

The python file can be run directly with the settings in .env
If you create a personal access token and enter it in the .env-file, this should work with private repositories.

**GitHub manual workflow**

In '/.github/workflows/copyissues.yml' you find the manual GitHub workflow. 
- Copy this workflow to the target repository
- Execute the workflow
- Enter the owner/repo-name of the public repo with the issues you want to copy

**GitHub automatic workflow**

In '/.github/workflows/autoscript.yml' you find the automatic GitHub workflow.
This workflow is executed when the classroom-bot creates the repo for an accepted assignment.
- Copy this workflow to the template repository
- Create an assignment with this template
- Students accept the assignment. They get a copy of the repo with all the issues.

**Settings:**
- GHSECRET: (personal) access token
- SOURCE_REPO: the source repository 
- TARGET_REPO: the target repository

**Remarks:**
- The 'time.sleep(n)' avoids too many requests in too short a time. Otherwise GitHub would abort with an error.
