# Git commands


### Current User
git config user.name
git config user.email

### Switch/Modify User
git config user.name "XXXX"
git config user.email "XXXX@gmail.com"

### Current User
gh auth status
gh auth login
gh auth switch --hostname github.com --user XXXX

### Set Origin
git remote set-url origin https://github.com/XXXX/devops-notes-and-labs.git

## Basics
- Initialize repo: `git init`
- Clone repo: `git clone <url>`
- Check status: `git status`

## Branching
- Create branch: `git checkout -b feature/xyz`
- Merge branch: `git merge feature/xyz`


 git credential-manager --version
