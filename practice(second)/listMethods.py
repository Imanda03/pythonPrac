numbers = [5, 2, 1, 7, 4]

numbers.append(10)  # add 10 at the last

numbers.insert(0, 20)  #add 20 at the index 0 -----> 0 means index here

numbers.remove(5)    #Remove 5 here

#numbers.clear()     #Clear all the numbers

numbers.pop()    #Delete the last index

numbers.index(2)    #Find the index where 5 lies

print(50 in numbers)        #Check the 50 in numbers and return boolean

numbers.sort()              #Sort in ascending order

numbers.reverse()            #Sort in Reverse

numbers2 = numbers.copy()   #Copy all the number in numbers2

#Exercise: Remove duplicate
numbersss = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbersss:
    if number not in uniques:
        uniques.append(number)
print(uniques)