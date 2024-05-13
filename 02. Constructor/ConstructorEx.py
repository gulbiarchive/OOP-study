class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
		
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first - self.second
        return result
    
    def sub(self):
        result = self.first * self.second
        return result
    
    def dev(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2) 
# a.setdata(4, 2)

print(a.add())  
print(a.mul())
print(a.sub())
print(a.dev())