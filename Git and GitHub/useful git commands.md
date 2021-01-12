
## What is Git:
    Git is the software that runs on your computer and manages your files;

## What is GitHub:
    GitHub is an online platform that allows you to synchronise your local Git reporitory onto the web.


## Useful Git commands:

git init # initialize a Git repository
git status # check the staging area
git add new_file.txt # add file in staging area
git commit -m 'Initial version' # commit a change
git log # log all commits
git remote add origin URL_OF_GITHUB_REPO # Link Git repo with GitHub repo
git remote remove origin URL_OF_GITHUB_REPO # Link Git repo from GitHub repo
git push -u origin master # push changes to GitHub 
git push # (without the -u origin master) 
git rm new_file.txt # remove file (should be followed by a commit and 'rm new_file.txt'  - same thing when moving files)
---------------------------------------------------------
git reset --hard # go back to repo before change - if changes are not commited
git checkout -- proteins.txt # go back to file before change - if changes are not commited
git revert identifier # reverting the latest commit (identifier that you want to undo, not the one you want to get back to)
git checkout identifier -- filename # obtain an older version of a particular file
git checkout identifier # get back to an older version without actually undoing the changes between that version and the current version
git checkout master # return to the latest commit
---------------------------------------------------------
git checkout -b branchname # create new branch (-b) and switched to 
git branch # see the rurently working branch
git push -u origin branchname # §§§
git commit -m 'make some commit'
git push
git checkout master # return to the master branch
git diff master # differences between the current branch and master branch
git diff # differences from the most recent commit
git diff identifier # differences between the current commit and specified commit
git diff identifier identifier # differences between two specific commits
git checkout master # return to the master branch
git merge branchname # merge branchname in master branch - The merge is automatically committed, 
git push 
git branch -d branchname # delete branch on the local machine
git push origin --delete branchname # necessary efter delete 
git remote prune origin # necessary efter delete 















