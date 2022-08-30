weight = int(input("Please enter your weight: "))

inp = input("enter (L)lbs and (K)kg:  ")

if inp.upper()=="L":
    converted = str(weight * 0.45)
    print("Your weight in kg: " + converted)
else:
    converted = str(weight/0.45)
    print("Your weight in lbs: " + converted)