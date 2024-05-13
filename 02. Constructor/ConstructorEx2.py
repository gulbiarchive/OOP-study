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
        result = self.first * self.second
        return result
    
a = FourCal(4, 2)  # 생성자 호출하여 객체 생성
print("초기 값:", a.first, a.second)  # 초기값 출력

a.setdata(3, 7)  # setdata 메서드를 호출하여 속성 변경
print("변경된 값:", a.first, a.second)  # 변경된 값 출력

print("덧셈 결과:", a.add())  # 덧셈 결과 출력
print("곱셈 결과:", a.mul())  # 곱셈 결과 출력