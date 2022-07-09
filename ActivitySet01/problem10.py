# Dictionaries

def in_put() :
    file_name = input("Enter name of file: ")
    return file_name

def execute_file(file_name) :
    if file_name == 'p':
        file_exe = open('progrm8.txt')
    return file_exe

def find_days(file_exe) :
    num_of_days = dict()
    for lines in file_exe:
        if lines.startswith("From "):
            words = lines.split()
            if words[2] not in num_of_days:
                num_of_days[words[2]] = 1
            else:
                num_of_days[words[2]] += 1
    print(num_of_days)

def main() :
    file_name = in_put()
    file_exe = execute_file(file_name)
    find_days(file_exe)

    main()