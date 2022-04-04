#!/usr/bin/env python
# coding: utf-8

# # Computing 5 Assignment
# 
# 

# ---
# ## Background
# 
# In this assignment you will be implementing a set of functions used in conjunction to form a website login system. Your system will utilize a text file for storing, retrieving, and verifying user credentials. We identify users based on their **username** and **password**. For simplicity we assume that usernames and passwords only contain alphanumeric characters. Alphanumeric characters represent the numbers **0-9** and the letters **A-Z** (both uppercase and lowercase). Usernames and passwords are case sensitive and must contain **at least 6** characters. Usernames must be unique.
# 
# Each username and password combination will be stored on its own line in the text file. Each line in the text file has the following format:
# 
# 
# <br>
# \begin{align}
#   \texttt{username\tpassword\n}\tag{1}
# \end{align}
# <br>
# 
# More explicitly, each line in the text file will contain a user’s username, a tab character, and that user’s password followed by the newline character. Please note that when opening the text file for viewing you will not explicitly see the **\t** and **\n** characters.
# 
# 
# In your implementation, usernames and passwords will be stored as plain text. This means that all usernames and passwords can easily be compromised if access to the text file is provided. This is extremely dangerous in the real world and poses huge security issues. In practicality, passwords are encrypted before stored so that they are not easily identifiable in the event of a data breach. Thus, please do not use any real passwords when developing and testing your program. 
# 

# ---
# ## Program Requirements (12 Marks)
# 
# Your task is to implement a set of functions that will be used in conjunction to form a website login system. Your system will read and write user credentials from a text file that emulates a database. The requirements of the system are given below. 
# Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks. You can choose to copy and paste the function names into the implementation cell to avoid spelling mistakes.
# 
# 
# 1. Define a function **get_user_data**(*filename*):
#   - ***filename***: A *string* representing the name of the text file (ex. “database.txt”) that stores user login credentials in the form of ```username\tpassword\n```.
#   - **Function Description**: The function performs the following actions as defined by the pseudocode below:
#     - Opens a file with the name *filename* for reading.
#     - Initializes two empty lists: **usernames**, and **passwords**
#     - For each line in file:
#         - Strips the line of the newline character "\n" using strip() and then splits it at the tab "\t" character using split(). 
#         - Extracts the username and password in each line. 
#         - The username is appended as a string to **usernames** and the password is appended as a string to **passwords**. 
#     - Closes the file with the name *filename*<br>*(Note that it is assumed that the file associated with filename exists before the function is called)*    
#   - **Return**: A *list of lists* of length 2 where the first list is the **usernames** list and the second list is the **passwords** list populated with the data from *filename* as described above. <br>
# 
# 
# 2. Define a function **exists**(*username*, *username_list*):
#   - ***username***: A *string* representing a username.
#   - ***username_list***: A *list* containing all usernames from *filename*.
#   - **Return**: *True* if *username* exists in *username_list*, otherwise *False*.<br>*(Hint: Use the **in** keyword.)*
# 
# 
# 3. Define a function **create_user**(*username*, *password*, *username_list*, *filename*):
#   - ***username***: A *string* representing a username.
#   - ***password***: A *string* representing a password.
#   - ***username_list***: A *list* containing all usernames from *filename*.
#   - ***filename***: A *string* representing the name of the text file (ex. “database.txt”) that stores user login credentials in the form of ```username\tpassword\n```.
#   - **Function Description**: The function performs the following actions:
#     - If *username* **does not** exist in *filename*, open *filename* in append mode, write the username and password in the form ```username\tpassword\n```, and close the file.
#     - If *username* **does** exist in *filename*, do nothing.
#   - **Return**: *True* if *username* and *password* were added to *filename*, otherwise *False*<br>*(Hint: Use your **exists** function to check if the username exists in username_list and remember to close your file if you open it.)*
# 
# 
# 4. Define a function **login**(*username*, *password*, *filename*):
#   - ***username***: A *string* representing a username.
#   - ***password***: A *string* representing a password.
#   - ***filename***: A *string* representing the name of the text file
#   - **Function Description**: The function performs the following actions:
#     - If *username* **does** exist in *filename*, find the password associated with *username* in *filename* using the index of the *username* and check if *password* is equal to the expected password.<br> *(Hint: Use your **get_user_data** and **exists** functions and the **index()** method.)*
#     - If the username **does not** exist in *filename*, do nothing.
#   - **Return**: *True* if *password* matches the password associated with *username* in *filename*. *False* if the passwords do not match or *username* does not exist in *filename*.

# ---
# ## Implementation
# Please define all functions in the cell below

# In[ ]:


#********************************************
# Write your get_user_data function below: (2.5 marks)
#********************************************

def get_user_data(filename):
    #Create a list for the usernames and password
    usernames = []
    passwords = []
    #Creare a combined list to return
    username_password_list = []
    #Open file, and save info in a variable
    with open(filename) as my_file:
        lines = my_file.readlines()

    for i in lines:
        #For each line, strip '\n', split the new string, and take the first element, which is the username
        usernames.append(i.strip('\n').split()[0])
        #For each line, strip '\n', split the new string, and take the second element, which is the password
        passwords.append(i.strip('\n').split()[1])
    #Append the usernames and passwords to combined list, and return the list
    username_password_list.append(usernames)
    username_password_list.append(passwords)
    return username_password_list

#********************************************
# Write your exists function below: (2.5 marks)
#********************************************

def exists(username, username_list):
    #If the username is in the list, return True
    if username in username_list:
        return True
    else:
        return False

#********************************************
# Write your create_user function below: (2.5 marks)
#********************************************

def create_user(username, password, username_list, filename):
    if exists(username, get_user_data(filename)[0]) == True:
        return False
    else:
        with open(filename, 'a') as my_file:
            my_file.write(username+'\t'+password+'\n')
        return True

#********************************************
# Write your login function below: (4.5 marks)
#********************************************

def login(username, password, filename):
    if exists(username, get_user_data(filename)[0]) == True:
        
        password_index = get_user_data(filename)[0].index(username)
        if get_user_data(filename)[1][password_index] == password:
            return True
        else:
            return False
    else:
        return False


# ---
# ## Testing
# 
# The cell below contains a main function that you can use to test your functions. 
# 
# ### Important
# Run the cell where you implemented your functions ***first*** and ensure it outputs with no errors. Then, run the cell below with the main function to verify that your code works correctly with the provided input.
# 

# In[1]:


# TESTING
def main():

    database = "database.txt"
    while True:
        ans = input("Press [q] to quit, [l] to login, [c] to create an account: ")
        if ans == "q":
            # Break if the user quits
            break
        elif ans == "l":
            # Login if the user types in "l"
            uname = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if login(uname, password, database):
                print("Login successful!\n")
            else:
                print("Sorry, login unsuccessful :(\n")
        elif ans == "c":
            # Create an account if the user types in c
            uname = input("Please create a username: ")
            password = input("Please create a password: ")
            # Check if username exists
            username_list = get_user_data(database)[0]
            if create_user(uname, password, username_list, database):
                    print("Account creation successful for user,",uname,"\n")
            else:
                    print("Sorry,",uname,"is already taken!\n")
        else:
            print("Please enter a valid character")
main()

