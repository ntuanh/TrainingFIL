# create students management 

class Student :
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade
    
    def get_average_grade(self):
        pass 

    def get_grade(self):
        return self.grade
    

class Course :
    def __init__(self, name, max_student ):
        self.name = name
        self.max_student = max_student
        self.students = []
    
    def add_student(self , student ):
        if len(self.students) < self.max_student :
            self.students.append(student)
            print(f"Addition student {student.name} successful !")
            return True 
        else :
            print(f"Addition student {student.name} failed !")
            return False
        
    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.grade 
        return value / len(self.students)
    
student_1 = Student("Tim" , 20 , 50)
student_2 = Student("Tom" , 21 , 60)
student_3 = Student("Kim" , 20 , 90)
course = Course("Math" , 3)
# course.add_student(student_1)
# course.add_student(student_2)
# course.add_student(student_3)
# print(course.get_average_grade())  # 66.66666666666

"""def spam():
    global eggs 
    eggs = 'spam'

spam()
print(eggs)"""
 # output : 'spam'

class Shape:
    def area(self):
        pass 

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height 
    
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius 
    
shapes = [Rectangle(4 , 5) , Circle(5)]

for shape in shapes :
    print(shape.area())  # 20.0 78.5



        