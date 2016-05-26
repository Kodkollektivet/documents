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

`! Before you begin working for the day pull changes from upstream (the kodkollektivet repo): !`


```bash
git pull --rebase upstream master
```


When you are working on a feature or PR create a new branch:

```bash
git checkout -b <BRANCH_NAME>
```


When you push stuff, make sure that you push to YOUR repo:

```bash
git push --set-upstream origin <BRANCH_NAME>
git push origin <BRANCH_NAME>  # When branch is pushed to remote
```


Do a pull request from your branch to upstream.


## How to name a branch?


There are three different branch name startouts: ref/, bug/, and fet/.

* ref/<NAME>  # Refactoring / Improvements
* bug/<NAME>  # Bug
* fet/<NAME>  # Feature
* tes/<NAME>  # Tests


<NAME> is something that represents the branch.

* Example 1: bug/login-utf-chars
* Example 2: fet/external-containers
* Example 3: ref/faster-boot-time
* Example 3: tes/api-tests




