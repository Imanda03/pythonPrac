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

#Exercise: Loop through and print out all even numbers from the numbers list in the same order they 
#are received. Don't print any numbers that come after 237 in the sequence.

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break
    
    if number%2 ==0:
        print(number)