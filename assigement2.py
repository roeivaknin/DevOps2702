# A
x = 5
y = 6
if x > y:
    print("BIG")
elif y > x:
    print("small")

# B
for i in range(5):
    print(i)

# C
season = 1
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

# D 1 - 10 times
# D 2 - 10

# E
age = 25
firstLetter = "v"
usdNis = 3.59
abroad = True
apartmentNum = 8
print(
    f"age: {age}, first letter of last name: {firstLetter}, USD to NIS is: {usdNis}, flying abroad: {abroad}, apartment number is: {apartmentNum}")
age += usdNis
print(age)

# F
phoneNum = input("Enter your phone number: ")
print(f"phone number {phoneNum}")


# G
def printHello():
    print("hello")


def calculate():
    print(5 + 3.2)


# H
def printName(name):
    print(f"Name: {name}")


def divideNum(num):
    print(num / 2)


# I
def sumOfNums(num1, num2):
    return num1 + num2


def addSpace(str1, str2):
    newstr = str1 + " " + str2
    return newstr


# Challenges
# K
for i in range(5):
    for j in range(i + 1):
        print("#", end="")
    print("")

# L
l = 7
for i in range(l):
    for j in range(l):
        if (i == j) or (i + j == l - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# M
def getNum():
    number = int(input("Enter number: "))
    return number


def sumOfDigits(number):
    sum = 0
    while number > 10:
        sum += number % 10
        number //= 10
    sum += number
    return sum


print(sumOfDigits(getNum()))
