#PATTERN NO::1

n = int(input("ENTER NUMBER OF ROWS FOR PATTERN::"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#PATTERN NO::2
    
n = int(input("ENTER NUMBER OF ROWS FOR PATTERN::"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
#PATTERN NO::3

n = int(input("ENTER NUMBER OF ROWS FOR PATTERN::"))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for j in range(n+1-i,n+i):
        print(i,end=" ")
    print()

#PATTERN NO::4

n = int(input("ENTER NUMBER OF ROWS FOR PATTERN::"))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
        
    print()









                   
