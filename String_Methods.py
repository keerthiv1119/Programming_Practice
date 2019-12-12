s = input()
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
for i in range(0,len(s)):
    if s[i].isalnum():
        s1 = 1
    if s[i].isalpha():
        s2 = 1
    if s[i].isdigit():
        s3 = 1
    if s[i].islower():
        s4 = 1
    if s[i].isupper():
        s5 = 1
if s1 == 1:
    print("True")
else:
    print("False")
if s2 == 1:
    print("True")
else:
    print("False")
if s3 == 1:
    print("True")
else:
    print("False")
if s4 == 1:
    print("True")
else:
    print("False")
if s5 == 1:
    print("True")
else:
    print("False")
