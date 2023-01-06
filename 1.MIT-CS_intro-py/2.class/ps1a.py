# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:44:55 2022
@author: banco
"""

total_cost = int(input('You want to buy a house. How much does it costs? :'))
down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
# savings = current_savings*r/12
annual_salary = int(input('Enter your salary:'))
precentToSave = float(input('Enter the precent you will save from your salary each month in decimal: '))
# portion_saved =precentToSave*(annual_salary/12)

monthsToWait = 0

while (down_payment > 0):
    monthsToWait += 1
    current_savings += precentToSave*(annual_salary/12)
    current_savings *(r/12)
    down_payment -= current_savings
print(monthsToWait)