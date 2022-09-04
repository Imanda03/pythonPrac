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