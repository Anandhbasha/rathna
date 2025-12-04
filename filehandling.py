# read
# file = open("new.txt",'r')
# print(file.read())
# file.close()

# file = open("new.txt",'r')
# print(file.readline())
# file.close()

# file = open("new.txt",'r')
# readlines = file.readlines()
# print(readlines[1])
# file.close()

# write
# wri = open("new.txt","w")
# wri.write("This is new written line")
# print("New line added successfully")
# wri.close()


# wri = open("new.txt","w")
# wri.writelines(["This is new written line\n","This is a second insert Operation"])
# wri.writelines(["This is new written line\n","This is a second insert Operation"])
# print("New lines added successfully")
# wri.close()


# # append
# append = open("new.txt","a")
# append.write("\n Add this line")
# print("Added successfully")
# append.close()


# with open("new.txt",'r') as f:
#     print(f.read())


# os
import os

# if os.path.exists("newe.txt"):
#     print("File found")
# else:
#     print("file not found")

# # remove
# if os.path.exists("new.txt"):
#     os.remove("new.txt")


# file_name = "newdoc.txt"

# with open(file_name,"w") as file:
#     file.write("This new file to create")

# seek
with open("newdoc.txt",'r') as f:
    print(f.seek(7))
    print(f.tell())
    print(f.read())
# tell