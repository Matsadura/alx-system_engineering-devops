# Exploring Shell Init Files, Variables, and Expansions: Building a Strong Foundation

"Shell Variables and Expansions" are core concepts in shell scripting, providing a way to store and manipulate data dynamically. They enhance the flexibility and reusability of scripts. Some key concepts:

1. **Variables:**
   - **Defining Variables:** Variables are created by assigning a value to a name. No spaces are allowed around the equal sign.
     - Example: `name="John"`

   - **Accessing Variables:** To access the value of a variable, prefix its name with a dollar sign (`$`).
     - Example: `echo $name`

   - **Variable Naming Conventions:** Variable names are typically in uppercase to distinguish them from commands or other elements.

2. **Environment Variables:**
   - **System-wide Variables:** Environment variables are accessible by all processes running in a shell session.
     - Example: `echo $HOME`

   - **Common Environment Variables:**
     - `PATH`: Defines the directories where executable files are located.
     - `USER` or `LOGNAME`: Holds the username of the current user.
     - `PWD`: Represents the present working directory.

3. **Expansions:**
   - **Command Substitution:** Allows the output of a command to replace the command itself.
     - Example: `echo "Today is $(date)"`

   - **Variable Expansion:** The shell expands variables when they are referenced.
     - Example: `echo "Hello, $name!"`

   - **Arithmetic Expansion:** Performs arithmetic operations within double parentheses.
     - Example: `result=$((5 + 3))`

   - **Wildcard Expansion (Globbing):** Matches filenames based on patterns.
     - Example: `ls *.txt`

   - **Tilde Expansion:** Expands the tilde (`~`) to represent the home directory.
     - Example: `cd ~/Documents`

4. **Quoting:**
   - **Single Quotes (`'`):** Preserves the literal value of each character within the quotes.
     - Example: `echo 'This is $HOME'`

   - **Double Quotes (`"`):** Permits variable and command substitution.
     - Example: `echo "Welcome, $USER"`

   - **Backticks (``):** Older form of command substitution; generally replaced by `$(...)`.
     - Example: ``echo "Today is `date`"``

5. **Default Values and Substitution:**
   - **Variable Assignment with Default Value:** Provides a default value if the variable is unset.
     - Example: `greeting=${greeting:-"Hello"}`

   - **Variable Substitution:** Replaces part of a variable's content.
     - Example: `fruit="apple"; echo ${fruit/a/A}`


| File      | Description |
|-----------|-----|
| [0-alias](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/0-alias)     | Creates an alias, name: ``ls``, value: ``rm *``  |
| [1-hello_you](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/1-hello_you)     | Prints ``hello user``, where user is the current Linux user.  |
| [2-path](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/2-path)      | Adds ``/action`` to the ``PATH``. ``/action`` should be the last directory the shell looks into when looking for a program.  |
| [3-paths](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/3-paths)     | Counts the number of directories in the ``PATH``.  |
| [4-global_variables](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/4-global_variables)     | Lists environment variables.  |
| [5-local_variables](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/5-local_variables)      | Lists all local variables and environment variables, and functions.  |
| [6-create_local_variable](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/6-create_local_variable)     | Creates a new local variable, name: ``BEST``, value: ``School``  |
| [7-create_global_variable](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/7-create_global_variable)     | Creates a new global variable, name: ``BEST``, value: ``School``  |
| [8-true_knowledge](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/8-true_knowledge)     | Prints the result of the addition of 128 with the value stored in the environment variable ``TRUEKNOWLEDGE``, followed by a new line.  |
| [9-divide_and_rule](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/9-divide_and_rule)      | Prints the result of ``POWER`` divided by ``DIVIDE``, followed by a new line, ``POWER`` and ``DIVIDE`` are environment variables  |
| [10-love_exponent_breath](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/10-love_exponent_breath)      | Displays the result of ``BREATH`` to the power ``LOVE``, ``BREATH`` and ``LOVE`` are environment variables  |
| [11-binary_to_decimal](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/11-binary_to_decimal)       | Converts a number from base 2 to base 10, the number in base 2 is stored in the environment variable ``BINARY``  |
| [12-combinations](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/12-combinations)      | Prints all possible combinations of two letters, except ``oo``, letters are lower cases, from ``a`` to ``z``, one combination per line, the output ìs alpha ordered, starting with ``aa``, does not print ``oo``  |
| [13-print_float](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/13-print_float)      | Prints a number with two decimal places, followed by a new line, the number will be stored in the environment variable ``NUM``.  |
| [100-decimal_to_hexadecimal](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/100-decimal_to_hexadecimal)      | Converts a number from base 10 to base 16, the number in base 10 is stored in the environment variable ``DECIMAL``  |
| [101-rot13](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/101-rot13)    | Encodes and decodes text using the rot13 encryption.  |
| [102-odd](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/102-odd)     | Prints every other line from the input, starting with the first line.  |
| [103-water_and_stir](https://github.com/Matsadura/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/103-water_and_stir)     | Adds the two numbers stored in the environment variables ``WATER`` and ``STIR`` and prints the result, ``WATER`` is in base ``water``, ``STIR`` is in base ``stir``, the result is in base ``bestchol``  |
