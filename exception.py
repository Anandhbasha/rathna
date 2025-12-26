# try:
#     num = int(input("Enter the number:"))
#     print("Number is:",num)
# except:
#     print("Enter only numbers")

try:
    a = int(input("Enter the Number:"))
    b=0
    b=10/a
    print(b)
except ValueError:
    print("Enter only numbers")
except ZeroDivisionError:
    print("Enter the number above zero")
finally:
    print("Completed")