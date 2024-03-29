# Shell Basics: A Beginner's Guide to Command Line and Shell Scripting

## Key Concepts:

``Command Line Interface (CLI)``: Understand the power of interacting with your computer through text commands, providing a more direct and flexible approach than graphical user interfaces.

``Shell``: Learn about shells, such as Bash, which act as a command interpreter, allowing users to execute commands and scripts. Explore the environment where you'll be typing and executing your commands.

``Basic Commands``: Get hands-on experience with fundamental commands like ``ls`` (list files), ``cd`` (change directory), ``cp`` (copy), ``mv`` (move), and ``rm`` (remove). These form the building blocks of command-line navigation and file manipulation.

``File System Navigation``: Delve into navigating the file system hierarchy efficiently using commands like ``pwd`` (print working directory) and ``cd``.


| File      | Description |
|-----------|-----|
| [0-current_working_directory](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/0-current_working_directory)     | prints the path of the current directory  |
| [1-listit](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/1-listit)       | lists the content(files and directories) of current directory  |
| [2-bring_me_home](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/2-bring_me_home)     | changes the working directory to the user’s home directory  |
| [3-listfiles](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/3-listfiles)     | displays current directory contents in a long format  |
| [4-listmorefiles](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/4-listmorefiles)      | displays current directory contents in a long format including files starting with .  |
| [5-listfilesdigitonly](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/5-listfilesdigitonly)     | displays current directory contents in a long format including files starting with . with user and group IDs displayed numerically  |
| [6-firstdirectory](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/6-firstdirectory)     | creates a directory named `my_first_directory` in the `/tmp/` directory  |
| [7-movethatfile](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/7-movethatfile)     | moves the file betty from `/tmp/` to `/tmp/my_first_directory`  |
| [8-firstdelete](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/8-firstdelete)      | deletes file `betty` in `/tmp/my_first_directory`  |
| [9-firstdirdeletion](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/9-firstdeletion)      | deletes directory `my_first_directory` that is in the `/tmp` directory.  |
| [10-back](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/10-back)       | changes working directory to the previous one.  |
| [11-lists](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/11-lists)      | lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format  |
| [12-file_type](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/12-file_type)      | prints the type of the file named `iamafile` in `/tmp`  |
| [13-symbolic_link](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/13-symbolic_link)      | creates a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link is created in the current directory.  |
| [14-copy_html](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/14-copy_html)    | copies all HTML files from current working directory to parent of the working directory, but only files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory are copied.  |
| [100-lets_move](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/100-lets_move)     | moves all files beginning with an uppercase letter to the directory `/tmp/u`  |
| [101-clean_emacs](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/101-clean_emacs)     | deletes all files in the current working directory that end with the character `~`  |
| [102-tree](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/102-tree)    | creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.  |
| [103-commas](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/103-commas)       | lists all the files and directories of the current directory, separated by commas (,), directory names end with a slash (/), files and directories starting with a dot (.) will be listed, listing will be alpha ordered, except for the directories . and .. which should be listed at the very beginning, only digits and letters will be used to sort; digits come first, listing end with a new line  |
| [school.mgc](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x00-shell_basics/school.mgc)     | creates a magic file `school.mgc` that can be used with the command file to detect School data files. School data files always contain the string `SCHOOL` at offset 0.  |
