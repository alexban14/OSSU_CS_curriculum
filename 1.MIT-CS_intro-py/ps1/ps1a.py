# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:44:55 2022
@author: banco
"""

annual_salary = int(input('Enter your salary:'))
portion_saved = float(input('Enter the precent you will save from your salary each month in decimal: '))
total_cost = int(input('You want to buy a house. How much does it costs? :'))
down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04

monthsToWait = 0

while down_payment > 0:
    monthsToWait += 1
    monthly_salary = annual_salary/12
    savingsFromSalary = monthly_salary * portion_saved
    monthlyReturn = current_savings * (r/12)
    current_savings += savingsFromSalary + monthlyReturn
    down_payment = down_payment - (savingsFromSalary + monthlyReturn)
print('You will have to wait ', monthsToWait, 'months before you can afford to buy the house.')