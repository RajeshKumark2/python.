def  check_palindrom(s):
    return s == s[::-1]
result = input("Enter tha Name:")
print(check_palindrom(result))