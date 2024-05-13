class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print("사각형의 넓이:", rect.calculate_area())