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
        return False
    else:
        password_index = get_user_data(filename)[0].index(username)
        if get_user_data(filename)[1][password_index] == password:
            return True
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


# The main function above utilizes the functions you have created to simulate the login system environment. Inspect the code and play around with the funtionality to test out all of your functions. A file has already been created for you called "database.txt". This file contains one user with the following credentials:
# 
# Username: iLoveMac
# Password: iamthebeststudent123
# 
# Use the credentials to log into the system or create your own using the main function!

# ----------
# ## Code Legibility (6 Marks)
# Your code will be marked on commenting and code legibility.<br>
# The mark breakdown is as follows:<br>
# 
# >- 2 marks for using **appropriate variable names** that indicate what is being stored in that variable<br>
# >- 2 marks for leaving **comments on major parts of your code** such as where you read the file or calculate a summation<br>
# >- 2 marks for **general legibility**. The TA's should be able to understand your code without spending hours reading it. For example do not put your code in one very long line as this is hard for someone else reading your code to understand

# ---
# ## Reflective Questions (6 Marks)
# 
# 1. The **create_user** function requires that filename is opened in append mode in order to add a username/password combinations to filename. What will happen if filename is instead opened in write mode? Assume you are forced to use any access mode other append. Is it possible to re-write the function such that the functionality does not change? Please explain.
# 
# 
# 2. Assume you have to write a function **valid_length** that would check if the *username* and *password* are greater than 6 characters. How would you implement this function?
# 
# 
# 3. Assume you have two functions **encrypt(password)** and **decrypt(encoded_password)**. The function **encrypt** takes a password string and returns an encoded version of the password as a string. The function **decrypt** decodes  the encoded_password string and returns the decoded password as a string. Where would you use these functions in your code if you wanted your login system to store encoded user passwords rather than raw text passwords?
# 
# Please answer all questions in the cell below!

# ```
# 1.) If the file is opened in write mode, the will be resetted. That would mean all information that is currently on the file will be erased. This would delete all current usernames and passwords currently stored, essentially causing a massive issue for the user. If I were to use any other mode, I would utilize the read and write mode. Essentially, I would read the information from the current file, store it in a variable, and put it in a new file with the same name as the original. I would delete the original file, then using the write mode, create a new file for the updated information.
# 
# 2.) I would implement this function by using a for loop that would count the amount of characters in each string. If that number exceeds 6, I would break the loop and return True. Else, I would return False, indicating the string is not a minimum of 6 characters long.
# 
# 3.) I would use the encrypt() function when creating the password. This encrypted password will be stored in the file. I would then use the decryprt() function in the login() function and the get_user_data() function. These 2 functions ask for the password, so it would be necessary to decrypt those password for any type of data manipulation (such as loging in).
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 5 dropbox on avenue with the naming convention: macID_CL5.py
# 
# #### NOTE: YOU WILL BE MARKED ON MULTIPLE ITEMS IN THIS LAB IN ADDITION TO THE FUNCTIONALITY OF YOUR CODE
#  - Variable Names
#  - Commenting
#  - General Legibility
#  - Reflective Questions
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely receive zero.**
# 
# This assignment is due the day after your Lab A section at 11:59 PM EST
# 
# Late labs will not be accepted
