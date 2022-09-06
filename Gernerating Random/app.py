import random

for i in range(3):
    print(random.random())


print(random.randint(10, 30))

members = ["anish", "sugam", "niraj", "nischal"]
print(random.choice(members))


#Exercise: dice

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)


dice = Dice()
print(dice.roll())