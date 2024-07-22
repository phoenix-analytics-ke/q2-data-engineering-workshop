### The Relationship between Git and Scrum

Git is a way of sharing code among developers.  It has a code repository called the Git Repository.

The Git Repository has a url like:

     https://javaspeak.repositoryhosting.com/git/javaspeak/git.git
     
or:

     https://github.com/enigmascore/enigma_test_katalon.git
     
Both the above examples, repositoryhosting.com and github.com offer hosting services allowing you
to create git repositories.  You normally create the repository by using their web page admin 
functionality.

Infact the first url:

    https://javaspeak.repositoryhosting.com/git/javaspeak/git.git
    
is a repository holding this very file you are reading.

Developers can drag the code from that remote url to their local machine.  When done changing the 
code they can push it back to the remote repository.  In git there is the concept of branches.  The 
main branch is called the master.  There are different ways one can work with branches but for the 
purpose of this tutorial we will show you how scrum can use master, feature and release branches to 
work with sprints.

When a repository is made it comes with a default branch called master.   When a developer starts a 
story they make a copy of the master branch and give it a name like:

    feature-1

The number at the end refers to the ID of the story.  The ID has nothing to do with velocity - it is 
just a number associated with the story.  The Developer then modifies, deletes or adds new code to 
that feature branch.  The code of that feature branch is initially stored only on their local 
machine.  The developer can periodically push the local copy of their feature branch to the remote 
server.  When the developer thinks they are done making their changes they can do a final push of 
their feature branch to the remote server.

They then make a pull request.   The pull request is a term for asking one or more other developers 
to pull the feature branch to their local machines so that they can check that the code is good.  
The checking of the code is called a "Dev Review".   Once the code has been reviewed and passes 
the quality controls the Reviewers will tell the Developer that their feature branch passed the 
"Dev Review".

The Developer will at this point merge their feature branch to the master branch.  The merge can be 
smooth or it can have complications.  If the code cannot be merged automatically there are markers 
placed in the files after the merge showing conflicts.  These conflicts show 2 versions of the 
same code in the same file.  When there is a conflict you can see the code of the feature branch 
and the code of the master branch.   You can decide on several actions:

    * keep both versions 
    * reject one version
    * edit both versions manually so the code looks good

The developer will then run some tests to see that the merged code works as expected.  If it looks 
good they push the merged code to the remote server.

During the Sprint each story has a feature branch and each feature branch is merged to master.  

Towards the end of the sprint a release branch is created from the master branch.  An artefact 
(some packaging of the code)  is created from the release branch code and deployed to a test server. 
The testers will test all the stories that are in the release branch.  If they fail a story, the 
code is fixed on the release branch and the release branch is merged to the master branch. Finally 
when all stories have been tested by the Testers on the test server, the artefact is deployed to 
the production server.  The sprint is now complete and the sum of all stories for that sprint are 
counted.  The sum becomes the velocity of that sprint.  If scrum is being followed properly the 
velocity of each sprint should roughly be the same (assuming the same number of people are working 
in the team).