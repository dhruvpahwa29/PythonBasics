#LIST IS MUTABLE,ITS VALUES CAN BE CHANGED
a = [1,2,3,4]
print(a)
print(a[0])
print(a[1:100])
print(a[-1])

b = ['HI','DHRUV',3.4,'PAHWA',3]#IN LISTS,MIXTURE OF VARIABLES CAN BE USED IN A SINGLE LIST
print(b)

c =[a,b]
print(c)

a.append(43)#IT WILL INSERT NUMBER 34 AT THE END OF THE LIST
print(a)

c.append(56)
print(c)

b.insert(2,86)#IT WILL INSERT A NUMBER AT A PARTICULAR INDEX VALUE, IN THIS CASE 2 IS THE INDEX VALUE
print(b)

a.remove(3)#IT WILL REMOVE THE VALUE IN ROUND BRACKETS AND WE DON'T NEED TO PUT INDEX VALUE IN REMOVE FUNCTION
print(a)

a.pop(1)#IT WILL REMOVE THE VALUE WHICH IS AT THE POSITION AS IN THE ROUND BRACKETS BCZ THE POP CONTAINS THE INDEX NUMBER OF THE VALUE WE WANT TO DELETE  
print(a)

a.pop()
print(a)

del b[2:4]#IT WILL REMOVE FROM INDEX VALE 2 TILL INDEX VALUE 4 ELEMETS OF THE LIST BASICALLY DEL FUNCTION IS USED WHEN WE HAVE TO REMOVE MORE THAN ONE VALUES
print(b)

a.extend([6,4,3.7,8])#IT WILL ADD ALL THE VALUES IN THE SQUARE BRACKETS AT THE END OF THE LIST
print(a)

print(min(a))#IT WILL PRINT THE LEAST VALUE OF A PARTICULAR LIST
print(max(a))#IT WILL PRINT THE MAXIMUM VALUE OF A PARTICULAR STRING
print(sum(a))#IT WILL PRINT THE SUM OF ALL THE VALUES OF A PARTICULAR LIST