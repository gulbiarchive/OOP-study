# mod3.py

# mod2.py에서 필요한 클래스와 함수 임포트
from mod2 import PI, Math, add

# Math 클래스의 인스턴스를 생성
math_instance = Math()

# solve 메서드를 사용하여 원의 면적을 계산
radius = 5
area = math_instance.solve(radius)
print(f"Area: {area}")

# add 함수를 사용하여 두 수의 합을 계산
a = 3
b = 4
sum_result = add(a, b)
print(f"Sum: {sum_result}")
