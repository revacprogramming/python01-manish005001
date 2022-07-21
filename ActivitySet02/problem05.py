#s=system;d=database;u=username;p=ord
def get_cs():
    cs = input("enter your value")
    return cs

def cs_to_dict(cs):
    reqd_dict = dict()
    for ele in cs:
        ele = cs.split(';')
    for x in ele:
        word = x.split('=')
        reqd_dict[word[0]] = word[1]
    return reqd_dict

def dict_to_cs(d):
    reqd_cs = ''
    for i in d:
        reqd_cs+=(f"{i} = {d[i]} ; ")
    return reqd_cs

def main():
    cs = get_cs()
    d = cs_to_dict(cs) 
    print(d)
    cs = dict_to_cs(d)
    print(cs)

if _name_ == '_main_':
    main()