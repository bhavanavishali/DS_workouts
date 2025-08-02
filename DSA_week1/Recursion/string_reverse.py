def string_rev(s):
    if s=="":
        return ""
    return string_rev(s[1:])+s[0]

print(string_rev('bhavana'))