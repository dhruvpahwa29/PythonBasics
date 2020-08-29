a ='HELLO DHRUV'
print(a)
a = "HELLO DHRUV"
print(a)
#The difference between the two is that using double quotes makes it easy to include apostrophes
#(whereas these would terminate the string if using single quotes)
b = "Don't worry about apostrophes"
print(b)
#We cannot use single quotes inside single quotes statement and double quotes inside double quotes statement
#If we want to use single qouotes inside single quotes and in double quotes case ,we can use like this:
print('hello\'world\' world')
print("hello\"world\" world")
#As we use backslash before quotation marks then it means quotation marks only as\' means single quotes, \" means double quotes, \n means new line,\t means tab space and \b means backspace.       

print("line a \n line b")
print("name:\t Dhruv")
#print("this is blackslash\") this will not run as \" acc. to interpreter our line is not completed we should use \\ to print a singlr backslash
print("this is backslash\\")
print("hell\blo")# this is backspace
