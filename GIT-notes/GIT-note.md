# git
## check the number of branches 
```
git branch 
```
## change the branch 
```
git checkout <branch-name>
```
## update local machine repo with remote or pull request
```
git pull origin <branch-name>
```
## push the local git repo to remote server or push request
```
git push origin <branch-name>
```
## how to know where the git is pushing (or know the remote push address)
```
git config --get remote.origin.url
```
## create a new branch 
```
git branch <new-branch-name>
```
## create a new branch and go inside it
```
git checkout -b <new-branch-name>
```
## add file 
```
git add <file-name>
git add .    # for all files 
```

## remove file 
```
git rm <file-name>
```

## commit (with message)
```
git commit -m 'your messageg here'
```
(do from within your working branch)
