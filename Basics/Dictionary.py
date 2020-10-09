#DICTIONARY::

#A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

phonebook={}
phonebook["DHRUV"]=1234
phonebook["KAMAL"]=4321
phonebook["PARUL"]=5678
print(phonebook)# here,phonebook is dictionary, dhruv,kamal, and parul are keys and 1234,4321,5678 are the values stored in different keys resp.

#Dictionary can also be initialised as follows:

phonebook = {
    "DHRUV":1234,
    "KAMAL":4321,
    "PARUL":5678
}
print(phonebook)

#Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, does not keep the order of the values stored in it. To iterate over key value pairs, use the following syntax:

phonebook = {"DHRUV":1234,"KAMAL":4321,"PARUL":5678}
for name,number in phonebook.items():
    print("PHONE NUMBER OF %s is %d"%(name,number))
          
#Removing a value from dictionary::

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

#or we can also remove using pop() function

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)
