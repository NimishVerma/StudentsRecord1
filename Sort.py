class Student(object):
    def __init__(self):
        self.name = raw_input(str("Enter name:"))
        self.rollno = int(raw_input("Enter roll no:"))
        self.section = raw_input("Enter section:")
        
student_list = {}
for i in range(10):
    student_list[i] = Student()
for i in range(10):
    if student_list[i].rollno > student_list[i+1].rollno:
        student_list[i], student_list[i+1] = student_list[i+1], student_list[i]
    