def isPalindrome(pal):
    return pal == pal[::-1]
#                   [start:stop:step]

pal = input("Enter string to test for palindrom or 'exit': ")
ans = isPalindrome(pal)
if ans:
    print("Palindrome Test: True")
elif pal == "exit":
    exit()
else: 
    print("Palindrome Test: False")
