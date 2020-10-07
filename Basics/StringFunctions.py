name = "DHRUV PAHWA"
#len() IS A FUNCTION AND OTHER ALL WHICH WE WILL STUDY BELOW ARE METHODS,AS FUNCTION AND METHODS BOTH ARE USED FOR FUNCTIONALITY IN PYTHON BUT INTERNALLY THEY HAVE SOME DIFFERENCE

print(len(name))#len() function is used to find the length of the string
print(len("DHRUV PAHWA"))#this statement and above statement will give the same output


print(name.lower())#lower() method is used to change all the characters of the string to lower case letters


print(name.upper())#upper() method is used to change all the characters of the string to upper case letters


print(name.title())#title() method is used to change first letter of each word of the string to upper case and rest of the letters of that word to lower case, like this pattern all the words are changed in that string


print(name.count("a"))#count() method is used to count number of times a particular character (which is given in parenthesis as "a" in this case) is present in string
#the output of the previous statement will be zero as in "DHRUV PAHWA" there are zero "a" as it counts with case sensitive concept
a = "   dhruv  "

dots = "............"
print(a+dots)
print(a.lstrip() + dots)#lstrip() method is used to remove all the left side spaces of the string it means that it removes spaces before the characters of string
print(a.rstrip() + dots)#rstrip() method is used to remove all the spaces which are at the end of the string
print(a.strip() + dots)#strip() method is used to remove all the spaces before or after the string but it do not removes in between spaces of the string

#IF WE WANT TO REPLACE ANY CHARACTER OF A STRING WITH ANY OTHER CHARACTER THEN WE USE replace() method AS::
name.replace(" ","")#in first inverted commas we put what which character or whatever  we have to replace and in second inverted commas we put with which character we have to replace as in this case we are removing space as we haven't put any character in second inverted commas

b = "Dhruv___Pahwa"
print(name.replace("_","*",3))#here we entered 3 as it means how many "_" we want to replace with"*" in the string


print(name.find("A"))#find() method is used to find the position of a particular character or word as at which position that character is located in the string and if we have entered any word in inverted commas then it will give the position of the first character of that word in the string
print(b.find("_",2,7))#here 2 is the position of the string with which we want to start finding"_" in the string and 7 is the position till which we want to find"_" in the string


print(name.center(13,"*"))# center method is use when we have to print anything before and after of the string as in this case,the length of the 'name' string is 11 and we have entered 13 in center() method which means one* will be printed at the starting and one at the end of the string
print(name.center(12,"*"))#length of name string is 11 now one asterix will be printed at the end only


#STRINGS ARE IMMUTABLE
c = "DHRUV"
print(c[1])#output will be 'H'
#c[1]='h' is wrong statement as strings are immutable which means the original string once declared cannot be changed further

print(c.replace('H','h'))#this can be done but if we do:
#c.replace('H','h')
#print(c)#this will print DHRUV, because it will not change in original string ,we can putthe previous statement's c.replace function's value in other variable 
