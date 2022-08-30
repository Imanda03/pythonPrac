'''
We have following comparision operators:
<
>
<=
>=
==
!=
= -> error for equal
'''

temperature = 30

if temperature > 30:
    print("Its a hot day")
else:
    print("Its a lovely day..")


name = "Anish"

if name < 3:
    print("Name must be at least 3 char")
elif name > 50:
    print("name cannot be 50 char")
else:
    print("perfect")