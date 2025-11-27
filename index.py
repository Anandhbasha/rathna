'''print("Hello Python", end='-')
print(100)
print("red","blue","green","black",sep='/') '''

# variable
# a=20
# print(a)
# print(type(a))

# b=30
# b=60
# print(b)

# a,b,c=30,40,80

# temp = a
# a=b
# b=c
# c=temp
# print(a,b,c)

# a,b,c = b,c,a
# print(a,b,c)

# data types
# simple data types(Premitive Data types)
# int
# a=10
# print(type(a))
# # float
# a=20.5
# print(type(a))
# # string
# name = "xyx"
# print(type(name))
# # boolean
# isComing = True
# print(type(isComing))
# complex data types(Non Premitive)
#list
list = [10,10.5,"abc",True] #index 
# print(type(list))
# print(list)
#0 = 10
#1 = 10.5
#2 = "abc"
#3 = True
# print(list[0])
# print(list[1])
list[3] = 100
# print(list)
# # tuple
# tuple = (10,20,30,40,True)
# print(tuple)
# tuple[3] = 200
print(tuple[0])
# set
sets = {101,101,102,108,102,103,105,106,107,104}
print(sets)
# dictionary
person = {
    "name":"abc",
    "age":20,
    "city":"CBE",
    "family":{
        "Father":"ghrr",
        "mother":"hgghhg",
        "siblings":{
            "brother":"jkhjh",
            "sister":"hjghg"
        }
    }
}
# print(person["family"]["siblings"])
print(type(person))

import json 
newJson = json.dumps(person)
print(newJson)
print(type(newJson))


dictValue = json.loads(newJson)
print(type(dictValue))