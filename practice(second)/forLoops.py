for item in "Python":
    print(item)


for item2 in ['Anish', 'Sugam', 'Santosh']:
    print(item2)


for item3 in [1,2,3,4,5]:
    print(item3)


for items in range(10):
    print(items)

for items2 in range(5,10):
    print(items2)


for items3 in range(5,10,2):
    print(items3)

prices = [10,20,30,40]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")