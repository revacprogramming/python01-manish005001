

#s=system;d=database;u=username;p=password
def get_cs() :
    cs = input("Enter the connected string: ")
    return cs
def cs_to_lot(cs) :
    tupl_list = []
    for value in cs:
        value = cs.split(';')
    for ele in value:
        word = ele.split('=')
        tupl_list.append((word[0],word[1]))
    return tupl_list
def lot_to_cs(lot) :
    n=0
    cs=''
    while n<len(lot) :
        ele = lot[n]
        cs += (f'{ele[1]} = {ele[0]}; ')
        n += 1
    return cs.removesuffix('; ')
def main() :
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)
    cs = lot_to_cs(lot)
    print(cs)
if _name=='main_':
    main()

