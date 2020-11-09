# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class ClassRegister:
  def __init__(self, class_name: str):
    self.students = []
    self.class_name = class_name

  def add_student(self, first_name: str, last_name: str):
    self.students.append(Student(first_name, last_name))
    return self
  def next_student(self, first_name, last_name):
    return next(x for x in self.students if
                x.first_name == first_name and
                x.last_name == last_name)

  def __str__(self):
    out = ""
    for i, x in enumerate(self.students, start=1):
      out += f"{str(i)}. {x}\n"
    return out

class Student:
  def __init__(self, first_name: str, last_name: str):
    self.first_name = first_name
    self.last_name = last_name
    self.full_name = f"{first_name} {last_name}"
    self.marks = {}
    self.attendance = {}

  def __str__(self):
    return f"{self.full_name}: {self.marks}: {self.attendance}"

  def average(self, subject: str):
    pass
    # for x in self.marks
    # no time to do it :c

  def get_attendance_data(self):
    pass

  def add_mark(self, mark: int, course: str):
    if(course in self.marks):
      self.marks[course] += (mark,)
    else:
      self.marks[course] = (mark,)
    return self

  def add_attendance(self, attendance: bool, date):
    self.attendance[date] = attendance
    return self

if __name__ == "__main__":
  class_register_1A = ClassRegister("1A")
  class_register_1A.add_student("Piotr", "Kolecki")
  class_register_1A.add_student("Jack", "Sassin")
  class_register_1A.add_student("Janusz", "Gajos")


  class_register_1A.next_student("Piotr", "Kolecki").add_mark(2, "PiTE").add_mark(2, "PiTE").add_mark(2, "PiTE").add_mark(2, "PiTE")

  class_register_1A.next_student("Jack", "Sassin").add_mark(2, "MoneyManagement").add_mark(2, "PiTE")

  class_register_1A.next_student("Janusz", "Gajos").add_mark(5, "PiTE")

  class_register_1A.next_student("Piotr", "Kolecki").add_attendance(True, "09.11.2020").add_attendance(True, "02.11.2020")
  class_register_1A.next_student("Jack", "Sassin").add_attendance(False, "09.11.2020")
  class_register_1A.next_student("Janusz", "Gajos").add_attendance(True, "09.11.2020")

  print(class_register_1A)
