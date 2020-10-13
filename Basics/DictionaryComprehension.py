d = {1:2,2:4,3:6}
print(d)

#If we want to add ten elements in a dictionary which have the elements as cube of first ten elements, then we can do that as follows::

e = {x:x**3 for x in range(10)}#this is dictionary comprehension
print(e)

#we can do the same thing by using separate key and separate values as in above statement key and value both were same(cube was printed of key)

f = {k:v**3 for k,v in zip(['a','b','c','d','e'],range(5))}
print(f)



print(e.keys())#it will print keys of dictionary "e".

print(f.values())#it will print values of dictionary "f".
