def strings(s,o):
    if len(s)==0:
        return ""
    if s[0]==o:
        return strings(s[1:],o)
    else:
        return s[0]+strings(s[1:],o)
        
print(strings(s="helloaa",o="l"))