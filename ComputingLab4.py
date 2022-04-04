#!/usr/bin/env python
# coding: utf-8

# # Computing 4 Assignment
# 

# ---
# ## Background
# 
# You are a part of a team that is responsible for maintaining the quality of an app (which may or may not involve slicing fruit mid-air). Your team has prepared an update for improving app graphics, where 4 update versions are available for different users.
# 
# **You are responsible for implementing a system to determine which app update will be installed on various devices depending on their device operating system and time of last app update on their device.**
#  
# 
# Your system will be provided with a list of user's information, following the following format: 
# 
# <br>
# \begin{align}
#   \texttt{[‘serialNum’, ‘OS Type’, ‘OS Version’, 'Update Date']}\tag{1}
# \end{align}
# <br>
# 
# Each entry in the sub-list is explained below:
# 
# |   |   |
# |---|:--|
# |**serialNum** |A string with length 8 that represents the smartphone's serial number.   |
# |**OS Type**   |A string representing operating system type with the value iOS or Android.  |
# |**OS Version**|A string representing operating system version.  |
# |**Update Date**|A string representing the latest app update date on that device (YYYY-MM-DD)   |
# 
# 
# 
# The following list of lists provides an example of data used by your system. Each sub-list follows the format given in (1). There are 3 devices in this example:
# 
# ```
# devices = [
# ['BX001321','iOS', '12.0' ,'2019-01-03'],
# ['GX021629','Android', '11.0', '2019-08-06'],
# ['BX101129','iOS', '8.0', '2019-05-22']]
# ```
# 
# <br>
# 
# The update consideres two operating systems: MAC **iOS** or **ANDROID** OS. There are 4 different app updates available, and are compatible with different devices depending on the **OS Type**, **OS Version**, and **Update Date**. The following table depicts this set of criteria for each update version:
# 
# \begin{align}
#   \texttt{Table 1: Criteria to determine app update version}
# \end{align}
# 
# 
# | OS Type |  OS Version | App Update Criteria  | App Update Version| 
# |---|:--|:--|---|
# | **iOS**  | - Version 8.0 or higher  | - At any date of last update | Version 1   |
# | **iOS**  | - Version less than 8.0  | - At any date of last update | No Update   |
# | **Android**  | - Version 10.0 or higher  | - At any date of last update | Version 2   |
# | **Android**  | - Version 8.0 to 10.0 (not including 10.0)  | - Last update between **January** and **June** | Version 3  |
# | **Android**  | - Version 8.0 to 10.0 (not including 10.0)  | - Last update between **July** and **December** | Version 4  |
# | **Android**  | - Version less than 8.0  | - At any date of last update | No Update   |
# 
# 
# <br>
# 
# Given this information, your task is to generate a list of devices and their update version required. The steps in the requirements section will help you achieve this task.

# ---
# ## Program Requirements (12 marks)
# The requirements of the program are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks. 
# 
# 1. Define a function **update_required**(*device_info*):
#   - ***device_info***: A *list* containing device and app information in the form of (1).
#       
#       \begin{align}
#   \texttt{[‘serialNum’, ‘OS Type’, ‘OS Version’, 'Update Date']}\tag{1}
# \end{align}
# 
#    - Begin by defining the OS Version as a local variable in the form of a float (you can copy and paste this line into your function):      
#          OSVersion = float(device_info[2])
#    - Using a conditional statement, determine if the device requires an update or not (You only need the OS Version to do this!) 
#    - **Return**: A *Boolean* denoting whether an update is required or not, given the criteria in Table 1. (True if the device met the criteria to require an update, otherwise false)
# 
# 
# 2. Define a function **determine_update**(*device_info*):
#   - ***device_info***: A *list* containing device and app information in the form of (1). 
#   - Begin by defining local variables needed for comparisson (you can copy and paste these lines into your function): 
#          update_req = update_required(device_info) # a boolean representing if an update is required
#          OSType = device_info[1]
#          OSVersion = float(device_info[2])
#          month = int((device_info[3]).split('-')[1]) # Split the date by -, take the middle element, convert to int
# 
#    - This function should compare the local variables through multiple nested conditionals to determine which update version is required.
#    - **Return**: A *string* indicating which update version is required. These **MUST** be typed exactly as seen in column four (App Update Version) of Table 1.
#    
# 
# 3. Define a function **determine_device_update**(devices):
#   - ***devices***: A *list of lists* containing the information of all devices, where each entry is in the form of (1).
#   - Begin by defining an empty list that will hold the serial number and version number for devices with an app that requires an update
#   - Define a for-loop that iterates through each sub-list in the list ***devices***. Each sub-list represents a device's information in the form of (1).  
#   - Within the for-loop, use conditional statement(s) to determine:
#         - If the app on that device needs an update: create a list in the format: ['Serial Number' , 'Update Version']. Then append this list to the list you previously defined within this function. 
#         - If the app on that device does not need an update: skip that device *(such that this device will not be included in the final list of devices and their required update version)*
#   - **Return**: A *list of lists* of serial numbers and update versions (both as strings) of only the devices that require an app update.  

# ---
# ## Implementation
# Please define all functions in the cell below

# In[2]:


#********************************************
# Write your update_required function below: (4 marks)
#********************************************

def update_required(device_info):
    OSVersion = float(device_info[2])
    if OSVersion >= 8.0:
        return True
    elif OSVersion < 8.0:
        return False

#********************************************
# Write your determine_update function below: (4 marks)
#********************************************

def determine_update(device_info):
    update_req = update_required(device_info) # a boolean representing if an update is required
    OSType = device_info[1]
    OSVersion = float(device_info[2])
    month = int((device_info[3]).split('-')[1]) # Split the date by -, take the middle element, convert to int
    
    #iOS
    if OSType == 'iOS':
        if update_req == True:
            return "Version 1"
        else:
            return "No Update"
        
    #Android    
    elif OSType == 'Android':
        #V=10.0
        if OSVersion >= 10.0:
            return "Version 2"
        #V=8.0-10.0
        elif OSVersion >= 8.0:
            if (1 <= month <= 6):
                return "Version 3"
            elif (7 <= month <= 12):
                return "Version 4"
        #V= <8.0    
        elif OSVersion < 8.0:
            return "No Update"

#********************************************
# Write your determine_device_update function below: (4 marks)
#********************************************

def determine_device_update(devices):
    serial_number_list = []
    
    for i in range(len(devices)):
        if determine_update(devices[i]) != ("No Update"):
            number_list = [devices[i][0], determine_update(devices[i])]
            serial_number_list.append(number_list)
    return serial_number_list


# ---
# ## Testing
# 
# The cell below contains a main function that you can use to test your functions. 
# 
# ### Important 
# Run the cell where you implemented your functions first and ensure it raises no errors. Then, run the cell below with the main function to verify that your code works correctly with the provided input. The following message should be printed after the main() function above is run:
# 
# >[['GX010365', 'Version 1'], ['BX041085', 'Version 2'], ['GX031153', 'Version 3'], ['BX601829', 'Version 1'], ['BX481436', 'Version 1'], ['GX301320', 'Version 4']]
# 
# Note that your code is not necessarily correct if your output matches the expected output. Your code will be checked against multiple inputs for correctness. The cell below is not graded, so feel free to modify the code as you wish!
# 

# In[3]:


# TESTING
def main():
    devices = [['GX010365', 'iOS', '8.1', '2019-04-10'], #Version 1
              ['BX041085', 'Android', '12.0', '2019-09-13'], #Version 2
              ['BX031112', 'Android', '5.0', '2019-02-13'], #No Update
              ['BX210529', 'iOS', '7.0', '2019-11-15'], #No Update
              ['GX031153', 'Android', '9.0', '2019-04-11'], #Version 3
              ['BX601829', 'iOS', '9.0', '2019-04-28'], #Version 1
              ['BX481436', 'iOS', '10.1', '2019-01-10'], #Version 1
              ['GX301320', 'Android', '9.0', '2019-07-13']] #Version 4
    device_updates = determine_device_update(devices)
    print(device_updates)
main()


