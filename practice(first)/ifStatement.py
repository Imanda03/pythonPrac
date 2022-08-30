is_hot = False
is_cold = True
if is_hot:
    print("Its a hot day...")
    print("Drink plenty")
elif is_cold:
     print("It's is cold day")
     print("Wear warm clothes")
else:
    print("It's a lovely day")


price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")