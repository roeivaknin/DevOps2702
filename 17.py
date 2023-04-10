def get_name(name):
    my_file = open("names.txt", "a")
    my_file.write(name + '\n')
    my_file.close()


def collect_name(file_name):
    with open(file_name) as my_file:
        for line in my_file.readlines():
            print("hello " + line, end="")

for i in range(3):
    get_name(input("enter name: "))
collect_name("names.txt")