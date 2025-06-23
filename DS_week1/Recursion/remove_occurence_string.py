def strings(s,o):
    if s=="":
        return ""
    if s[0]==o:
        return strings(s[1:],o)
    else:
        return s[0]+strings(s[1:],o)
        
print(strings(s="hello",o="l"))