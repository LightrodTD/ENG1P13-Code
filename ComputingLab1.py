import math
import random

g = 9.81

theta = (random.random()) * 45

theta_rad = math.radians(theta)

distance = float(input("Please enter the distance to our target zombie(as a float): "))

def velocity(d, angle_rad):
    numerator = g*d
    denominator = math.sin(2*angle_rad)
    v = math.sqrt(numerator/denominator)
    return v

print("Ready for launch!")
print("Set angle to", theta, "degrees")
print("Set speed to",velocity(distance,theta_rad),"m/s")
