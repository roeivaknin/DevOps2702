#1

# a = 1 / 0

# 2

try:
    a = 1 / 0
except ZeroDivisionError:
    print("Could not divide by zero")

# 3

# Yes, finally will print at the end of the code no matter what (weather code is valid or not)

# 4

# This is a general exception that will handle all kind of exceptions.

# 5

# It very generic exception and will not report for specific exception - so it is very general.
# Instead of using a specific exception and then you can peforms actions based on specific exception.

# 6

# except IOError - handle input or output errors, that mostly come from users (such as wrong filename, so on).
# except ZeroDevisionError - handle errors of diving a number with 0.


# 7

my_file = open("words.txt", "w")
my_file.close()

# 8

my_file = open("words.txt", "w")
my_file.write("roei")
my_file.close()

# 9

my_file = open("words.txt", "r")
my_name = my_file.read()
print(f"Name on file: {my_name}")
my_file.close()

# 10

my_file = open("words.txt", "w", encoding='utf-8')
my_file.write("רועי")
my_file.close()

my_file = open("words.txt", "r")
my_name = my_file.read()
print(f"Hebrew name on file: {my_name}")
my_file.close()

# Challenge

from PIL import Image

img = Image.open("png_file.png")
img.show()