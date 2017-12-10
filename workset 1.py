#Exercise 5

'''
less_value  = 0.1
more_value = 0.25

# taking input of the values

less_lit = int(input(" Enter the number of bottle with less than 1 lt values"))     #taking input as int, type casting
more_lit = int(input(" Enter the number of bottle with more than 1 lt values"))

result = less_value*less_lit + more_lit*more_value      # result becomes float
print(" The total refund values is $ %0.2f"%result)       # reference of variable, preciaion 0.2 two decimals  0.3 three 0.3f
'''
'''

block A , % 


%person x

xyz = "Thisis a fine "

abc = "Day"



print(xyz+abc)      # string cancatinion    when both are same data type
print(xyz,abc)      # printing them sepratly, str next to int , float to int'''


#Exercise 6
meal_cost =  82
tip =0.18*meal_cost
tax =  0.2*meal_cost

grand_total = meal_cost+tip + tax

#to do : set precision after 2 decimals
print("Bill \nMeal \t",meal_cost,"\nTip \t",tip)
print("Tax \t",tax,"\nGrand total \t",grand_total)

