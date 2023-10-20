# Shell Permissions: Controlling Access to Files and Directories

### Permission Types:

``Read (r)``: Allows a user to view the contents of a file or the names of files in a directory.
``Write (w)``: Permits a user to modify the contents of a file or create, delete, and rename files in a directory.
``Execute (x)``: Enables the execution of a file (for programs or scripts) or the ability to enter a directory.

### Permission Levels:

``User (u)``: The owner of the file or directory.
``Group (g)``: Users who belong to the same group as the file or directory.
``Others (o)``: Users who fall outside the owner and group categories.

### Viewing Permissions:

The ``ls`` command, when used with the ``-l`` option, displays detailed information about files, including their permissions.

### Changing Permissions:

The ``chmod`` command is used to change file and directory permissions.
Example: ``chmod u+r file.txt`` adds read permission for the owner of the file.
Permissions can also be set using octal representation, e.g., ``chmod 755 file.sh``.

### Changing Ownership:

The ``chown`` command is used to change the owner of a file or directory.
Example: ``chown newuser file.txt`` changes the owner of ``file.txt`` to ``newuser``.

### Changing Group:

The ``chgrp`` command changes the group ownership of a file or directory.
Example: ``chgrp newgroup file.txt`` changes the group of ``file.txt`` to ``newgroup``.

### Default Permissions:

The umask value influences the default permissions assigned to newly created files and directories.

| File      | Description |
|-----------|-----|
| [0-iam_betty](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/0-iam_betty)     | switches the current user to the user `betty`.  |
| [1-who_am_i](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/1-who_am_i)      | prints the effective username of the current user.  |
| [2-groups](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/2-groups)     | prints all the groups the current user is part of.  |
| [3-new_owner](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/3-new_owner)     | changes the owner of the file `hello` to the user `betty`.  |
| [4-empty](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/4-empty)      | creates an empty file called `hello`.  |
| [5-execute](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/5-execute)     | adds execute permission to the owner of the file `hello`.  |
| [6-multiple_permissions](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/6-multiple_permissions)     | adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.  |
| [7-everybody](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/7-everybody)     | adds execution permission to the owner, the group owner and the other users, to the file `hello`  |
| [8-James_Bond](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/8-James_Bond)      | sets the permission to the file `hello` as follows: (Owner: no permission at all , Group: no permission at all , Other users: all the permissions  |
| [9-John_Doe](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/9-John_Doe)      | sets the mode of the file `hello` to this: ```-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello```  |
| [10-mirror_permissions](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/10-mirror_permissions)       | sets the mode of the file `hello` the same as `olleh`’s mode.  |
| [11-directories_permissions](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/11-directories_permissions)      | adds execute permission to all subdirectories of the __current directory__ for the owner, the group owner and all other users, regular files should not be changed.  |
| [12-directory_permissions](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/12-directory_permissions)      | creates a directory called `my_dir` with permissions 751 in the working directory.  |
| [13-change_group](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/13-change_group)      | changes the group owner to `school` for the file `hello`  |
| [100-change_owner_and_group](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/100-change_owner_and_group)    | changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.  |
| [101-symbolic_link_permissions](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/101-symbolic_link_permissions)     | changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.  |
| [102-if_only](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/102-if_only)     | changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.  |
| [103-Star_Wars](https://github.com/Matsadura/preparation_alx/blob/master/alx-system_engineering-devops/0x01-shell_permissions/103-Star_Wars)    | will play the StarWars IV episode in the terminal.  |
