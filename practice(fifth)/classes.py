class Point:
    def move(self):
        print("Moving")

    def draw(self):
        print("Drawing")


point1 = Point()
point1.x = 10
point1.y = 20

print(point1.x)
point1.draw()


# Accessing function inside the class
class MyClass:
    def myFunction(self):
        print("This is the function inside the class")


clas = MyClass()
clas.myFunction()

# Exercise: 2

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())