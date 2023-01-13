import os


def get_file_path():
    return os.getcwd()


def get_name(name, names_on_file):
    with open(names_on_file, "r") as file:
        names = file.readlines()
        with open("baby2008_formatted.txt", "w+") as input_file:
            names = [input_file.write(str(name.replace("\t", "\n")[1:].strip()) + "\n") for name in names]
            names = [name.replace("\n", "") for name in input_file.readlines()]

    low, high = 0, len(names) - 1
    print(names)
    while low <= high:
        try:
            middle = (low + (high - low)) // 2
            if names[middle] == name:
                return middle
            elif middle < names.index(name):
                low = middle + 1
            else:
                high = middle - 1
            return -1
        except ValueError as err:
            print("Value not found")
            break


def read_name(file_name):
    with open(file_name, "r") as file:
        first_name = file.readline()
        second_name = file.readline()
        return first_name, second_name


# first_name, second_name = read_name("name.txt")
# print(first_name, second_name)
#
# print(get_file_path())

print(get_name("rackle", "baby2008.txt"))
