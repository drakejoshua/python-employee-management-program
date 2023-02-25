# Python employee management program

This is a python practice project used to mock employee management. Built with python 3 and postgreSQL

## Software Requirements
- python must be installed to run the program ( version 3+ )
- postgreSQL must be installed to run the program
- you should look into the python file to configure the program for your own personnal database connection credentials

## How to use?
1. To start using the program, firstly download the code( employeemanagement.py ) as a ZIP archive from the github repo above or using the link: https://github.com/drakejoshua/Python-employee-management-program/archive/refs/heads/main.zip

2. After downloading, unzip the archive and extract the employeemanagement.py from the archive. Then, navigate to the file location of the extracted file on your command line or in vs code and then run the program using the file

> *To run on the command line( command prompt or bash ), run the command:*
>> `C:\file_location>py employeemanagement.py`
>> or
>> `~/file_location>python3 employeemanagement.py`

> *if using visual studio code,*
>> just click 'run' in the menu bar and click 'run without debugging'. This should open up the CLI in the vscode window

3. After running, the program will display some greeting/info and then start loading some employees data:

``` bash
    Welcome to the employee management program by joshua mabawonku




    Fetching employees data from the database........
```

4. it'll then display the data if loaded/found else it'll show an error message and then stop running. it also displays a list of options and a prompt if the data was loaded

``` bash
    Welcome to the employee management program by joshua mabawonku




    Fetching employees data from the database........

    id | name | rate | role | hoursworked
    1 | daniel sullivan | 30 | helper | 15
    2 | joshua mabawonku | 60 | manager | 10


    Select an option:

            1. Add New Employees
            2. Remove Employees
            3. Update Employee Detail
            4. Filter Table Values
            5. Calculate Employees wages
            6. Exit the program

   >>>
```

5. You can choose any option or may wish to exit the program. What each option does won't be described in much detail but a brief description for each option is given in the table below:

| Option | Description |
| :--- | :--- |
| 1. Add New Employees | This adds a new employee. it prompts for an employee name, rate and role and then the new employee data to the database |
| 2. Remove Employees | This removes an existing employee from the database. it prompts for an employee id and then removes the employee with the entered id from the database |
| 3. Update Employee Detail | This updates employee info if any mistakes were made. if prompts for an employee id and then the employee detail to update then the new value for the updated detail |
| 4. Filter Table Values | This allows you to sort or order table details using one of the column names. it prompts for the column name |
| 5. Calculate Employees wages | This calculates the each employee wage and the total overall wages of all employees. it displays a table of each employee with their respective wages and also shows the total wage |

6. After you're done with all operations, you should can close the app by choosing the 'exit the program' option in the menu 

<br><br>

#### About the Author
Hi, i'm mabawonku joshua, i'm a frontend web developer with only one year of tight experience. i aim to build websites, webapps, backends and all other cool stuff for the web. If you're interested in my craft, do well to follow me on github and start a gist and you can send me a email.. i'll reply asap

***Happy Employee Management👋*** <br> **Don't forget to follow me on github:** ***[@drakejoshua](https://github.com/user/drakejoshua)*** 
 
