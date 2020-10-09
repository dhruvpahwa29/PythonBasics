#FOR LOOP::

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

#We Can Also Use Range Function In Python

for x in range(5): #prints out 0,1,2,3,4
    print(x)

for x in range(1,6): #prints out 1,2,3,4,5
    print(x)

for x in range(1,9,2): #prints out 1,3,5,7,9
    print(x)


#WHILE LOOP::

count = 0
while count<5:
    print(count) #While loops repeat as long as a certain boolean condition is met.
    count+=1 #prints out 0,1,2,3,4
    
