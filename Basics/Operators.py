#ARITHMETIC OPERATORS::

x = 2
y = 3

print(x+y) #Addition operator
print(x-y) #Subtraction operator
print(x*y) #Multiplication Operator
print(x/y) #Division Operator
print(y%x) #Modulus Operator


#ASSIGNMENT OPERATOR::


x=x+2
x+=2 #These both statements mean same as in both statements we are adding 2 to x itself
x*=3 #In this statement we are multiplying x itself by 3

a,b = 34,43 #Assigning values to more than one variables simultaneously in a single line
print(a)
print(b)

c=7
c=-c
print(c)


#RELATIONAL OPERATORS::

print(x>y) #Greator than operator here x=18 and y=3 as mentioned above
print(x<y) #Smaller than operator
print(x==y) #It compares whether both the values are same or not
x=3 #Now x and y both are same
print(x==y) #Equal To Operator: Now the output will be true
print(x>=y) #Greator Than Or Equal To Operator: It will print true when either x is greator than y or equal to y
print(x<=y) #Smaller Than Or Equal To Operator: It will print true when either x is smaller than y or equal to y
print(x!=y) #Not Equal Operator: It will print false as here both are equal


#LOGICAL OPERATORS::

a = 8
b = 10
print(a<9 and b<8) #And Operator: It will print true only if both conditions are true ,here the output will be false
print(a<9 or b<8) #Or Operator: It will print true when only one or both statements are true,here the output will be true
a =True
a=not a #Not Operator :We can use not operator for reversing value
print(a)
