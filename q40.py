x = int(input("Enter an integer "))
y = int(input("Enter another integer "))
for i in range(1,(x*y)+1):
    if i%x == 0 and i%y == 0:
        lcm = i
        break
print("LCM = ",lcm)
if x<y:
    lower = x
else:
    lower = y
for i in range(lower,0,-1):
    if x%i == 0 and y%i == 0:
        hcf = i
        break
print("HCF = ",hcf)