# Files

name=input("enter the file name :")
if name == 'p':
    file_exe = open('pythontext.txt')
    for lines in file_exe:
        capitalize=lines.upper()
        print(capitalize)
