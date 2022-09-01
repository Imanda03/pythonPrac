name = ['Anish', 'Sugam','Nischal','Niraj', 'Hekka']
print(name)

print(name[0])

print(name[-1])

print(name[2:4])


#Exercise: Largest Numbers

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number

print(max)