a = int(input("enter number: "))
b = int(input("enter number: "))
result = 0
try:
    result = a / b
    f = open("fmfmfd.txt")
except FileNotFoundError:
    print("Could not open the file")
except ZeroDivisionError:
    print("Could not divide by zero")
except BaseException as e:
    print("Something went wrong")
    print(e.args)
print(result)