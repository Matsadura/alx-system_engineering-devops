# Mastering Shell Redirections and I/O Filters: Efficiently Managing Data Input, Output, and Filters

"Shell Redirections" are powerful features in command-line interfaces that allow you to control the input and output of commands. They enable you to manipulate the flow of data between commands, files, and even devices. Some key concepts related to shell redirections:

1. **Standard Input (stdin), Standard Output (stdout), and Standard Error (stderr):**
   - Every command in a shell has three default data streams: stdin (0), stdout (1), and stderr (2).
   - stdin is the input stream, while stdout and stderr are output streams.

2. **Redirection Operators:**
   - **`>` (Output Redirection):** Redirects stdout to a file. If the file exists, it will be overwritten; otherwise, a new file will be created.
     - Example: `ls > filelist.txt`

   - **`>>` (Appending Output):** Appends stdout to a file. If the file exists, new content is added; if not, a new file is created.
     - Example: `echo "Additional text" >> filelist.txt`

   - **`<` (Input Redirection):** Takes stdin from a file, providing it as input to a command.
     - Example: `sort < unsorted.txt`

   - **`|` (Pipeline):** Sends stdout of one command as input to another. Allows chaining multiple commands together.
     - Example: `cat file.txt | grep keyword`

   - **`2>` (Error Redirection):** Redirects stderr to a file. Useful for separating error messages from regular output.
     - Example: `command_that_might_fail 2> error.log`

   - **`&>` (Redirects both stdout and stderr):** Sends both standard output and standard error to a file.
     - Example: `command &> output_and_error.log`

3. **Combining Redirections:**
   - You can combine redirections to achieve more complex operations.
     - Example: `command < input.txt > output.txt 2>&1`

4. **Null Device (`/dev/null`):**
   - Redirecting to `/dev/null` discards output or input. It's often used to silence commands or ignore unwanted output.
     - Example: `command > /dev/null`

5. **Here Documents:**
   - A way to provide input to a command directly within a script or command line.
     - Example:
       ```bash
       cat << EndOfText
       This is
       a multiline
       text.
       EndOfText
       ```


| File      | Description |
|-----------|-----|
| [0-hello_world](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/0-hello_world)     | Prints “Hello, World”, followed by a new line to the standard output.  |
| [1-confused_smiley](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/1-confused_smiley)     | Displays a confused smiley ``"(Ôo)'``.  |
| [2-hellofile](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/2-hellofile)      | Displays the content of the ``/etc/passwd`` file. |
| [3-twofiles](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/3-twofiles)     | Displays the content of ``/etc/passwd`` and ``/etc/hosts``  |
| [4-lastlines](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/4-lastlines)     | Displays the last 10 lines of ``/etc/passwd``  |
| [5-firstlines](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/5-firstlines)      | Display the first 10 lines of ``/etc/passwd``  |
| [6-third_line](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/6-third_line)     | Displays the third line of the file ``iacta``.  |
| [7-file](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/7-file)     | Creates a file named exactly ``\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)`` containing the text Best School ending by a new line.  |
| [8-cwd_state](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/8-cwd_state)     | Writes into the file ``ls_cwd_content`` the result of the command ``ls -la``. If the file ``ls_cwd_content`` already exists, it should be overwritten. If the file ``ls_cwd_content`` does not exist, create it.  |
| [9-duplicate_last_line](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/9-duplicate_last_line)      | Duplicates the last line of the file ``iacta``  |
| [10-no_more_js](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/10-no_more_js)      | Deletes all the regular files (not the directories) with a ``.js`` extension that are present in the current directory and all its subfolders.  |
| [11-directories](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/11-directories)       | Counts the number of directories and sub-directories in the current directory, the current and parent directories should not be taken into account, hidden directories should be counted.  |
| [12-newest_files](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/12-newest_files)      | Displays the 10 newest files in the current directory, one file per line and sorted from the newest to the oldest.  |
| [13-unique](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/13-unique)      | Takes a list of words as input and prints only words that appear exactly once, Input format is one line one word, Output format is one line one word, and Words should be sorted.  |
| [14-findthatword](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/14-findthatword)      | Displays lines containing the pattern “root” from the file ``/etc/passwd``  |
| [15-countthatword](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/15-countthatword)    | Displays the number of lines that contain the pattern “bin” in the file ``/etc/passwd``  |
| [16-whatsnext](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/16-whatsnext)     | Displays lines containing the pattern “root” and 3 lines after them in the file ``/etc/passwd``.  |
| [17-hidethisword](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/17-hidethisword)     | Displays all the lines in the file ``/etc/passwd`` that do not contain the pattern “bin”.  |
| [18-letteronly](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/18-letteronly)    | Displays all lines of the file ``/etc/ssh/sshd_config`` starting with a letter.  |
| [19-AZ](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/19-AZ)       | Replaces all characters ``A`` and ``c`` from input to ``Z`` and ``e`` respectively.  |
| [20-hiago](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/20-hiago)     | Removes all letters ``c`` and ``C`` from input.  |
| [21-reverse](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/21-reverse)      | Reverses its input.  |
| [22-users_and_homes](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/22-users_and_homes)      | Displays all users and their home directories, sorted by users, based on the the ``/etc/passwd`` file .  |
| [100-empty_casks](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/100-empty_casks)    | Finds all empty files and directories in the current directory and all sub-directories, only the names of the files and directories should be displayed (not the entire path), hidden files should be listed, one file name per line, the listing should end with a new line. |
| [101-gifs](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/101-gifs)     | Lists all the files with a .gif extension in the current directory and all its sub-directories, Hidden files should be listed, only regular files (not directories) should be listed; the names of the files should be displayed without their extensions, the files should be sorted by byte values, but case-insensitive (file ``aaa`` should be listed before file ``bbb``, file ``.b`` should be listed before file ``a``, and file ``Rona`` should be listed after file ``jay``), one file name per line, the listing should end with a new line.  |
| [102-acrostic](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/102-acrostic)     | Decodes acrostics that use the first letter of each line, the ‘decoded’ message has to end with a new line.  |
| [103-the_biggest_fan](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x02-shell_redirections/103-the_biggest_fan)    | Parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests, order by number of requests, most active host or IP at the top. |
