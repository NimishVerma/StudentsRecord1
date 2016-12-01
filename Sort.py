class Student(object):
    def __init__(self):
        self.name = raw_input(str("Enter name:"))
        self.rollno = int(raw_input("Enter roll no:"))
        self.section = raw_input("Enter section:")
    def return_class_variables(Student):
        return(Student.__dict__)
num = int(raw_input("enter number of students"))
student_list = {}
for i in range(num):
    student_list[i] = Student()
for j in range(num-1):
    if student_list[j].rollno > student_list[j+1].rollno:
        student_list[j], student_list[j+1] = student_list[j+1], student_list[j]
for k in range(num):
    print Student.return_class_variables(student_list[k])
