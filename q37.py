wt = eval(input("Enter wt"))
ht = eval(input("Enter ht"))
bmi = wt/(ht*ht)
if bmi<18.5:
    print("Underweight")
elif bmi<24.9:
    print("normal")
elif bmi<29.9:
    print("Overweight")
elif bmi >=30:
    print("Overweight you fat piece of shit. Better get on keto")