def palindrome(s):
    if s[0] != s[-1]:
        return False
    if len(s) <= 1:
        return True
    return palindrome(s[1:-1])

print(palindrome("mamww"))