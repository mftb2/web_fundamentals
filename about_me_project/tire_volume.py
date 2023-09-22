# Car Tire Volume Calculator

print("Car tire calculator:")

import math

#Get user input
width = int(input("What is the width of the tire?"))
ratio = int(input("What is the aspect ratio of the tire?"))
diameter = int(input("What is the diameter of the tire?"))

#Calculate volume based on input
volume = str((math.pi * (width * width) * ratio * ((width * ratio) + (2540 * diameter)))/10000000000)

#Round volume to 2 decimals
rounded_volume = round(float(volume), 2)

print("The volume of the tire is " + str(rounded_volume) + ".")