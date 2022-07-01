# Files

name=input("enter the file name :")
if name == 'p':
    file_ex = open('pythontext.txt')
    for lines in file_ex:
        capitalize=lines.upper()
        print(capitalize)
