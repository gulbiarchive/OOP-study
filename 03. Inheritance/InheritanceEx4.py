class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Cat(Animal):
    def speak(self):
        print("야옹")

animal = Animal()
animal.speak()

cat = Cat()
cat.speak()