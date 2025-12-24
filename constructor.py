class Student:
    def __init__(self):
        self.studentName = ""

    def show(self):
        print(self.studentName)

S = Student()
S.studentName = "Arun"
S.show()