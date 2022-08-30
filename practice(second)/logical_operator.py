'''
We have three logical operator:
and 
or
not
'''

highIncome = True
goodCredit = False

if highIncome and goodCredit:     #replace and with or and make one true->false
    print("Eligible for loan")
else:
    print("We are really sorry....")



has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("We are very sorry.")