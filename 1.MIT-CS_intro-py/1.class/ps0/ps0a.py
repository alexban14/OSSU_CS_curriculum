# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:14:16 2022
@author: banco
"""

# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”
import math

x = int(input('Enter a number:'))
y = int(input('Eneter another number:'))

power = x**y
logBase2 = math.log(x,2)
print(power, logBase2)