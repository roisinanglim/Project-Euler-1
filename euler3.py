#Roisin Anglim 02-04-18 
#Project Euler No.3 
n=600851475143 
i=2 
#Do this while i is less then N
while i < n: 
#Set C as a counter
  c=0  
    #If N modulus i is equal to zero , count the amount of times it equals zero. If its greater than 2 dont print i.
    if n % i == 0:
        for x in range(1,i): 
             if i % x == 0:
                 c = c +1  
        if c < 3:
            print(i) 
    i = i + 1
