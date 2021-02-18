# dependancies
import os
import subprocess
import time

# Config for remote repo


def gitRemote(title):
    try:
        repo = "git remote add origin git@github.com:Chrisvimu/"+title+".git"
        push = "git push --set-upstream -f origin master"
        subprocess.run(repo, check=True, shell=True)
        subprocess.run(push, check=True, shell=True)
        print(repo)
    except Exception:
        print("Error, cant greate repo")

# Frist steps for github repo creation


def gitInit(title):
    try:
        subprocess.run(["ls"])
        os.chdir(title)
        subprocess.run(["ls"])
        subprocess.call(["git", "init"])
        subprocess.run("git add *",  check=True, shell=True)
        subprocess.run(f"git commit -m 'Created repo by script'",
                       check=True, shell=True)
    except Exception:
        print("Error, cant greate repo")


# initialize path as a git repository
def gitRepoCreator(title):
    try:
        gitInit(title)
        gitRemote(title)
        print("Repository created visit github")
    except Exception:
        print("Error, can't get to " + title)


# Only calls other
def main(title):
    gitRepoCreator(title)
