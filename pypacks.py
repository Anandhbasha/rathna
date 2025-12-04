# import math

# print(math.sqrt(16))
# print(math.pow(2,5))
# print(math.pi)

# random
# import random
# print(random.random())
# print(random.randint(99999,999999))
# print(random.choice(["red","blue","green","black"]))


# datetime

# import datetime
# thisday = datetime.date.today()
# print(thisday)

# timenow = datetime.datetime.now()
# print(timenow)

# import os
# print(os.name)
# print(os.getcwd())
# os.mkdir("newApp")


# re - regular expression
import re
# text = "this is my mobile number 8947845588"
# num = r'\d{10}'
# match = re.search(num,text)
# if match:
#     print("my number is:",match.group())

# password

password = "Mypassword123"

# password = input("Enter the password:")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$'
if re.match(pattern,password):
    print("Strong Password")
else:
    print("Week Password")

# statsics
import statistics as sa

value = [10,20,30,40,50]
print(sa.median(value))
print(sa.mean(value))

# collection
from collections import Counter
nums = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(Counter(nums))