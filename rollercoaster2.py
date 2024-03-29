# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:37:51 2024

@author: aisha
"""

print("Hello and Welcome to the Rollercoaster!!!")
height = int(input("What is your height in cm? " ))

if height >= 150:
    print("Hooray, you can ride the rollercoaster!")
    age = int(input("What is your age? " ))
    if age < 12 :
        print("Please pay $5.00")
    elif age <= 18: 
        print("Please pay $7.00")
    else: 
        print("Please pay $12.00")
else: 
        print("Sorry, you have to be a little taller to ride this rollercoaster.")