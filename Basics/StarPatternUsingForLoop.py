#PATTERN NO::1

n = int(input("ENTER NUMBER OF ROWS FOR STAR PATTERN::"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#PATTERN NO::2

n = int(input("ENTER NUMBER OF ROWS FOR STAR PATTERN::"))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print("*",end=" ")
    k=k+2
    print()
    
    
#PATTERN NO::3 (PYRAMID)


n = int(input("ENTER NUMBER OF ROWS FOR STAR PATTERN::"))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(n+1-i,n+i):
        print("*",end=" ")
    print()

#PATTERN NO::4 (REVERSE PYRAMID)


n = int(input("ENTER NUMBER OF ROWS FOR STAR PATTERN::"))
for i in range(1,n+1):
    for j in range(0,i-1):
        print(" ",end=" ")
    for j in range(i,(2*n)+1-i):
        print("*",end=" ")
    print()

#PATTERN NO::5 (HEART SHAPE)

for i in range(6):
    for j in range(7):
        if(i==0 and j%3!=0)or(i==1 and j%3==0)or(i-j==2)or(i+j==8):
            print("*",end="")
        else:
            print(end=" ")
    print()

