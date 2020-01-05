x = int(input("Enter a no. "))
isPrime = True
for i in range(2,x):
    if x%i==0:
        isPrime=False
        print("Not prime")
        break
if isPrime == True:
    print("Prime no.")