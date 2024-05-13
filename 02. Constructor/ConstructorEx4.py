class Student:
    def __init__(self, name, grade, score):
        self.name = name
        self.grade = grade
        self.score = score
    
    def update_score(self, new_score):
        self.score = new_score
    
    def print_info(self):
        print("이름:", self.name)
        print("학년:", self.grade)
        print("성적:", self.score)

student = Student("Alice", 10, 85)
student.print_info()
print()
student.update_score(90)
student.print_info()