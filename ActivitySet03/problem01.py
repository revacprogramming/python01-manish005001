def inp_coordinates(x):
    crd=[]
    str = input(f"Enter three coordinates for the rectangle: ")
    crd1=str.split()
    for ele in crd1:
        crd.append(float(ele))
    if len(crd1)<6 | len(crd1)>6 :
        print("Enter six coordinates only")
    else:
        return crd

def calc_area(crd):  #c1 = 0,1 c2= 2,3 c3 = 4,5
    l1 = sqrt(pow(crd[2]-crd[4],2) + pow(crd[3]-crd[5],2))
    l2 = sqrt(pow(crd[0]-crd[4],2) + pow(crd[1]-crd[5],2))
    l3 = sqrt(pow(crd[0]-crd[2],2) + pow(crd[1]-crd[3],2))
    if (l1<l3) & (l2<l3):
        return l1*l2
    elif (l2<l1) & (l3<l1):
        return l2*l3
    else:
        return l1*l3

def main():
    x=inp_no_of_rectangle()
    n=0
    while n<x:
        coords = inp_coordinates(x)
        final_area = calc_area(coords)
        print(f'Area of rectangle with vertices{(coords[0],coords[1])},{(coords[2],coords[3])},{(coords[4],coords[5])} is {final_area}')
        n+=1
if _name_ == '_main_':
    main()