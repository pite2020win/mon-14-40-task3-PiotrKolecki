import logging
import statistics
import json

logging.basicConfig(
    format='%(levelname)s[%(asctime)s]: %(message)s',
    level=logging.INFO
)


class School:
    def __init__(self, school_name: str):
        self.school_name = school_name
        self.classes = {}

    def __str__(self):
        out = f"*** School \"{self.school_name}\"\n"
        for x in self.classes:
            out += f"***** *** {self.classes[x]}\n"
        return out

    def add_class(self, class_name):
        if(isinstance(class_name, ClassRegister)):
            self.classes[class_name.class_name] = class_name
        elif(isinstance(class_name, str)):
            self.classes[class_name] = ClassRegister(class_name)

    def mean_subject(self, subject):
        school_marks = ()
        for curr_class in self.classes:
            filtered_students = filter(
                lambda x: (
                    subject in self.classes[curr_class].students[x].marks),
                self.classes[curr_class].students)
            for x in filtered_students:
                school_marks += (*
                                 self.classes[curr_class].students[x].marks[subject],)
        school_subject_mean = statistics.mean(school_marks)
        logging.info("School {}, {} mean: {}".format(
            self.school_name, subject, school_subject_mean))
        return school_subject_mean

    def get_all_students(self):
        all_students = []
        for curr_class in self.classes:
            all_students.extend(list(self.classes[curr_class].students.values()))
        return all_students
    
    def get_all_grades(self):
        all_grades = {}
        for curr_class in self.classes:
            for curr_stud in self.classes[curr_class].students:
                for subject in self.classes[curr_class].students[curr_stud].marks:
                    if(subject in all_grades):
                        all_grades[subject] += self.classes[curr_class].students[curr_stud].marks[subject]
                    else:
                        all_grades[subject] = self.classes[curr_class].students[curr_stud].marks[subject]
        return all_grades

    def to_json(self):
        classes_json = {}
        for x in self.classes:
            classes_json[x] = self.classes[x].to_json()
        school_json = {
            "classes": classes_json,
            "school_name": self.school_name
        }
        return school_json

    def __repr__(self):
        return self.to_json()

    def save_to_file(self, file_name):
        logging.info("saving School to file")
        with open(file_name, 'w') as outfile:
            json.dump(self.to_json(), outfile, indent=4)

    @staticmethod
    def load_from_json(register_json):
        logging.info("loading School from json")
        school = School(register_json["school_name"])
        for x in register_json["classes"]:
            school.classes[x] = ClassRegister(x)
            school.classes[x].load_from_json(register_json["classes"][x])
        return school

    @staticmethod
    def load_from_file(school_json_file):
        logging.info("loading School from file")
        with open(school_json_file) as infile:
            school_json = dict(json.load(infile))
            return School.load_from_json(school_json)


class ClassRegister:
    def __init__(self, class_name: str, students={}):
        self.class_name = class_name
        self.students = dict(students)

    def add_student(self, first_name: str, last_name: str):
        self.students[f"{first_name} {last_name}"] = Student(
            first_name, last_name)
        return self

    def __str__(self):
        out = f"Class Register of {self.class_name}\n"
        for i, x in enumerate(self.students, start=1):
            out += f"{str(i)}. {self.students[x]}\n"
        return out

    def mean_subject(self, subject):
        class_marks = ()
        filtered_students = filter(
            lambda x: (subject in self.students[x].marks), self.students)
        for x in filtered_students:
            class_marks += (*self.students[x].marks[subject],)
        class_subject_mean = statistics.mean(class_marks)
        logging.info("Class {}, {} mean: {}".format(
            self.class_name, subject, class_subject_mean))
        return class_subject_mean

    def to_json(self):
        students_json = {}
        for x in self.students:
            students_json[x] = self.students[x].to_json()
        class_register_json = {
            "students": students_json,
            "class_name": self.class_name
        }
        return str(class_register_json)

    def __repr__(self):
        return self.to_json()

    def save_to_file(self, file_name):
        logging.info("saving Register to file")
        with open(file_name, 'w') as outfile:
            json.dump(self.to_json(), outfile, indent=4)

    def load_from_json(self, register_json):
        logging.info("loading Register from json")
        self.class_name = register_json["class_name"]
        for x in register_json["students"]:
            self.students[x] = Student(
                register_json["students"][x]["first_name"],
                register_json["students"][x]["last_name"],
                register_json["students"][x]["marks"],
                register_json["students"][x]["attendance"]
            )
        return self

    def load_from_file(self, register_json_file):
        logging.info("loading Register from file")
        with open(register_json_file) as infile:
            register_json = json.load(infile)
            return self.load_from_json(register_json)


class Student:
    def __init__(self, first_name: str, last_name: str, marks={}, attendance={}):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        # without dict(...) it shared data across all registers
        self.marks = dict(marks)
        for x in self.marks:
            self.marks[x] = tuple(marks[x])
        self.attendance = dict(attendance)

    def __str__(self):
        return f"{self.full_name}, Marks: {self.marks}, Attendance: {self.attendance}"

    def to_json(self):
        student_json = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "marks": self.marks,
            "attendance": self.attendance
        }
        return str(student_json)

    def __repr__(self):
        return self.to_json()

    def save_to_file(self, file_name):
        with open(file_name, 'w') as outfile:
            json.dump(self.to_json(), outfile, indent=4)

    def mean_subject(self, subject: str):
        calculate_mean = statistics.mean(self.marks[subject])
        logging.info("Student {}, {} mean: {}".format(
            self.full_name, subject, calculate_mean))
        return calculate_mean

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
    School_of_good_code = School("School of Good Code")

    # add students by hand
    class_register_1A = ClassRegister("1A")
    class_register_1A.add_student("Piotr", "Kolecki")
    class_register_1A.add_student("Jack", "Sassin")
    class_register_1A.add_student("Janusz", "Gajos")
    class_register_1A.add_student("Jeb", "Acpis")

    # add class by hand
    School_of_good_code.add_class(class_register_1A)

    # add marks
    class_register_1A.students["Piotr Kolecki"].add_mark(
        5, "PiTE").add_mark(3, "PiTE").add_mark(2, "PiTE").add_mark(3, "PiTE")

    class_register_1A.students["Jack Sassin"].add_mark(
        2, "MoneyManagement").add_mark(2, "PiTE")

    class_register_1A.students["Janusz Gajos"].add_mark(5, "PiTE")

    # add attendance
    class_register_1A.students["Piotr Kolecki"].add_attendance(
        True, "02-11-2020").add_attendance(
        True, "09-11-2020").add_attendance(
        True, "16-11-2020").add_attendance(
        True, "23-11-2020")
    class_register_1A.students["Jack Sassin"].add_attendance(
        False, "09.11.2020")
    class_register_1A.students["Janusz Gajos"].add_attendance(
        False, "09.11.2020").add_attendance(
        True, "16.11.2020")

    # export Class and Student to JSON
    class_register_1A.save_to_file("out.json")
    class_register_1A.students["Piotr Kolecki"].save_to_file(
        "out_student.json")

    # add class from JSON
    School_of_good_code.add_class("class register 2B")
    School_of_good_code.classes["class register 2B"].load_from_file("in.json")

    # export / import school JSON
    School_of_good_code.save_to_file("out_school.json")
    School_of_importers = School.load_from_file("in_school.json")

    # school mean in subject
    School_of_good_code.mean_subject("PiTE")
    School_of_importers.mean_subject("PiTE")

    # class mean in subject
    class_register_1A.mean_subject("PiTE")
    School_of_good_code.classes["class register 2B"].mean_subject("PiTE")

    # student mean in subject
    School_of_good_code.classes["1A"].students["Piotr Kolecki"].mean_subject(
        "PiTE")
    class_register_1A.students["Piotr Kolecki"].mean_subject("PiTE")

    # final print
    print(School_of_good_code)
    print(School_of_importers)

    logging.info(f"get all students: {School_of_good_code.get_all_students()}")
    logging.info(f"get all grades: {School_of_good_code.get_all_grades()}")
