# Functions

def computpay(hr,pay):
    hr=h*r
    pay=((h-40)*1.5*r + 40*r)
  
    if h>40:
        return pay
    else:
        return hr

h=int(input("enter the hour :"))
r=int(input("enter the rate :"))
result=computpay(h, r)
print(result)