#Constructor (__init__ Function)

class Student:
  college_name = "Governor House"
  name = "anonymous" #class attr

  def __init__(self, name, marks):
     self.name= name #obj attr > class attr
     self.marks = marks
print("adding new student in database")
s1 = Student("Mohsin", 97)
print(s1.name,s1.marks)

s2 = Student("Ali", 90 )
print(s2.name,s2.marks)
print(s2.college_name)