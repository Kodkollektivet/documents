# Documents

This repository contains any documentation related to
Kodkollektivet, such as workflows, policy etc.

## Git workflow

* You are not allowed to merge your own pull requests (PRs).
* Write good git commits that is relevant.
* Rebase of commits is allowed, BUT dont rebase in a way that obfuscates.
* Create branch for every new PR.
* The repo that is in Kodkollektivets is called upstream and we refer that repo as upstream.

### Why?

An essintial part of the projects is to get new members in and the existing to understand the changes.
By not allowing merging by own PRs or direct pushing to the projects, another member must check and understand the code in the PRs.


### How?

Fork a Kodkollektivet repo to your own account using the ![formimg](https://sammyk.s3.amazonaws.com/blog/images/2014-05-28/fork.png)



Clone the repo from YOUR account to your local computer:

```bash
git clone https://github.com/<YOUR_NAME>/<REPO_NAME>.git
```



Add the Kodkollektivet repo as upstream:

```bash
git remote add upstream https://github.com/Kodkollektivet/<REPO_NAME>.git
git pull --rebase upstream master
```



Before you begin working for the day pull changes from upstream (the kodkollektivet repo):

```bash
git pull --rebase upstream master
```



When you are working on a feature or PR create a new branch:

```bash
git checkout -b <FEATURE_NAME>
```



When you push stuff, make sure that you push to YOUR repo:

```bash
git push -u origin <FEATURE_NAME>  # First time
git push origin <FEATURE_NAME>  # When branch is pushed to remote
```



Do a pull request from your branch to upstream.

