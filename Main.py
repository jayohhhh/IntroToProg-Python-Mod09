# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Jonathan Ou, 6.7.2021, imported modules for usage
# Jonathan Ou, 6.7.2021, loaded data from file
# Jonathan Ou, 6.7.2021, wrote a if conditionals cycling through possible user choices
# ------------------------------------------------------------------------ #
# TODO: Import Modules
# import modules for usage
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# initiate variables for later usage
strFileName = 'EmployeeData.txt'
lstOfEmployeeData = []
lstTable = []

# Load data from file into a list of employee objects when script starts
lstOfEmployeeData = Fp.read_data_from_file(strFileName)
lstTable.clear()
# iterates through file capture all data
for line in lstOfEmployeeData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

while (True):
    # Show user a menu of options
    Eio.print_menu_items()
    # Get user's menu option choice
    strChoice = Eio.input_menu_options()
    # Show user current data in the list of employee objects
    if strChoice == '1':
        Eio.print_current_list_items(lstTable)
        continue
        # Let user add data to the list of employee objects
    elif strChoice == '2':
        # appends input acquired from user when prompted
        lstTable.append(Eio.input_employee_data())
        continue
        # let user save current data to file
    elif strChoice == '3':
        Fp.save_data_to_file(strFileName, lstTable)
        # alerts user that the save has taken place
        print('Your data has been saved!')
        continue
        # Let user exit program
    elif strChoice == '4':
        print('Goodbye!')
        # stops the script from continuing to run
        break
# Main Body of Script  ---------------------------------------------------- #
