class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Moving")
    
    def draw(self):
        print("Drawing")
    
point1 = Point(10, 20)

print(point1.x)

#Exercise:
class Person:
    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print("talking")

anish = Person("Anish Sharma")
anish.talk()

print(anish.name)

#Modify:
class Persons:
    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print(f"Hi! I am {self.name}")

anish = Persons("Anish Sharma")
anish.talk()

sugam = Persons("Sugam Poudel")
sugam.talk()
