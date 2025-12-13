class Student:
    def __init__ (self , name , roll):
        self.name = name
        self.roll = roll
    def display(self):
        return (f"{self.name} : {self.roll}")
        
def main():
    student_list = []
    num_students = int(input("Enter no of students: "))
    for i in range(num_students):
        i_name = input("Enter the name: ")
        i_rollno = int(input("Enter the roll no: "))
        new_student = Student(i_name , i_rollno)
        student_list.append(new_student)
    for s in student_list:
        print(s.display())
main()