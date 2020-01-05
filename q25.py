r = int(input("Enter radius of circle "))
ui = input("\n(A) Calculate area \n(P) Calculate perimeter \n(B) Calculate both\n").upper()
if ui=="A":
    print(3.14*r*r)
elif ui=="P":
    print(2*3.14*r)
elif ui=="B":
    print("\nArea = ",3.14*r*r)
    print("\nPerimeter = ",2*3.14*r)
else:
    print("Invalid character entered :(")