names = ["inbar", "lanir", "eran", "kfir", "alina"]
numbers = [1, 2, 3, 4, 5, 6, 7]
for name in names:
    print(name, end=' ')
print('\n')

for i in range(len(names)):
    print(names[i])

a = 0
while a < 5:
    print(a)
    a += 1

for number in numbers:
    if number == 3:
        continue
    if number == 2:
        break
    print(number)
else:
    print("finished successfully")