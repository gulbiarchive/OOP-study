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
    
    def div(self):
        result = self.first / self.second
        return result      

# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

class SelfFourCal(FourCal):
    def div(self):
        # 나누는 값이 0인 경우 숫자 0을 돌려주도록 수정
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
    
a = SelfFourCal(4, 0) 

print(a.div()) 