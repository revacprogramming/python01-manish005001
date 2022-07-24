# Files
def in_put():
    file_name = input("Enter Name of file: ")
    return file_name

def open_file(file_name) :

    if file_name == 'progrm8.txt':
        file_exe = open('progrm8.txt')
    else:
        print("Invalid file name")
    return file_exe

def convert_upper(file_exe) :

    for lines in file_exe:
        capitalized = lines.upper()
        print(capitalized)
    
def main() :

    file_name = in_put()
    file_exe = open_file(file_name)
    convert_upper(file_exe)

if _name=='main_' :
    main()