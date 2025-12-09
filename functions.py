# def add():
#     print("Hello")

# add()

# def add(a,b):
#     print(a+b)
# add(60,70)
# add(66,70)
# add(60,80)
# add(62,75)
# add(60,70)

# return
# def add(a,b):
#     return a+b

# print(add(60,70))

# def user(name,age):
#     print(f'The user Name is:{name} and the age is {age}')

# user(age=30,name="abc")

# args
def add(*num1):  # num1 = (70,50,60)
    total = 0
    for i in num1:
        total+=i
    print(total)

add(70,50,60)
add(50,80,99,66)


# kwargs
# def userInfo(**users):
#     for key,value in users.items():
#         print(key,value)

# userInfo(name="arun",age=25,city="CBE")
# userInfo(name="arun",age=25,city="CBE",course="Python")

# lambda
square = lambda x,y:x*y
print(square(5,10))


def greet():
    print("Hello")