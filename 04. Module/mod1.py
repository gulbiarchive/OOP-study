# 파일 경로 확인하는 방법
'''
1. 파일 경로 확인
(base) parkjihyeon@bagjihyeon-ui-iMac Python_OOP_Study % pwd
/Users/parkjihyeon/Desktop/Data/Python_OOP_Study

2. 파일 절대 경로(특정 파일 경로) 확인
(base) parkjihyeon@bagjihyeon-ui-iMac Python_OOP_Study % echo $(p
wd)/mod1.py
/Users/parkjihyeon/Desktop/Data/Python_OOP_Study/mod1.py
'''
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print(add(3, 4))
print(sub(3, 4))
