# Palindrome

def palindrome_str(string):
    string = string.casefold()
    revStr = reversed(string)
    if list(string) == list(revStr):
        print("The string is a Palindrome.")
    else:
        print("The string is not a Palindrome.")

# We can't use function overloading 
def palindrome_num(num):
    res = str(num) == str(num)[::-1]
    if res:
        print("The number is a Palindrome.")
    else:
        print("The number is not a Palindrome.")
