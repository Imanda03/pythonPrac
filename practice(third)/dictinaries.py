customer = {
    "name" : "Anish Sharma",
    "age" : 22,
    "is_verified" : True
}
print(customer["name"])

print(customer.get("birthday"))  #When we use get error will not occur

print(customer.get("birthday", "Dec 23 2000"))  #Yadi value xaina vanya value add garxa

#updating
customer["name"] = "Imanda"
print(customer["name"])

customer["qualify"] = "bacheloar"

print(customer["qualify"])


#Exercise: Change number into word
phome = input("Phones: ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three"
}
output = ""
for ch in phome:
    output = digits_mapping.get(ch, "!") + ""

print(output)