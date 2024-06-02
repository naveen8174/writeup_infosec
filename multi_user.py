import os
import pandas as pd
import getpass
#for adding an user to this file.
def adduser():
    username = input("Enter username: ")
    try:
        # making sure that password is a 4 digit password.
        password = input("Enter 4 digit numeric password: ")
        if len(password) == 4 and password.isdigit():
            new_user = pd.DataFrame({"username": [username], "passwords": [int(password)]})
            new_user.to_csv("password.csv", mode="a", index=False, header=False)
            print(f"User '{username}' added successfully.")
        else:
            print("Password must be a 4 digit number.")
    except ValueError:
        print("Enter numbers only")
#for deleting the user for file
def deluser():
    username = input("Enter username: ")
    #defining the pswd_df for usage.
    global pswd_df
    if username in pswd_df["username"].values:
        pswd_df = pswd_df[pswd_df["username"] != username]
        pswd_df.to_csv("password.csv", index=False)
        print(f"User '{username}' deleted successfully.")
    else:
        print("Username not found")

# Check if password.csv exists and load or create the DataFrame
if os.path.exists("password.csv"):
    pswd_df = pd.read_csv("password.csv")
#if not exist create thefile with arbitary user u1,u2,u3, with passwords 1111,2222,3333.
else:
    cred = {"username": ["u1", "u2", "u3"], "passwords": [1111, 2222, 3333]}
    pswd_df = pd.DataFrame(cred)
    pswd_df.to_csv("password.csv", index=False)
print(" you may enter as a user u1 with password 1111")

username = input("Enter username: ")
if username in pswd_df['username'].values:
    #password is hidden while entering.
    passwd = int(getpass.getpass(f"Enter password of {username}: "))
    user_row = pswd_df[pswd_df['username'] == username]
    #if credentials matcches properly.
    if not user_row.empty and user_row.iloc[0]['passwords'] == passwd:
        print(f"Hello, {username}, let's start!!\n")
        print("1. Add user\n2. Delete user\nOther. go to to-do list")
        user_choice = input("Choose: ")
        #adding user
        if user_choice == '1':
            adduser()
        #deleting user
        elif user_choice == '2':
            deluser()
        #updating the password.csv file.
        pswd_df = pd.read_csv("password.csv")
        task = {"task": [], "status": []}
        if os.path.exists("todo-list.csv"):
            task_df = pd.read_csv("todo-list.csv")
            task["task"] = task_df["task"].tolist()
            task["status"] = task_df["status"].tolist()
        else:
            print("Hurray!! No tasks for now!!!")

        print("1. Enter the task\n2. Print the tasks\n3. Mark the task as completed\n4. Save the file\n5. Exit\nOther. Exit")
        while True:
            opt = input("Enter the option: ")

            if opt == '1':
                task1 = input("Enter the new task: ")
                task["task"].append(task1)
                task["status"].append("no")
            elif opt == '2':
                printtask = pd.DataFrame(task)
                print(printtask)
            elif opt == '3':
                taskc = input("Enter the completed task: ")
                if taskc in task["task"]:
                    ind = task["task"].index(taskc)
                    task["status"][ind] = 'yes'
                else:
                    print("Task not found")
            elif opt == '4':
                printtask = pd.DataFrame(task)
                printtask.to_csv("todo-list.csv", index=False)
                location = os.getcwd()
                path = os.path.join(location, "todo-list.csv")
                print(f"File saved successfully at: {path}")
            elif opt == '5':
                break
            else:
                print("Enter a valid input")
    else:
        print("Invalid password")
else:
    print("Invalid username")
