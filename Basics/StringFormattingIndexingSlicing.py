#STRING FORMATTING::
a = int(input("ENTER FIRST VALUE::"))
b = int(input("ENTER SECOND VALUE::"))
c = int(input("ENTER THIRD VALUE::"))
avg = (a+b+c)/3
print(f"AVERAGE OF THREE VALUES YOU ENTERED IS::{avg}")#this is string formatting



#STRING INDEXING::
language="python"
#INDEX VALUE OF EACH CHARACTER IS AS FOLLOWS::
#p=0 or -6
#y=1 or -5
#t=2 or -4
#h=3 or -3
#o=4 or -2
#n=5 or -1

#IF WE WANT TO PRINT ANY PARTICULAR CHARACTER OF A STRING ::
print(language[4])
#IF WE WANT TO PRINT LAST CHARACTER OF A STRING AND WE DON'T KNOW THE SIZE OF STRING THEN WE CAN SIMPLY DO THIS::
print(language[-1])



#STRING SLICING::
#IF WE WANT TO PRINT MORE THAN ONE CHARACTER OF A PARTICULAR STRING THEN WE USE STRING SLICING
print(language[0:3])#it will print language[0],[1],[2] asstarting value is included and the end value is excluded
print("python"[0:3])#above statement and this one are same and will provide the same output

print("python"[:])#it will print the whole string
print("python"[1:])#it will print characters from 1 index value to end
print("python"[:4])#it will print characters from starting to 3 index value


#STEP ARGUMENTS IN STRING SLICING::
#IT IS USED WHEN WE HAVE TO SKIP CHARACTERS IN A PERFECT SEQUENCE
print("computer"[0:5:1])#here step is 1 which will give the same output as [0:5},step of 1 means we don't need to skip any value
print("computer"[0:6:2])#here step is 2 which will print the characters from index value 0 to 5 with skipping one character after each character
print("computer"[0::3])#here is no end index value mentioned so it will print till end with skipping 2 characters after each character

#IF WE WANT TO PRINT STRING FROM THE BACK THEN SIMPLY WE CAN DO AS FOLLOWS::
print("computer"[4::-1])#step of -1 we have to skip previous value but here is step of -1 which means we do not have to skip any value but only we have to go back or reverse
print("computer"[-1::-1])#it will print full reverse string
#WE CAN ALSO PRINT FULL REVERSE STRING AS::
print("computer"[::-1])

