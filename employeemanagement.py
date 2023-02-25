# importing the needed modules for the program
import psycopg2

# printing the welcome message
print("    Welcome to the employee management program by joshua mabawonku\n\n\n\n")

# connecting to the database and creating a cursor
# and displaying the employees data
def showEmployees():
    # displaying a loading message
    print("    Fetching employees data from the database........\n")

    global dbConnectSuccess, conn, cur, noOfEmployees

    # fetching employees details from the database, and if not possible
    # displaying some error messages
    # else, displaying the employee details in a table
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="nextgen",
            database = "forte_company"
        )

        cur = conn.cursor()


        dbConnectSuccess = True
    except:
        # the error messages if fetch was unsuccessful
        print("    There was an error fetching the employees data from the database\n")
        print("    Try rerunnning the program again and check if the data server is up and running\n")
        dbConnectSuccess = False

    if dbConnectSuccess:
        cur.execute("SELECT * FROM employees ORDER BY id")

        # the table headings
        print(f"    id | name | rate | role | hoursworked")

        # generating the table data
        for ( employeeId, employeeName, employeeRate, employeeRole, hoursWorked ) in cur.fetchall():
            print(f"    { employeeId } | { employeeName } | { employeeRate } | { employeeRole } | { hoursWorked }")

        cur.execute("SELECT * FROM employees")

        # updating the number of employees found in the data fetched from the database
        noOfEmployees = len( cur.fetchall() ) + 1


# the addNewEmployees function to add a new employee to the database
def addNewEmployees():
    print("""\n   Enter the new employee details\n""")

    # prompting for employee details
    # if "cancel" is entered, the prompting process is stopped and exited back to the main menu
    employeeName = input("\tEnter the name> ")

    if employeeName == 'cancel':
        print("\n    cancelling....\n")

        showEmployees()
        showOptionMenu()
    else:
        employeeRate = input("\tEnter the rate> ")

        if employeeRate == 'cancel':
            print("\n    cancelling....\n")

            showEmployees()
            showOptionMenu()
        else:
            employeeRole = input("\tEnter the role> ")

            if employeeRole == 'cancel':
                print("\n    cancelling....\n")

                showEmployees()
                showOptionMenu()
            else:
                # saving the user data as far as the new employee details were properly entered
                # without any form of cancellation when asking for the data
                # and then, printing a success message, exiting to the main menu
                cur.execute(""" INSERT INTO employees( id, name, rate, role, hoursworked ) 
                                VALUES ( %s, %s, %s, %s, 0 )""", [ noOfEmployees ,employeeName, int( employeeRate ), employeeRole ] )
                conn.commit()

                print(f"{ cur.rowcount } new employee added ")

                showEmployees()
                showOptionMenu()


# the removeEmployees function which is used to remove an existing employees by his/her id
def removeEmployees():
    # prompting for the employee id
    employeeIdToRemove = input("Enter the employee ID from the table/roster> ")

    # checking if the employee id is invalid or if "cancel" was entered in order to terminate the 
    # removal process. if so, stop the process and exit to the main menu.
    if employeeIdToRemove == 'cancel':
        print("\n    cancelling....\n")

        showEmployees()
        showOptionMenu()
    elif int( employeeIdToRemove ) == None or int( employeeIdToRemove ) > noOfEmployees:
        print("\n    employee id entered not found....\n")

        showEmployees()
        showOptionMenu()
    else:
        # deleting the user from the database since a valid id is entered and no cancellation was attempted
        # and then, printing a success message, exiting to the main menu
        cur.execute(""" DELETE FROM employees WHERE id = %s""", [ int( employeeIdToRemove ) ] )
        conn.commit()

        print(f"{ cur.rowcount } employee data deleted ")

        showEmployees()
        showOptionMenu()


# the filterTableValues function which is used to sort the table by a particular column name
def filterTableValues():
    # prompting the user for the parameter to sort by
    sortParam = input("    Enter the column name you want to sort by> ")

    # checking if the column name is invalid or if "cancel" was entered in order to terminate the 
    # removal process. if so, stop the process and exit to the main menu.
    if sortParam == 'cancel':
        print("\n    cancelling....\n")

        showEmployees()
        showOptionMenu()
    elif sortParam != 'id' and sortParam != 'name' and sortParam != 'rate' and sortParam != 'role' and sortParam != "hoursworked":
        print("\n    column name entered not found....\n")

        showEmployees()
        showOptionMenu()
    else:
        # sorting by the column name from the database since a valid column name is entered and no cancellation was attempted
        # and then, printing a success message, exiting to the main menu
        if sortParam == 'name':
            cur.execute("SELECT * FROM employees ORDER BY name" )
        elif sortParam == 'rate':
            cur.execute("SELECT * FROM employees ORDER BY rate" )
        elif sortParam == 'role':
            cur.execute("SELECT * FROM employees ORDER BY role" )
        elif sortParam == 'hoursworked':
            cur.execute("SELECT * FROM employees ORDER BY hoursworked" )
        else:
            cur.execute("SELECT * FROM employees ORDER BY id" )

        # the table headings
        print(f"    id | name | rate | role | hoursworked")

        # generating the table data
        for ( employeeId, employeeName, employeeRate, employeeRole, hoursWorked ) in cur.fetchall():
            print(f"    { employeeId } | { employeeName } | { employeeRate } | { employeeRole } | { hoursWorked }")
        
        showOptionMenu()


def calculateEmployeesWages():
    # variable declarations for this function
    listOfWages = []        # to hold the list of employee details and their respective wages
    totalEmployeeWage = 0   # to hold the total wages of all employees

    # re-fetching the data from database and using it to calculate the wages and
    # displaying the wage per employee in a table and the total employee wages and
    # exit back to the main menu
    cur.execute("SELECT * FROM employees ORDER BY id")

    for ( employeeId, employeeName, employeeRate, employeeRole, hoursWorked ) in cur.fetchall():
        listOfWages.append( { "name": employeeName, "id": employeeId, "wage": ( hoursWorked * employeeRate ) } )
        totalEmployeeWage += ( hoursWorked * employeeRate )

    print( f"\n    id | name | wage " )

    for employeeDict in listOfWages:
        print( f"    { employeeDict['id'] } | { employeeDict['name'] } | ${ employeeDict['wage'] }" )

    print(f'\n    The total employee wage is: ${ totalEmployeeWage }')

    showOptionMenu()


def updateEmployeeDetail():
    # prompting for the employee id
    employeeIdToUpdate = input("    Enter the employee ID from the table/roster> ")

    # checking if the employee id is invalid or if "cancel" was entered in order to terminate the 
    # removal process. if so, stop the process and exit to the main menu.
    if employeeIdToUpdate == 'cancel':
        print("\n    cancelling....\n")

        showEmployees()
        showOptionMenu()
    elif int( employeeIdToUpdate ) == None or int( employeeIdToUpdate ) > noOfEmployees:
        print("\n    employee id entered not found....\n")

        showEmployees()
        showOptionMenu()
    else:
        # prompting for the employee detail to be updated( e.g. role, rate, ... )
        employeeDetailToUpdate = input("    Enter the employee detail to be updated( e.g. role, rate, ... )> ")

        if employeeDetailToUpdate == 'cancel':
            print("\n    cancelled....\n")

            showEmployees()
            showOptionMenu()
        elif employeeDetailToUpdate == 'id':
            print("\n    cancelled... employee ID is read-only and can't be updated\n")

            showEmployees()
            showOptionMenu()
        elif employeeDetailToUpdate != 'name' and employeeDetailToUpdate != 'rate' and employeeDetailToUpdate != 'role' and employeeDetailToUpdate != "hoursworked":
            print("\n    employee detail entered not found....\n")

            showEmployees()
            showOptionMenu()
        else:
            if employeeDetailToUpdate == 'name':
                updateValue = input('    Enter the value to be used for update> ')

                if updateValue != 'cancel':
                    cur.execute( """
                            UPDATE employees
                            SET name = %s
                            WHERE id = %s
                    """, [ updateValue, int( employeeIdToUpdate ) ] )

                    conn.commit()

                    print(f"    { cur.rowcount } employee detail updated\n")

                    showEmployees()
                    showOptionMenu()
                else:
                    print("\n    cancelled\n")
                    showEmployees()
                    showOptionMenu()

            elif employeeDetailToUpdate == 'rate':
                updateValue = input('    Enter the value to be used for update> ')

                if updateValue != 'cancel':
                    cur.execute( """
                            UPDATE employees
                            SET rate = %s
                            WHERE id = %s
                    """, [ int( updateValue ), int( employeeIdToUpdate ) ] )

                    conn.commit()

                    print(f"    { cur.rowcount } employee detail updated\n")

                    showEmployees()
                    showOptionMenu()
                else:
                    print("\n    cancelled\n")
                    showEmployees()
                    showOptionMenu()

            elif employeeDetailToUpdate == 'role':
                updateValue = input('    Enter the value to be used for update> ')

                if updateValue != 'cancel':
                    cur.execute( """
                            UPDATE employees
                            SET role = %s
                            WHERE id = %s
                    """, [ updateValue, int( employeeIdToUpdate ) ] )

                    conn.commit()

                    print(f"    { cur.rowcount } employee detail updated\n")

                    showEmployees()
                    showOptionMenu()
                else:
                    print("\n    cancelled\n")
                    showEmployees()
                    showOptionMenu()

            elif employeeDetailToUpdate == 'hoursworked':
                updateValue = input('    Enter the value to be used for update> ')

                if updateValue != 'cancel':
                    cur.execute("""
                            UPDATE employees
                            SET hoursworked = %s
                            WHERE id = %s
                    """, [ int( updateValue ), int( employeeIdToUpdate ) ])

                    conn.commit()

                    print(f"    { cur.rowcount } employee detail updated\n")

                    showEmployees()
                    showOptionMenu()
                else:
                    print("\n    cancelled\n")
                    showEmployees()
                    showOptionMenu()



# the showOptions function which is used to show the main menu, prompt the user for the action to take and
# take the action based on the user's decision
def showOptionMenu():
    if dbConnectSuccess:
        print("\n\n    Select an option:")

        print("""
            1. Add New Employees
            2. Remove Employees
            3. Update Employee Detail
            4. Filter Table Values
            5. Calculate Employees wages
            6. Exit the program
        """)

        actionCode = input("""   >>> """)

        if actionCode == "1":
            addNewEmployees()
        elif actionCode == "2":
            removeEmployees()
        elif actionCode == "3":
            updateEmployeeDetail()
        elif actionCode == "4":
            filterTableValues()
        elif actionCode == "5":
            calculateEmployeesWages()
        elif actionCode == "6":
            exit()




showEmployees()
showOptionMenu()




