# 1. input for 5 ages from the user
#  print out the biggest age from the user
ages = []
for num in range(0, 5):
    userInput = int(input("Enter age: "))
    ages.append(userInput)

max = ages[0]
for num in range(0, 5):
    if ages[num] > max:
        max = ages[num]

print(f"Biggest age is: {max}")


# 2. write a function the get name as input
# from the user until the name 'moshe' and return a list of those names

def getName(name):
    names = []
    while name != "moshe":
        names.append(name)
        name = input("Enter another name: ")
    return names


print(getName(input("Enter name: ")))
