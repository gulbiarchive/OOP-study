# Python-OOP-Study
파이썬으로 객체 지향 공부

# 클래스와 객체(object)

- 클래스 : 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면
- 객체 : 클래스로 만든 피조물(과자 틀을 사용해 만든 과자)

```python
과자 틀 -> 클래스
과자 틀을 사용해 만든 과자 -> 객체
```

## 객체의 중요한 특징

- 객체마다 고융한 성격 가진다는 것
- 쉽게 이해
    - 과자 틀로 만든 과자에 구멍을 뚫거나 조금 베어 먹더라도 다른 과자에는 아무 영향이 없다는 것과 마찬가지로 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않음

---

# 클래스와 객체 생성

```python
class Cookie:
	pass # 아무것도 수행하지 않는 문법(임시로 코드 작성할 때 주로 사용)
```

- 아무 기능도 갖고 있지 않은 껍질뿐인 클래스
- 껍질뿐인 클래스도 객체 생성하는 기능 있음 → 과자 틀로 과자를 만드는 것처럼

```python
class Cookie:
	pass

a = Cookie()
b = Cookie()
```

- Cookie()의 결괏값을 돌려받은 a, b → 객체
    - 마치 함수를 사용하여 그 결괏값을 돌려받는 모습과 비슷
- 파이썬 클래스명 작성 시 주의 사항
    - 파이썬 클래스 이름은 대문자로 시작!

---

# 객체와 인스턴스 차이

- 클래스로 만든 객체를 인스턴스
- a는 객체이다. a 객체는 Cookie의 인스턴스이다.
- 즉, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용

```python
a = Cookie()
```

- a는 객체
- a는 Cookie의 인스턴스

---

# 메서드

- 클래스 안에 구현된 함수

```python
# 형식
class 클래스명:
	def 메서드명(매개변수):
		수행 코드
```

# 정리

```python
#1 함수(사용자 지정 함수)
def 메서드명(매개변수):
	수행코드
-------------------
#2 내장 함수
print()
insert()
list()
input()
...
----------------------
#3 메서드
class 클래스명:
	def 메서드명(매개변수):
		수행 코드
```

---

# 2개의 숫자 값 설정하는 클래스

- 클래스, 메서드 등에 대해 자세히 알아보기!

```python
# 클래스 구조
class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second
		

a = FourCal() # a 객체 생성
a.setdata(4, 2) # 객체를 통해 클래스의 메서드를 호출하려면 도트(.) 연산자 사용

print(a.add())
```

## 1) setdata 메서드의 매개변수

- self, first, second 3개 입력값을 받는다.
- 일반 함수와 달리 메서드의 첫 번째 메서드 self는 특별한 의미

### 매개변수는 3개인데 인자는 왜 2개일까?

```python
class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second
		
a = FourCal()
a.setdata(4, 2)
```

- 첫 번째 매개변수 self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달
- 정리
    - self → a 객체 전달
    - first → 4 전달
    - second → 2 전달
- 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self 사용
- 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self 사용

## 2) setdata 메서드의 수행문

```python
class FourCal:
	def setdata(self, first, second): # 메서드의 매개변수
		# 메서드의 수행문
		self.first = first 
		self.second = second
	
a = FourCal()
a.setdata(4, 2)
```

- a.setdata(4, 2)처럼 호출하면 setdata 메서드의 매개변수 first, second에는 각각 값 4, 2가 절달되어 아래처럼 해석

```python
self.first = 4 # a.first = 4
self.second = 2 # a.second = 2
```

---

# 2개의 숫자 더하는 기능 클래스

```python
# 클래스 구조
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
		
    def add(self):
        result = self.first + self.second
        return result

a = FourCal() 
a.setdata(4, 2)

print(a.add())  # 6
```

---

# 실습1

```python
아래 코드를 활용하여 빼기, 곱하기, 나누기 기능도 추가하여
아래처럼 출력하는 프로그램을 작성하시오.

출력
6
2
8
2.0

코드
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
		
    def add(self):
        result = self.first + self.second
        return result

a = FourCal() 
a.setdata(4, 2)

print(a.add())
```

- 정답
    
    ```python
    class FourCal:
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
    
    a = FourCal() 
    a.setdata(4, 2)
    
    print(a.add())  
    print(a.mul())
    print(a.sub())
    print(a.dev())
    ```
    

# 실습2

```python
a, b 객체를 생성하고
sedata에 10, 20, 30을 전달하고 
코드를 작성하시오.

출력
a 객체의 더한 값은 60
b 객체의 곱한 값은 6000
```

- 정답
    
    ```python
    class FourCal:
        def setdata(self, first, second, third):
            self.first = first
            self.second = second
            self.third = third
    		
        def add(self):
            result = self.first + self.second + self.third
            return result
        
        def sub(self):
            result = self.first * self.second * self.third
            return result
    
    a = FourCal() 
    a.setdata(10, 20, 30)
    
    b = FourCal()
    b.setdata(10, 20, 30)
    
    print(f'a 객체의 더한 값은 {a.add()}')  
    print(f'b 객체의 곱한 값은 {b.sub()}')
    
    ```
    # 생성자 필요한 이유

```python
**class FourCal:
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

a = FourCal() 
# a.setdata(4, 2)

print(a.add())  
print(a.mul())
print(a.sub())
print(a.dev())**
```

```python
**Traceback (most recent call last):
  File "/Users/ex.py", line 25, in <module>
    print(a.add())  
          ^^^^^^^
  File "/Users/ex.py", line 7, in add
    result = self.first + self.second
             ^^^^^^^^^^
AttributeError: 'FourCal' object has no attribute 'first'**
```

- setdata 메서드를 수행해야 객체 a의 객체 변수 first, second가 생성되기 때문에 오류 발생
- 이런 이유로 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법

------------

# 생성자

- 객체가 생성될 때 자동으로 호출되는 메서드
- 메스드명으로 `__init__`를 사용하면 이 메서드는 생성자가 된다.

## 생성자를 추가해도 오류가 발생하는 이유는 뭘까?

- 정답
    - 인자 전달하지 않았음
    
    ```python
    a = FourCal() 
            ^^^^^^^^^
    TypeError: FourCal.__init__() missing 2 required positional arguments: 'first' and 'second'
    ```
    

```python
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

a = FourCal() 
# a.setdata(4, 2)

print(a.add())  
print(a.mul())
print(a.sub())
print(a.dev())
```

⬇️

```python
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
```

### __init__ 메서드의 매개변수

| 매개변수 | 값 |
| --- | --- |
| self | 생성되는 객체 |
| first | 4 |
| second | 2 |

---

## setdata() 메서드가 없어도 오류가 발생하지 않는데 왜 작성했을까?

```python
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
```

- 생성자
    - 객체가 생성될 때 자동으로 호출되어 초기화 작업 수행
    - 객체 생성 시 초기화 담당
- setdata 메서드
    - 객체가 생성된 후에도 속성을 변경하거나 추가로 초기화할 때 사용
    - 예 : 객체가 생성된 이후에 다른 값으로 속성을 설정하고자 할 때 setdata 메서드를 호출할 수 있음
    - 생성된 객체의 속성을 나중에 변경하거나 초기화할 때 사용

### 예시

```python
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
```

- 필요에 따라 생성자와 setdata 메서드를 함께 사용하여 객체를 초기화하고 필요에 따라 속성 변경 가능
-------------------------
# 상속의 개념

- 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것
---
# FourCal 클래스에 a의 b제곱 기능 추가

## 상속 방법

```python
class 클래스 이름(상속할 클래스 이름)
```

```python
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
        
class MoreFourCal(FourCal):
    pass
    
# a = FourCal(4, 2) 
a = MoreFourCal(4, 2) # 상속 확인

print(a.add())  
print(a.mul())
print(a.sub())
print(a.dev())
```

## 상속이 왜 필요할까?

- 클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 되지?
- 답변 : `기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.`
    

## 제곱 계산하는 MoreFourCal 클래스 생성

```python
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

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
# a = FourCal(4, 2) 
a = MoreFourCal(4, 2) # 상속 확인

print(a.pow())  # 16
```

- 상속은 기존 클래스는 그대로 놔둔 채 클래스의 기능을 확장시킬 때 주로 사용

---

# 메서드 오버라이딩

```python
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

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
a = FourCal(4, 0) 

print(a.div())
```

```python
result = self.first / self.second
             ~~~~~~~~~~~^~~~~~~~~~~~~
ZeroDivisionError: division by zero**
```

- 파이썬에서 정수를 0으로 나누면 `ZeroDivisionError` 발생
    - 수학적으로 정의되지 않은 연산

### 0으로 나눌 때 오류가 아닌 0을 돌려주도록 만들고 싶다면?

- FourCal 클래스를 상속하는 SafeFourCals 클래스 생성

```python
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
```

- FourCal 클래스에 있는 div 메서드를 동일한 이름으로 다시 작성
- 메서드 오버라이딩(덮어쓰기)
    - 부모 클래스(상속할 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
---------------------------
# 모듈

- 함수나 변수 또는 클래스를 모아 놓은 파일
- 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈

```python
# mod1.py
# Python_OOP_Study 파일에 저장
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```
# 모듈 불러오기

```python
import 모듈 이름

# mod1 모듈 불러오기
import mod1

# mod1의 add 또는 sub 기능 불러오기
import mod1.add
import mod1.sub

# add, sub처럼 모듈 이름 없이 함수 이름만 사용
from 모듈 이름 import 모듈 함수
from mod1 import add
```

## mod1의 add, sub 함수 둘 다 사용하는 방법

```python
# 콤마로 구분
from mod1 import add, sub

# * 문자 사용
# * : 파이썬에서 '모든 것'이라는 뜻
```

## mod2 파일에서 mod1 기능 사용

```python
from mod1 import *

print(add(3, 4)) # 7
print(sub(3, 4)) # -1
```
-----------------------
# 자주 발생하는 오류

- 오타 입력했을 때 발생하는 구문 오류 제외
- 실제 프로그램에서 자주 발생하는 오류

## 디렉터리 안에 없는 파일 열려고 시도

- FileNotFoundError 오류 발생

```python
f = open("없는 파일.txt", 'r')

Traceback (most recent call last):
  File "/Users/parkjihyeon/Desktop/Data/Python_OOP_Study/05. expect/ex1.py", line 1, in <module>
    f = open("없는 파일.txt", 'r')
        ^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '없는 파일.txt'
```

## 0으로 다른 숫자 나누는 경우

- ZeroDivisionError 오류 발생

```python
print(4 / 0)

Traceback (most recent call last):
  File "/Users/parkjihyeon/Desktop/Data/Python_OOP_Study/05. expect/ex1.py", line 3, in <module>
    print(4 / 0)
          ~~^~~
ZeroDivisionError: division by zero
```

## 리스트에서 얻을 수 없는 값

- IndexError 오류 발생

```python
a = [1, 2, 3]
print(a[4])

Traceback (most recent call last):
  File "/Users/parkjihyeon/Desktop/Data/Python_OOP_Study/05. expect/ex1.py", line 6, in <module>
    print(a[4])
          ~^^^
IndexError: list index out of range
```

---

# try, except문

```python
try:
	...
except [발생 오류[as 오류 메시지 변수]]:
```

- try 블록 수행 중 오류가 발생하면 except 블록 수행
- try 블록에서 오류가 발생하지 않는다면 except 블록은 수행 x

```python
except [발생 오류[as 오류 메시지 변수]]:
```

[ ] : 괄호 안의 내용은 생략할 수 있다는 관례적인 표기법

## 1. try, except만 쓰는 경우

- 오류 종류에 상관없이 오류가 발생하면 except 블록 수행

```python
try:
	...
except:
	...
```

## 2. 발생 오류만 포함한 except문

- 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록 수행

```python
try:
	...
except 발생 오류:
	...
```

## 3. 발생 오류와 오류 메시지 변수까지 포함한 except문

```python
try:
	...
except 발생 오류 as 오류 메시지 변수:
	...
```

```python
try:
    4/0
except ZeroDivisionError as e:
    print(e)

# 결과 : division by zero
```

- 4 / 0으로 나누려고 하면 ZeroDivisionError가 발생하여 except 블록이 실행되고 변수 e에 담기는 오류 메시지 출력

## 실습

```python
a = [1, 2, 3]
print(a[4])

IndexError가 발생할 때 오류 메시지를 출력하는 프로그램을 작성하시오.
```

- 정답
    
    ```python
    a = [1, 2, 3]
    try:
        a[4]
    except IndexError as e:
        print(e) # list index out of range
    ```
    

---

# try … finally

- finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행
- finally절은 사용한 리소스를 close할 때 많이 사용

```python
f = open('foo.txt', 'w')
try:
	# 무언가를 수행
finally:
	f.close()
```

- foo.txt 파일을 쓰기 모드로 연 후 try문을 수행한 후 예외 발생 여부와 상관없이 finally 절에서 f.close()로 열린 파일을 닫을 수 있다.

---

# 여러 개의 오류 처리

```python
try:
	...
except 발생 오류 1:
	...
except 발생 오류2:
	...
```

```python
try:
	a = [1, 2]
	print(a[3])
	4/0
except ZeroDivisionError:
	print('0으로 나눌 수 없다.')
except IndexError:
	print('인덱싱할 수 없다.')
```

- 인덱싱 오류가 먼저 발생했으므로 ‘인덱싱할 수 없다.’라는 문자열 출력
- 인덱싱 오류가 먼저 발생했으므로 4/0으로 발생되는 ZeroDivisionError 오류는 발생 x

## 오류 메시지 출력

```python
try:
	a = [1, 2]
	print(a[3])
	4/0
except ZeroDivisionError as e:
	print(e) 
except IndexError as e:
	print(e) # list index out of range
```

## ZeroDivisionError, IndexError 함께 처리

- 2개 이상의 오류를 동시에 처리하기 위해서는 괄호 사용

```python
try:
	a = [1, 2]
	print(a[3])
	4/0
except (ZeroDivisionError, IndexError) as e:
	print(e)
```

---

# 오류 회피

- pass를 사용하여 오류 그냥 회피

```python
try:
	f = open('없는 파일', 'r')
except FileNotFoundError: # 파일이 없더라도 오류를 발생시키지 않고 통과
	pass 
```

---

# 오류 일부러 발생시키기

- raise 명령어 사용

```python
class Bird:
	def fly(self):
		raise NotImplementedError
```

- Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수 구현하도록 만들기
- NotImplementedError
    - 파이썬 내장 오류
    - 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류 발생시키기 위해 사용

```python
class Eagle(Bird):
	def fly(self):
		print("very fast")
		
eagle = Eagle()
eagle.fly()
```

- NotImplementedError가 발생되지 않게 하려면 위처럼 Eagle 클래스에 fly 함수를 반드시 구현

```python
class Eagle(Bird): # Eagle 클래스는 Bird 클래스 상속 받음
	pass
		
eagle = Eagle()
eagle.fly()
```

- fly 함수 구현하지 않으면 NotImplementedError 발생

---

# 예외 만들기

- Exception 클래스를 상속하여 만들 수 있음

```python
class MyError(Exception):
	pass
	
def say_nick(nick):
	if nick == '악마':
		raise MyError()
	print(nick)
	
say_nick('천사')
say_nick('악마')
```

```python
천사
None
Traceback (most recent call last):
  File "/Users/parkjihyeon/Desktop/Data/Python_OOP_Study/05. expect/ex2.py", line 10, in <module>
    print(say_nick('악마'))
          ^^^^^^^^^^^^^^^^
  File "/Users/parkjihyeon/Desktop/Data/Python_OOP_Study/05. expect/ex2.py", line 6, in say_nick
    raise MyError()
MyError
```

- 천사가 한 번 출력된 후 MyError 발생

```python
class MyError(Exception):
	pass
	
def say_nick(nick):
	if nick == '악마':
		raise MyError()
	print(nick)
	
try:
    say_nick('천사')
    say_nick('악마')
except MyError:
    print('허용되지 않는 별명')
    
# 천사
# 허용되지 않는 별명
```

⬇️ 오류 메시지 사용

```python
class MyError(Exception):
	pass
	
def say_nick(nick):
	if nick == '악마':
		raise MyError()
	print(nick)
	
try:
    say_nick('천사')
    say_nick('악마')
except MyError as e:
    print(e)
    
# 천사
```

⬇️ 오류 메시지 안 나옴 

- __str__ 메서드 사용
    - pritn(e)처럼 오류 메시지를 print문으로 출력할 경우 호출되는 메서드

```python
class MyError(Exception):
	def __str__(self):
		return '허용되지 않는 별명'
	
def say_nick(nick):
	if nick == '악마':
		raise MyError()
	print(nick)
	
try:
    say_nick('천사')
    say_nick('악마')
except MyError as e:
    print(e)
```
