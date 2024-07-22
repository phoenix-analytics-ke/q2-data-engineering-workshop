#### How Git Works Internally

---

Every time you add, edit or delete a file it is tagged with a new version.  This means that even when you delete a file it is not actually completely deleted from the repository.  In fact you can retrieve an older version of the file from a time when it was not deleted.



Git is very very efficient with text files.  Let us say you add 2 lines to a file: Git compares the file before you added the lines with the file after you added the lines.  The comparison is called a "diff".  Git remembers the "diff" instead of remembering both full versions of the file.  



Git has the concept of branches.  When you create a branch from another branch, it has not duplicated all the files of the branch into the other branch.  In fact it has just created a pointer reference.  This means that the size of the repository does not increase much significantly when you create a branch (e.g MB stay roughly the same).



Git works very very IN-efficiently with binary files.  Instead of seeing only 2 changed lines as the diff it will see the whole file as the "diff" - this means that every time you edit a binary file and save it in the repository the MB space used on the file system doubles.



As mentioned above deleting a file does not actually remove all diffs for it in the repository - therefore adding a binary file is a bad bad idea.  However it is very easy to accidentally add binary files to the repository - so how do we stop this?



The answer is that we can stop binary files from being added to the repository by added a `".gitignore"` file to the root of the project after we have cloned it for the first time.

Inside the `.gitignore` file you can add file extensions you do not want checked into the git repository.  Therefore one of the first things you must do after cloning an empty repository for the first time is to create an ".ignore" file and add it to the repository.



---

.gitignore


---



This is how a .gitignore file looks like:

    /.settings/
    /target/
    /.classpath
    /.project
    /.springBeans
    /test-output/
    /logs/
    /trade43.log
    /bin/
    *.class
    *.zip
    *.log
    *.pgsql
    *.DS_Store
    *.factorypath
    *.jar
    /systemproperty

Notice that the file can list individual files, extensions or directories to exclude from git.

Notice that ".gitignore" starts with a dot - this means that the file is normally treated as a "hidden file" in the operating system.

In unix on the command line you have a command called "ls" to show the contents of the directory. 
 If you type "ls" you will not see ".gitignore" as it is a hidden file.

In unix to show hidden files you should instead type:

    ls -a

If you do not know basic unix commands you should do a unix course.
