# Tuples

def in_put() :
    text_name = input("Enter the name of file: ")
    return text_name

def executefile(text_name) :
    if text_name == "p":
        text_exe = open('progrm8.txt')
    return text_exe

def sender_dict(text_exe) :
    senders = dict()
    for lines in text_exe:
        if lines.startswith('From '):
            words = lines.split()
            if words[1] not in senders:
                senders[words[1]] = 1
            else:
                senders[words[1]] += 1
    return senders

def sender_list(senders) :
    
    reqdlist = []
    for tpl in senders:
        reqdlist.append((senders[tpl],tpl))
    reqdlist.sort()
    print(reqdlist[-1])

def main() :
    text_name = in_put()
    text_exe = executefile(text_name)
    sender = sender_dict(text_exe)
    sender_list(sender)
main()