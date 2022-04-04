#!/usr/bin/env python
# coding: utf-8

# # Computing 8 Assignment
# 

# ---
# ## Background
# 
# Object oriented programming languages are often used when designing and developing complex systems such as movement systems for a robot. In this assignment, you will be implementing a **Drone** class for a robot. Flying drones such as quadcopters are now commonplace with many consumers. Our class will help keep track of the properties of our drone, and its location in space. Specifically, we will track.
# 
# -	The drones’s name
# -	The drone's battery percentage
# -	The drones’s X coordinate in space
# -   The drone's Y coordinate in space
# -   The drone's altitude in space
# 
# Our movement system for our drone can be thought of as an infinitely large grid, where [0,0] is the respective **X** and **Y** coordinates of our drone in its starting position. Additionally, we also have a third dimension (**Z**) which is the altitude of the drone, which can be only 0 or greater. 
# 
# You will also be required to write a **function** that utilizes your **Drone** class, the details of which are provided in your Program Requirements below. 

# ---
# ## Program Requirements (12 Marks)
# 
# ### Requirements - Drone Class
# 
# The requirements for the **Drone** class are given below. Please ensure that your methods have the EXACT naming as specified! Failure to do so will result in lost marks.
# 
# ***Note: you must include a try and except statement in at least one method in your code.***
# 
# 1.	Create an **\_\_init\_\_**(*name*) method that takes the following arguments:
# 
#     ***name***: A *string* representing the name of the Drone. The variable is assigned to an instance variable. If *name* is an empty string, the instance variable is set to the string **"Default"**.
#     
#     The method also initializes the following instance variables:
#     
#     - An *int* representing the drones’s battery. The drones’s battery is initially set to **100**.  
#     - An *int* representing the drones’s X coordinate. The drones’s initial X coordinate is **0**.  
#     - An *int* representing the drones’s Y coordinate. The drones’s initial Y coordinate is **0**.
#     - A *string* representing the drones’s altitude in meters. The drones’s initial altitude coordinate is **0m**.
# 
# 
# 2.	Create the following **accessor** methods:
# 
#     -	**get_name**: Returns the Drones’s name.  
#     -	**get_X**: Returns the drone's X coordinate
#     -	**get_Y**: Returns the drone's Y coordinate 
#     -	**get_coords**: Returns the drone's X and Y coordinates in the list format: [X,Y]
#     -	**get_altitude**: Returns the drone's altitude
#     -	**get_charge**: Returns the drone's current battery life
#     
#     
# 3.	Create the **mutator** method *charge*()
#     -	**Method description**: The method does not return anything, but sets the drone's battery to **100**.
#     
#     
#     
# 4.	Create the **mutator** method **move_x**(*val*) 
#     -	***val***: An *int*.  
#     -	**Method description**: The method does not return anything, but moves the drone's X coordinate by **val**. **val** can be a positive or negative number. Note that this method moves the drone *relative* to it's current positon. If the drone's current X coordinate is **3**, moving the drone by +5 will set the new X coordinate to **8**.
#     - This method drains the drone's battery life by **5** as long as the battery life is > 0. Ensure the battery life does not become a negative value. If it does, set battery life to 0. (0 is the lowest allowable battery life).
#     - **IMPORANT**: If the drone's battery life begins at **0**, this method does not move the drone, and instead returns the following message:
#     <center>"Error - Please charge the drone"</center>
#     
#     
# 5.	Create the **mutator** method **move_y**(*val*) 
#     -	***val***: An *int*.  
#     -	**Method description**: The method does not return anything, but moves the drone's Y coordinate by **val**. **val** can be a positive or negative number. Note that this method moves the drone *relative* to it's current positon. If the drone's current Y coordinate is **-10**, moving the drone by -7 will set the new Y coordinate to **-17**.
#     - This method drains the drone's battery life by **5** as long as the battery life is > 0. Ensure the battery life does not become a negative value. If it does, set battery life to 0. (0 is the lowest allowable battery life).
#     - **IMPORANT**: If the drone's battery life begins at **0**, this method does not move the drone, and instead returns the following message:
#     <center>"Error - Please charge the drone"</center>
#     
#     
# 6.	Create the **mutator** method **fly_to**(*new_x*,*new_y*)
#     -	**Method description**: The method does not return anything, but instead **sets** the drone's X and Y coordinates to **new_x** and **new_y** respectively. **new_x** and **new_y** can be positive or negative numbers. This method overwrites the drone's current coordinates.
#     - This method also drains the drone's battery life by **10** as long as the battery life is > 0. Ensure the battery life does not become a negative value. If it does, set battery life to 0. (0 is the lowest allowable battery life).
#     - **IMPORANT**: If the drone's battery life is **0**, this method does not move the drone, and instead returns the following message:
#     <center>"Error - Please charge the drone"</center>
#     
# 7.	Create the **mutator** method **move_altitude**(*height*)
#     -   ***height***: An *int*.
#     -   **Method description**: The method adds or subtracts the current altitude of the drone by **height**, and returns the new altitude of the drone as a string. If the new altitude is **negative**, the method sets the drone's altitude to 0 instead.
#     - This method also drains the drone's battery life by **15** as long as the battery life is > 0. Ensure the battery life does not become a negative value. If it does, set battery life to 0. (0 is the lowest allowable battery life).
#     - **IMPORANT**: If the drone's battery life is **0**, this method does not move the drone, and instead returns the following message:
#     <center>"Error - Please charge the drone"</center>
#  
#  
# --- 
# ### Requirements -  Class Function
# You are also required, in a seperate cell, to create a **function** that will utilize your **Drone** class.
# 
# 1.	Define the function **evasive_maneuvers**(*drone1*,*e_x*,*e_y*)
#     -   **drone1**: A *Drone* object
#     -   ***e_x***: An *int*.
#     -   ***e_y***: An *int*.
#     -   **Function description**: This function makes the drone perform an evasive maneuver, which consists of **5 movements**. For each of the **5 movements**, the X, Y, and altitude values follow the values below:
#     
#         - The X coordinate of the drone oscillates between having *e_x* added to it, and then subtracted from it **5 times**. For example, if the initial X coordinate of the drone was 3, and *e_x* was 4, the 5 X coordinate movements would be: <u>7, 3, 7, 3, 7</u>
#          - The Y coordinate of the drone has *e_y* continuously subtracted from it **5 times**. For example, if the initial Y coordinate of the drone was 10, and *e_y* was 5, the 5 Y coordinate movements would be: <u>10, 5, 0, -5, -10</u>
#          - The function should return all sets of X and Y coordinates as a **list of lists** . For example:
#          [[7,10], [3,5], [7,0], [3,-5], [7,-10]] 
#          - This function  drains the drone's battery severly by setting it to **1**.
#          - **IMPORANT**: If the drone's battery life is **0**, this function does not move the drone, and instead returns the following message:
#     <center>"Error - Please charge the drone"</center>
#          

# ---
# ## Implementation
# Please define the Drone class in the cell below.

# In[11]:


#********************************************
# Write your class definition and __init__ function below: (1.5 marks)
#********************************************

class Drone:
    def __init__(self, name):
        #Set name to new object, set name to Default if empty string entered
        if name == '':
            self.name = 'Default'
        else:
            self.name = name
        
        #Initialize battery, position, and altitude of every drone created
        self.battery = 100
        self.x_pos = 0
        self.y_pos = 0
        self.altitude = '0m'

#********************************************
# Write your accessor methods below: (0.25 marks each)
#********************************************
    #Accessor Methods: Return a certain value
    def get_name(self):
        return self.name
    
    def get_X(self):
        return self.x_pos
    
    def get_Y(self):
        return self.y_pos
    
    def get_coords(self):
        return [self.x_pos, self.y_pos]
    
    def get_altitude(self):
        return (self.altitude)
    
    def get_charge(self):
        return self.battery

#********************************************
# Write all mutator methods below: (1.5 marks each)
#********************************************

    #Mutator Method
    def charge(self):
        #Set battery to 100
        self.battery = 100
        
    def move_x(self, val):
        #If the charge ever reaches 0 prior to any manuever, exit the function with error statement
        if self.battery == 0:
            return "Error - Please charge the drone"
        
        #Adjust x-position by the amount of val
        self.x_pos += val
        
        #Decrease battery by 5 for everytime the x-position changes
        self.battery -= 5
        #Set battery to 0 if battery is less than 0 
        if self.battery < 0:
            self.battery = 0
            
        
    def move_y(self, val):
        #If the charge ever reaches 0 prior to any manuever, exit the function with error statement
        if self.battery == 0:
            return "Error - Please charge the drone"
        
        #Adjust y-position by the amount of val
        self.y_pos += val
        
        #Decrease battery by 5 for everytime the y-position changes
        self.battery -= 5
        #Set battery to 0 if battery is less than 0 
        if self.battery < 0:
            self.battery = 0
            
    def fly_to(self,new_x,new_y):
        #If the charge ever reaches 0 prior to any manuever, exit the function with error statement
        if self.battery == 0:
            return "Error - Please charge the drone"
        
        #Change current x and y positions to new x and y positions specified by input
        self.x_pos = new_x
        self.y_pos = new_y
        
        #Decrease battery by 10 for everytime the position changes
        self.battery -= 10
        #Set battery to 0 if battery is less than 0 
        if self.battery < 0:
            self.battery = 0
            
    def move_altitude(self, height):
        #If the charge ever reaches 0 prior to any manuever, exit the function with error statement
        if self.battery == 0:
            return "Error - Please charge the drone"
        
        #Try to adjust the altitude
        try:
            #Convert the integer portion of the altitude by omitting 'm'
            #Add height to current altitude value, and set within a new variable
            new_altitude = int(self.altitude[:-1]) + height
        except:
            #Print error statement and Return None value, as an error has occured
            print('An error has occured with changing the altitude.')
            return None
         
        #Ensure that the new altitude does not go below 0m
        if new_altitude < 0:
            self.altitude = '0m'
        else:
            #Change the current object altitude to the new altitude
            #Convert int to string, and add meters unit
            self.altitude = str(new_altitude) + 'm'
        
        #Decrease battery by 10 for everytime the position changes
        self.battery -= 15
        #Set battery to 0 if battery is less than 0 
        if self.battery < 0:
            self.battery = 0
            
        return self.altitude


# Please define the evasive maneuvers function in the cell below:

# In[12]:


#********************************************
# Write your evasive_maneuvers function below: (1.5 marks)
#********************************************
def evasive_maneuvers(drone1,e_x,e_y):
    #If the charge ever reaches 0 prior to any manuever, exit the function with error statement
    if drone1.battery == 0:
        return "Error - Please charge the drone"
    
    #Create an empty list to store previous movements
    coordinates_history = []
   
    #Repeat 5 times
    for i in range(5):
        #Alternate how e_x changes the x-position of the drone
        drone1.x_pos += ((-1)**i)*e_x
        #Decrease y-postion by set amount
        drone1.y_pos -= e_y
        
        #Create a list for the current coordinates, and add it to the history list
        coordinates = [drone1.x_pos, drone1.y_pos]
        coordinates_history.append(coordinates)
    
    #Change battery to 1, and return history variable
    drone1.battery = 1
    return coordinates_history
    


# ---
# ## Testing
# 
# The cell below contains a main function that you can use to test your functions. 
# 
# ### Important 
# Run the cell where you implemented your functions first and ensure it raises no errors. Then, run the cell below with the main function to verify that your code works correctly. The following output should be seen:
# 
# <code>
# ----TESTING CREATION----
# Drone created with name: QDrone, Coordinates: [0, 0], Altitude: 0m, and Battery life 100
# </code>
# <code>
# ----TESTING MOVEMENT----
# X movement by 7 units, Y movement by -13 units. New Coordinates: [7, -13]
# Drone elevated, now at a height of: 43m
# Current battery life: 75
# </code>
# <code>
# ----TESTING MOVEMENT----
# Drone movement. New Coordinates: [314, -201]
# Emergency Landing. Now at a height of: 0m
# Current battery life: 50
# </code>
# <code>
# ----RECHARGING AND TAKEOFF----
# Drone Recharged: 100
# Takeoff! Now at a height of: 20m - Coordinates: [314, -201]
# </code>
# <code>
# ----EVASIVE MANEUVERS ----
# [[324, -181], [314, -161], [324, -141], [314, -121], [324, -101]]
# Current Battery Life: 1
# </code>
# <code>
# ----LOW BATTERY MOVEMENTS ----
# Drone movement to home. New Coordinates: [0, 0]
# Attempting movement on emergency battery...
# Error - Please charge the drone
# Error - Please charge the drone
# Error - Please charge the drone
# Error - Please charge the drone
# Final Test: Error - Please charge the drone
# </code>
# Note that your code is not necessarily correct if your output matches the expected output. Your code will be checked against multiple inputs for correctness. The cell below is not graded, so feel free to modify the code as you wish!

# In[13]:


print("----TESTING CREATION----")
d1 = Drone("QDrone")
d1_name,d1_coords,d1_height,d1.battery = d1.get_name(),d1.get_coords(),d1.get_altitude(),d1.get_charge()

print(f"Drone created with name: {d1_name}, Coordinates: {d1_coords}, Altitude: {d1_height}, and Battery life {d1.battery}")

print("\n----TESTING MOVEMENT----")
d1.move_x(7)
d1.move_y(-13)
d1.move_altitude(43)
print(f"X movement by 7 units, Y movement by -13 units. New Coordinates: {d1.get_coords()}")
print(f"Drone elevated, now at a height of: {d1.get_altitude()}")
print(f"Current battery life: {d1.get_charge()}")

print("\n----TESTING MOVEMENT----")
d1.fly_to(314,-201)
d1.move_altitude(-100)
print(f"Drone movement. New Coordinates: {d1.get_coords()}")
print(f"Emergency Landing. Now at a height of: {d1.get_altitude()}")
print(f"Current battery life: {d1.get_charge()}")

print("\n----RECHARGING AND TAKEOFF----")
d1.charge()
print(f"Drone Recharged: {d1.get_charge()}")
d1.move_altitude(20)
print(f"Takeoff! Now at a height of: {d1.get_altitude()} - Coordinates: {d1.get_coords()}")

print("\n----EVASIVE MANEUVERS ----")
print(evasive_maneuvers(d1,10,-20))
print(f"Current Battery Life: {d1.get_charge()}")

print("\n----LOW BATTERY MOVEMENTS ----")
d1.fly_to(0,0)
print(f"Drone movement to home. New Coordinates: {d1.get_coords()}")
print(f"Attempting movement on emergency battery...")
print(d1.fly_to(10,20))
print(d1.move_x(10))
print(d1.move_y(10))
print(d1.move_altitude(10))
print("Final Test:", evasive_maneuvers(d1,20,20))

# ---
# ## Test Plan (6 Marks)
# Develop a test plan for your program. Your test plan should have at least three test cases: one normal case, one boundary case, and one abnormal case. You can test any function but you must test **at least two different** functions. Please use the following format for your test cases:
# 
# **Function:**   
# **Input:**  
# **Output:**  
# **Excepted Output:**  
# **Pass/Fail:**  
# 
# An example test case is shown below:  
# ```
# Function: fly_to(self,new_x,new_y)
# Input: d = Drone("QDrone")
#        d.fly_to(10,20)
#        print(d.get_coords() == [10,20])
# Excpected Output: True
# Output: True
# Pass/Fail: Pass
# ```
# 
# Implement your testing plan in the cell below! 

# ```
# Function #1: move_x(self, val)
# 
# Normal Case:
# Function: move_x(self, val):
# Input: d = Drone("QDrone")
#        d.move_x(5)
#        print(d.get_X())
# Excpected Output: 5
# Output: 5
# Pass/Fail: Pass
# 
# Boundary Case:
# Function: move_x(self, val):
# Input: d = Drone("QDrone")
#        d.battery = 4
#        d.move_x(5)
#        print(d.get_X())
#        print(d.get_charge())
# Excpected Output: 5
#                   0
# Output: 5
#         0
# Pass/Fail: Pass
# 
# 
# Abnormal Case:
# Function: move_x(self, val):
# Input: d = Drone("QDrone")
#        d.move_x('')
# Excpected Output: TypeError
# Output: TypeError
# Pass/Fail: Pass
# 
# 
# 
# Function #2: move_altitude(self, height):
# 
# #Normal Case:
# Function: move_altitude(self, height)
# Input: d = Drone("QDrone")
#        d.move_altitude(5)
#        print(d.get_altitude())
# Excpected Output: '5m'
# Output: '5m'
# Pass/Fail: Pass
# 
# #Boundary Case:
# Function: move_altitude(self, height)
# Input: d = Drone("QDrone")
#        d.move_altitude(-1)
#        print(d.get_altitude())
# Excpected Output: '0m'
# Output: '0m'
# Pass/Fail: Pass
# 
# #Abnormal Case:
# Function: move_altitude(self, height)
# Input: d = Drone("QDrone")
#        d.move_altitude('')
# Excpected Output: 'An error has occured with changing the altitude'
#                   'Remember: Input has to be an integer!'
# Output: 'An error has occured with changing the altitude'
#         'Remember: Input has to be an integer!'
# Pass/Fail: Pass
# 
# ```
