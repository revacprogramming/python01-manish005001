def in_put():
    file_name = input('Enter name of file: ')
    return file_name

def open_file(file_name):
    if file_name == 'romeo.txt':
        file_exe = open('progrm9.txt')
    return file_exe
def find_unique(file_exe) :    
    uniques=[]
    for line in file_exe:
        uniq = line.split()
        for word in uniq:
            if word not in uniques:
                uniques.append(word)
    return uniques

def main():
    file_name = in_put()
    file_exe=open_file(file_name)
    unique = find_unique(file_exe)
    unique.sort()
    print(len(unique))
    print(unique)

if _name=="main_" :
    main()