
## Quick Intro to Windows Terminal Commands & Github 

## Goal 
Successfully learn how to use a terminal on your PC, navigate through your computer faster using these basic commands and more about [Github.com](https://github.com/)

## What is Github? 
Github is a code hosting platform for version control and team collaborations. You and others can work on, manage or maintain your projects from anywhere. It also allows you to contribute code to their open source developer project community! 


## What is a Repository?

A repository is used to organize projects that is created. These repositories can contain just about anything that your project needs such as folders, files, images, videos, spreadsheets etc... 


## What is Git?

Open source version control system that Gitub uses for it's platform. It was developed by Linus Torvalds in 2005. 


## What is a Terminal?

A terminal also known as a command prompt(cmd) in Windows is an operating system that allows you to send text-based commands to your computer. 


## Windows Terminal Commands 

| Command       | 	Summary  | 
| ------------- |:-------------:| 
| cd    		| short-hand version used to display the drive letter and folder that you are currently in.| 
| cmd           | starts a new instance of the cmd.exe command interpreter| 
| dir 			| used to display a list of files and folders contained inside the folder that you are currently working in. |  
| del			| used to delete one or more files|  
| cls     		| clears the screen of all previously entered commands and other text.|  
| exit			| starts the MS-DOS Editor tool which is used to create and modify text files.|  
| mkdir		    | command is used to create a new folder|  



## Git Commands 

| Command       | 	Summary  | 
| ------------- |:-------------:| 
| git init 	    | initializes (creates) a git repository in the current directory| 
| ls - a        | list hidden files| 
| git status 	|show modified files in working directory, staged for your next commit|  
| git add / git add . /git add - A|add the untrack file to be committed|  
| git commit -m "initial commit"|commit and include a message about your commit|  
| git push origin master |push your changes to the remote repository|  
| git push|pushing changes after initial configuration|  
| git pull| pulls remote changes if available|  
| git clone| clones a repository into a newly created directory|  
| git fork| a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project|  



## REMEMBER these Git branch commands:
- git checkout <branchname>
		   Switch the current branch to the  <branchname> you specified
- git branch -m, --move
           Move/rename a branch and the corresponding reflog.
- git branch -M
           Shortcut for --move --force.
- git branch --color[=<when>]
           Color branches to highlight current, local, and remote-tracking
           branches. The value must be always (the default), never, or auto.
- git branch [--list | -a, --all]
           List the branches, OR both remote-tracking branches and local branches.
- git branch <branchname>
           The name of the branch to create or delete. The new branch name
           must pass all checks defined by git-check-ref-format(1). Some of
           these checks may restrict the characters allowed in a branch name.
- git branch -D <branchname>
		       Delete the <branchname> branch even if the "master" branch (or
           whichever branch is currently checked out) does not have all
           commits from the test branch.
- git push --set-upstream origin <branchname> 
           Pushes the branch to the remote repo

Here are some examples:
```
$ git branch my2.6.14 v2.6.14
$ git checkout my2.6.14
$ git branch -D test
$ git push --set-upstream origin stats_attack_refactor
```


## Command References for Windows & Github 

[Windows Command Prompt List](https://www.lifewire.com/list-of-command-prompt-commands-4092302)

[Github Command List ](https://education.github.com/git-cheat-sheet-education.pdf)



