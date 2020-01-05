s= input("Enter a string ")
s9=''
for i in range(1,len(s)+1):
    s9+=s[-i]
if s9==s:
    print("IS a PALLINDROME")
else:
    print("Not a pallindrome")