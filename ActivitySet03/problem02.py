from fractions import Fraction
def inp():
    x=input('enter the no. of unit fractions: ')
    return int(x)

def inp_fract(x):
    fract=[]
    str = input('Enter denominators of unit fraction: ')
    str1 = str.split()
    if len(str1)>x:
        print('enter denominators equal to number of unit fractions')
    else:
        for y in str1:
            fract.append(int(y))
    return fract

def sum_of_fract(fract):
    sum = 0
    str=''
    for x in fract:
        sum+= Fraction(1,x)
        str += f'{Fraction(1,x)} + '
    str = str.removesuffix('+ ')
    str += f'= {sum}'
    return str 

def main():
    no_of_Egyp_fract = inp()
    list_of_denom=inp_fract(no_of_Egyp_fract)
    Sum_of_Egyp_fract = sum_of_fract(list_of_denom)
    print(Sum_of_Egyp_fract)
if _name_ == '_main_':
    main()