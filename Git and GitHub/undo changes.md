
## undo changes:

### befor committing:
    git reset --hard
    git checkout -- proteins.txt

### after committing:     
    to last commit:
        git revert adbd940 (with undoing the changes)
    to specific commit:     
        git checkout commitid -- filename (without undoing the changes)
        git checkout commitid (without undoing the changes)
        git checkout master (return to the latest commit)


