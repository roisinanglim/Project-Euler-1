# Roisin Anglim 02-04-2018 
# Project Euler #1 Solution 

#Define your variables
sum = 0 
i = 1 

#Set your limit
while i < 1000: 
    if i % 3 ==0:
      sum = sum + i
    elif i % 5 ==0:
      sum = sum + i 
    i = i + 1 
print("sum of multiples",sum)
