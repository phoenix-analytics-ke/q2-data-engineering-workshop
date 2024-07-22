### Cloning Your First Git Repository

---

`Cloning` is the name given to copying the remote repository to your local machine.  When you clone a repository you have am exact copy of everything that has ever happened in the repository.

Go to github and click on the green button with the label `Code`

The URL for cloning the repository should have the following format> 

```
https://github.com/<your_git_username>/<your_repository_name>
```

For instance, if your github username is `smooth_operator`, and your repository is name `kenya-weather-data`, the link to your repository should look like this.

    https://github.com/codebot/smooth_operator/kenya-weather-data.git

#### Git Clone

To clone the repository, open the terminal in your working directory, and paste the following command in your git repository.

```sh
git clone https://github.com/gunnarmorling/awesome-opensource-data-engineering.git
```

Running the command in the terminal should look like something in the screenshot below. Note , this only works after authenticaring your terminal with git.

![](/home/c99/Desktop/phoenix-workshops/phoenix-etl-workshop-q2/01-git-basics/screenshots/git-clone-demo.png)

( *Cloning a git repository using VS Code* )
