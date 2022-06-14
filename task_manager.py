#=====importing libraries===========

from datetime import date
from datetime import datetime
from pathlib import Path


#====Function Section====


def reg_user():
    '''Define function to register a new user.

    Use if statement to check if username inputted is 'admin'.
    If it is, proceed with allowing admin to register new user & request input 
    of a new username.

    Use while loop to check if new username is already regsitered.
    If it is, loop until user enters a username that is not already registered.

    Then request input of a new password and password confirmation.
    Check if the new password and confirmed password are the same.
    If they are the same, add them to the user.txt file using append, also add
    them to the username_list and password_list, otherwise ask user to try again.

    If username inputted is not 'admin', show message to say only admin can
    register new users.
    '''
    new_username_success = False
    if username_input == 'admin':
        new_username = input('\nPlease enter a new username: ')
        while new_username_success == False:
            if new_username in username_list:
                new_username = input('This username is already registered.\n'
                                     '\nPlease enter a new username: ')
            else:
                new_username_success = True
        new_password = input('Please enter a password: ')
        password_conf = input('Please confirm the password: ')
        if new_password == password_conf:
            with open('user.txt', 'a') as user_file:
                user_file.write('\n' + new_username + ', ' + new_password)
                username_list.append(new_username)
                password_list.append(new_password)
                print('New user added successfully.')
        else:
            print('The passwords do not match. Please try again.') 
    else:
        print('\nSorry, only admin can register new users.')


def add_task():
    '''Define function to add a new task to the tasks.txt file.

    Prompt user to enter various details about the task and enter into
    respective variables.

    Add the variables to the tasks.txt file in the correct order using
    append method in order to not overwrite existing fiel data.
    '''
    print("\nPlease enter the following:")
    new_task_user = input('Username of the person whom the task is '
                          'assigned to: ')
    new_task_title = input('Title of the task: ')
    new_task_description = input('Description of the task: ')
    current_date = date.today().strftime("%d %b %Y")  # Get current date.
    new_task_due = input('Due date of the task (i.e. 01 Jan 2000): ')


    with open('tasks.txt', 'a') as tasks_file:
        tasks_file.write(f'\n{new_task_user}, {new_task_title}, '
                        f'{new_task_description}, {current_date}, '
                        f'{new_task_due}, No')
    print('New task added successfully.')


def view_all():
    '''Define function to display information for each task contained 
    in tasks.txt. 

    Open tasks.txt and read every line using for loop.

    Split the line where there is a comma and space and assign to
    respective variables depending on the type of data.

    Then print the data for each task in an easy to read format.
    '''
    tasks_file = open('tasks.txt', 'r')

    for line in tasks_file:
        username, task_title, task_description, \
        date_assigned, due_date, completed = line.split(', ')
        completed = completed.strip('\n')  # Remove line break.

        print(f'''
Task:                 {task_title}
Assigned to:          {username}
Date assigned:        {date_assigned}
Due date:             {due_date}
Task complete?        {completed}
Task description:     {task_description}''')

    tasks_file.close()


def view_mine():
    '''Define function to display information for all tasks for the user
    currently logged in.

    Also allow the user to edit their tasks.
    '''
    # Create task number counter and assign value 0.
    task_no = 0
    # Create empty lists for every type of data in the tasks file.
    task_no_for_user_list = []
    task_no_list = []
    username_list = []
    task_title_list = []
    task_description_list = []
    date_assigned_list = []
    due_date_list = []
    completed_list = []
    
    # Open the tasks file.
    tasks_file = open('tasks.txt', 'r')

    # Read every line of the tasks file using for loop.
    # Split the line where there is comma and space and assign to respective
    # variables depending on the type of data.
    for line in tasks_file:
        username, task_title, task_description, \
        date_assigned, due_date, completed = line.split(', ')
        completed = completed.strip('\n')  # Remove line break.

        # Increase task counter by 1.
        task_no += 1
        # Add the detail about the task to it's respective list using append.
        task_no_list.append(task_no)
        username_list.append(username)
        task_title_list.append(task_title)
        task_description_list.append(task_description)
        date_assigned_list.append(date_assigned)
        due_date_list.append(due_date)
        completed_list.append(completed)

        # Use if statement to check if the username in the line is the 
        # same as the logged in user.
        # If it is, print the data for each task in an easy to read format.
        if username_input == username:
            task_no_for_user_list.append(task_no)
            print(f'''
Task number:          {task_no}
Task:                 {task_title}
Assigned to:          {username}
Date assigned:        {date_assigned}
Due date:             {due_date}
Task complete?        {completed}
Task description:     {task_description}''')

    tasks_file.close()

    # Ask user if they want to select a specific task or return to the menu.
    # If user enters invalid entry, run while loop until valid entry.
    task_no_success = False
    while task_no_success == False:
        task_no_input = int(input('\nIf you would like to select a specific '
                                  'task, please enter the task number. '
                                  'Alternatively enter -1 to return to the '
                                  'main menu.\n: '))
        # Check if the task they want to select is one of their tasks.
        if task_no_input in task_no_for_user_list:
            task_no_success = True
            # If it is, find the index of that task in the list.
            task_no_input_index = task_no_list.index(task_no_input)
            # Ask the user if they want to mark the task as complete or edit
            # the task.
            # If user enters invalid entry, run while loop until valid entry.
            user_choice_success = False
            while user_choice_success == False:
                user_choice = input('''\nWould you like to:
'c' - Mark the task as complete
'e' - Edit the task
Please enter 'c' or 'e'.
: ''').lower()  # Convert the input to lower case.
                if user_choice == 'c':
                    # If the user wants to mark the task as complete, first 
                    # check if it isn't complete already.
                    user_choice_success = True
                    if completed_list[task_no_input_index] == 'Yes':
                        print(f'Task {task_no_input} is already complete. '
                            'Returning to the main menu.')
                    # If it's not complete yet, change the task to comlete.
                    else:
                        completed_list[task_no_input_index] = 'Yes'
                        print(f'Task {task_no_input} marked as complete.')

                elif user_choice == 'e':
                    user_choice_success = True
                    # If they want to edit the task, first check if the task
                    # isn't complete already.
                    if completed_list[task_no_input_index] == 'No':
                        # If not complete, give the user the option to edit
                        # the username or due date.
                        edit_choice_success = False
                        while edit_choice_success == False:
                            edit_choice = input('''\nWould you like to edit:
'u' - Username
'd' - Due date
Please enter 'u' or 'd'.
: ''').lower()  # Convert the input to lower case.
                            if edit_choice == 'u':
                                # If the user wants to edit the username, ask
                                # for new username and change it in the list.
                                edit_choice_success = True
                                new_username = input(f'Please enter a new '
                                                     f'username for task '
                                                     f'{task_no_input}: ')
                                username_list[task_no_input_index] = new_username
                                print(f'Task {task_no_input} username changed '
                                      f'to {new_username}.')

                            elif edit_choice == 'd':
                                # If the user wants to edit the due date, ask
                                # for new due date and change it in the list.
                                edit_choice_success = True
                                new_due_date = input(f'Please enter a new due '
                                                     f'date for task '
                                                     f'{task_no_input} (i.e. '
                                                     f'01 Jan 2000): ')
                                due_date_list[task_no_input_index] = new_due_date
                                print(f'Task {task_no_input} due date changed '
                                      f'to {new_due_date}.')

                            else:
                                # If user enters invalid entry, show 
                                # error message.
                                print('Invalid entry. Please try again.')

                    else:
                        # If the task is already complete, return message to
                        # say the task cannot be edited.
                        print('The task has already been completed and cannot'
                              ' be edited. Returning to the main menu.')

                else:
                    # If user enters invalid entry, show error message.
                    print('Invalid entry. Please try again.')

        elif task_no_input == -1:
            task_no_success = True
            # If user enters -1, return to main menu.
            print('Returning to the main menu.')

        else:
            # If the task number they choose is not one of their tasks,
            # show error message.
            print('Invalid entry. Please try again.')


    # Write the lists with the amended task info to the tasks.txt file.
    # Create index variable and assign value 0.
    index = 0
    # First, open the tasks file and write the first task to the file
    # using the write function and increase increae the index counter by 1.
    tasks_file = open('tasks.txt', 'w')

    tasks_file.write(f'{username_list[index]}, '
                     f'{task_title_list[index]}, '
                     f'{task_description_list[index]}, '
                     f'{date_assigned_list[index]}, '
                     f'{due_date_list[index]}, '
                     f'{completed_list[index]}')    
    index += 1

    tasks_file.close()


    # Secondly, open the tasks file and add the rest of the tasks to the 
    # file using the a while loop and append function .
    #
    # This second part with append function is used beacuse if only the first
    # part with write function only is used the .txt file will either begin or
    # end with a line break and that will cause the program to crash.
    tasks_file = open('tasks.txt', 'a')

    while index < len(task_no_list):
        tasks_file.write(f'\n{username_list[index]}, '
                         f'{task_title_list[index]}, '
                         f'{task_description_list[index]}, '
                         f'{date_assigned_list[index]}, '
                         f'{due_date_list[index]}, '
                         f'{completed_list[index]}')
        index += 1
      
    tasks_file.close()

def generate_reports():
    '''Define function to generate reports'''
    # Create variables to count certain task criteria and assign value 0.
    no_tasks = 0
    no_complete = 0
    no_incomplete = 0
    no_incomplete_overdue = 0

    ''' Open the tasks.txt file and read every line using for loop.
    Split the line where there is a comma and space and assign to
    respective variables depending on the type of data.'''
    
    tasks_file = open('tasks.txt', 'r')

    for line in tasks_file:
        username, task_title, task_description, \
        date_assigned, due_date, completed = line.split(', ')
        completed = completed.strip('\n')  # Remove line break.

        # Increase the task number count by 1.
        no_tasks += 1

        # If the task is complete, increase completed task number count by 1.
        if completed == 'Yes':
            no_complete += 1
        # If the task is incomplete, increase incomplete task number count
        # by 1.
        else:
            no_incomplete += 1

        # Parse due_date string into datetime.
        due_date = datetime.strptime(due_date, '%d %b %Y')
        # Find current date.
        current_date = datetime.today() # Get current date.
        # If the task is incomplete and task is overdue, increase task number 
        # count for no_incomplete_overdue variable.
        if completed == 'No' and due_date < current_date:
            no_incomplete_overdue += 1

    tasks_file.close()

    # Calculate the percentage of incomplete tasks.
    incomplete_percentage = round((no_incomplete / no_tasks) * 100, 2)
    # Calculate the percentage of overdue tasks.
    overdue_percentage = round((no_incomplete_overdue / no_incomplete) 
                                * 100, 2)

    # Write the task overview data to a text file in an easy to read manner.
    with open('task_overview.txt', 'w') as task_overview_file:
        task_overview_file.write(f'''\
Number of tasks:                            {no_tasks}
Number of completed tasks:                  {no_complete}
Number of incomplete tasks:                 {no_incomplete}
Number of incomplete and overdue tasks:     {no_incomplete_overdue}
Percentage of tasks that are incomplete:    {incomplete_percentage}%
Percentage of tasks that are overdue:       {overdue_percentage}%''')


    # Create new empty lists for usernames and passwords.
    username_list = []
    password_list = []

    # Open the file storing the usernames and passwords.
    user_file = open('user.txt', 'r')
    # Use for loop to read every line in the file.
    for line in user_file:
        # Split every line where there is a comma and space into username and
        # password and save into separate variables.
        username, password = line.split(', ')
        # Add username and password variables to the lists by using append 
        # function.
        username_list.append(username)
        password_list.append(password.strip('\n'))
    user_file.close()

    # Find number of users using len function.
    no_users = len(username_list)

    # Create the user_overview file.
    with open('user_overview.txt', 'w') as user_overview_file:
        # Write the number of users and tasks to the file.
        user_overview_file.write(f'''\
Total number of users:      {no_users}
Total number of tasks:      {no_tasks}''')
       
        # Use for loop to run through the list of usernames.
        for num in range(0, no_users):

            # Create variable to count various user task criteria and assign
            # value 0.
            user_tasks = 0
            user_tasks_complete = 0
            user_tasks_incomplete = 0
            user_tasks_overdue = 0

            '''Use for loop to run thrugh every task.
            Open the tasks.txt file and read every line using for loop.
            Split the line where there is a comma and space and assign to
            respective variables depending on the type of data.
            Use this for loop to loop through all the tasks'''
            with open('tasks.txt', 'r') as tasks_file:
                for line in tasks_file:
                    username, task_title, task_description, \
                    date_assigned, due_date, completed = line.split(', ')
                    completed = completed.strip('\n')  # Remove line break.

                    # If the username for the task is the same as the username
                    # in the username list, increase user_task count by 1.
                    if username_list[num] == username:
                        user_tasks += 1
                        # If the task is complete, increase completed tasks
                        # count for the user by 1.
                        if completed == 'Yes':
                            user_tasks_complete += 1
                        # If the task is incomplete, increase the incomplete
                        # task count for the user by 1.
                        elif completed == 'No':
                            user_tasks_incomplete += 1

                            # If the task is incomplete and overdue, increase
                            # the overdue task count for the user by 1. 
                            # Parse due_date string into datetime.
                            due_date = datetime.strptime(due_date, '%d %b %Y')
                            # Find current date.
                            current_date = datetime.today()
                            if due_date < current_date:
                                user_tasks_overdue += 1     
    
            # If the username has no tasks assigned to them, set the count
            # variables to 0.
            if user_tasks == 0:
                percentage_tasks = 0
                percentage_complete = 0
                percentage_incomplete = 0
                percentage_overdue = 0
            # If the username has tasks assigned to them, calculate various
            # percentages relating to task criteria.
            else:
                percentage_tasks = round((user_tasks / no_tasks) * 100, 2)
                percentage_complete = round((user_tasks_complete / user_tasks)
                                             * 100, 2)
                percentage_incomplete = round((user_tasks_incomplete
                                               / user_tasks)
                                               * 100, 2)
                percentage_overdue = round((user_tasks_overdue / user_tasks)
                                            * 100, 2)

            # Write the user overview data to the text file in an easy to read
            # manner.
            user_overview_file.write(f'''\n\n\
User:                                   {username_list[num]}
Number of tasks:                        {user_tasks}
Percentage of total tasks:              {percentage_tasks}%
Percentage of user tasks completed:     {percentage_complete}%
Percentage of user tasks incomplete:    {percentage_incomplete}%
Percentage of user tasks overdue:       {percentage_overdue}%''')

    print('Reports generated successfully.')


def display_statistics():
    '''Define function to display the statistics generated using the 
    generate_reports() function.

    If the reports have not been generated, first use the 
    generate_reports() function to generate the reports.
    '''
    # Use function to check if the task overview file exists.
    if Path('task_overview.txt').exists():
        # If it does exist, open the file as read the contents into the
        # new task_overview variable.
        with open('task_overview.txt', 'r') as task_overview_file:
            task_overview = task_overview_file.read()
    else:
        # If the file does not exist, generate the reports.
        generate_reports()
        # Open the file as read the contents into the new task_overview
        # variable.
        with open('task_overview.txt', 'r') as task_overview_file:
            task_overview = task_overview_file.read()

    # Open the user overview file and read the contents into the new 
    # user_overview variable.
    with open('user_overview.txt', 'r') as user_overview_file:
        user_overview = user_overview_file.read()

    # Print the contents of the task_overview and user_overview variables.
    print("\nTASK OVERVIEW:\n")
    print(task_overview)
    print("\nUSER OVERVIEW:\n")
    print(user_overview)


#====Login Section====


# Create new empty lists for usernames and passwords.
username_list = []
password_list = []

'''
Open the user.txt file.

Use for loop to read every line in the file.

Split every line where there is a comma and space into username and password
and save into separate variables.

Add username and password variables to the lists by using append function.

Close the user.txt file.
'''

user_file = open('user.txt', 'r')
for line in user_file:
    username, password = line.split(', ')
    username_list.append(username)
    password_list.append(password.strip('\n'))
user_file.close()


# Create new variable index and give value 0.
# Create login_success variable and set to False.

index = 0
login_success = False


'''
Use while loop to validate username and password.

While loop to keep running and ask for username and password for as long
as login_success is False.

Ask for user to input username and password and store in separate variables.
Use in function to check if the entered username is in username_list.

If it is, find the index of the username in the username_list.
The password for that username is saved under the same index within the
password_list.

If the username and password match, display appropriate message and set
login_success to True to end the while loop.

If username or password is not in the lists, display appropriate error
message and ask user to enter username and password again.
'''

while login_success == False:
    username_input = input('Username: ')
    password_input = input('Password: ')
    if username_input in username_list:
        index = username_list.index(username_input)
        if password_list[index] == password_input:
            print('Login successful.')
            login_success = True
        else:
            print('Invalid password. Please try again.\n')
    else:
        print('Invalid username. Please try again.\n')


#====Menu Section====

while True:
    '''
    Presenting the menu to the user and making sure that the user input is 
    coneverted to lower case.
    
    Provide two separate menu options using if statement, one for admin user 
    with an additional option, and another menu for all other users.
    '''

    if username_input == 'admin':
        menu = input('''\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
: ''').lower()

    else:
        menu = input('''\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    # Call reg_user() function to register a new user.
    if menu == 'r':
        reg_user()

    # Call add_task() function to add a new task to the tasks.txt file.
    elif menu == 'a':
        add_task()

    # Call view_all() function to display information for each task contained
    # in tasks.txt. 
    elif menu == 'va':
        view_all()

    # Call view_mine() function to display information for all tasks contained
    # in tasks.txt for the user that is currently logged in.
    elif menu == 'vm':
        view_mine()

    # Call generate_reports() function to generate task overview
    # and user overview reports. Only allow this input option for admin user.
    elif menu == 'gr' and username_input == 'admin':
        generate_reports()

    # Call display_statistics() function to display contents of task overview
    # and user overview reports. Only allow this input option for admin user.
    elif menu == 'ds' and username_input == 'admin':
        display_statistics()

    # Exit the program.
    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    # Error message if user inputs incorrect option.
    else:
        print("\nYou have made a wrong choice, please try again.")