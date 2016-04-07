# Documents
{{ 1+2 }}
This repository contains any documentation related to
Kodkollektivet, such as goals, policy etc.

## Git workflow

* Fork a Kodkollektivet repo to your own account using the ![formimg](https://sammyk.s3.amazonaws.com/blog/images/2014-05-28/fork.png)
* Clone the repo from YOUR account to your local computer
* Add the Kodkollektivet repo as upstream:

```bash
git remote add upstream https://github.com/Kodkollektivet/<REPO NAME>.git
git pull
```

* Before you begin working for the day pull changes from upstream (the kodkollektivet repo)

```bash
git pull upstream master --rebase
```

* When you are working on a feature create a new branch

```bash
git checkout -b <FEATURE NAME>
```




