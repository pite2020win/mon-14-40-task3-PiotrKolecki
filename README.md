[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3602138&assignment_repo_type=AssignmentRepo)


# Features
* json - custom encoders / decoders
    * import / export School
    * import / export Register
    * export Student
* Static methods
* Data Structure uses <br>
    School[ClassRegister][Student]
    * marks as dict {subject: (marks as tuple)}
    * attendance as dict {date: bool}
* statistics module for calculations
    * student mean in subject
    * school mean in subject
* filter() for filtering only students with subject marks
* multiple ways to acces class / student data
* get all students from school
* get all marks from school (maintaining subjects)

# Issues
* no data validation
    * very easy to break json input
    * user typo may create new subject
* School / Class are similar yet different enough for separate classes

# Sample Output
```
INFO[2020-11-22 12:17:26,766]: saving Register to file
INFO[2020-11-22 12:17:26,767]: loading Register from file
INFO[2020-11-22 12:17:26,768]: loading Register from json
INFO[2020-11-22 12:17:26,774]: saving School to file
INFO[2020-11-22 12:17:26,775]: loading School from file
INFO[2020-11-22 12:17:26,776]: loading School from json
INFO[2020-11-22 12:17:26,776]: loading Register from json
INFO[2020-11-22 12:17:26,777]: loading Register from json
INFO[2020-11-22 12:17:26,777]: School School of Good Code, PiTE mean: 3.6363636363636362
INFO[2020-11-22 12:17:26,778]: School School of Importers, PiTE mean: 3.4444444444444446
INFO[2020-11-22 12:17:26,778]: Class 1A, PiTE mean: 3.3333333333333335
INFO[2020-11-22 12:17:26,786]: Class 2B, PiTE mean: 4
INFO[2020-11-22 12:17:26,787]: Student Piotr Kolecki, PiTE mean: 3.25
INFO[2020-11-22 12:17:26,788]: Student Piotr Kolecki, PiTE mean: 3.25
*** School "School of Good Code"
***** *** Class Register of 1A
1. Piotr Kolecki, Marks: {'PiTE': (5, 3, 2, 3)}, Attendance: {'02-11-2020': True, '09-11-2020': True, '16-11-2020': True, '23-11-2020': True}
2. Jack Sassin, Marks: {'MoneyManagement': (2,), 'PiTE': (2,)}, Attendance: {'09.11.2020': False}
3. Janusz Gajos, Marks: {'PiTE': (5,)}, Attendance: {'09.11.2020': False, '16.11.2020': True}
4. Jeb Acpis, Marks: {}, Attendance: {}

***** *** Class Register of 2B
1. Dorian Kossowski, Marks: {'PiTE': (5, 3)}, Attendance: {'02.11.2020': True, '09.11.2020': True, '16.11.2020': True, '23.11.2020': True}
2. Jack Sassin, Marks: {'MoneyManagement': (2,)}, Attendance: {'09.11.2020': False}
3. Andrzej Pizbak, Marks: {'PiTE': (5, 4, 3)}, Attendance: {'09.11.2020': True}


*** School "School of Importers"
***** *** Class Register of 1A
1. Piotr Kolecki, Marks: {'PiTE': (5, 3, 2, 3)}, Attendance: {'02-11-2020': True, '09-11-2020': True, '16-11-2020': True, '23-11-2020': True}
2. Jack Sassin, Marks: {'MoneyManagement': (2,), 'PiTE': (2,)}, Attendance: {'09.11.2020': False}
3. Janusz Hajos, Marks: {'PiTE': (4,)}, Attendance: {'09.11.2020': False, '16.11.2020': True}
4. Je Bacpis, Marks: {'Entertainment': (5,)}, Attendance: {}

***** *** Class Register of Class 5-3
1. Jack Sassin, Marks: {'MoneyManagement': (2,)}, Attendance: {'09.11.2020': False}
2. Jaroslaw Kutewa, Marks: {'PiTE': (5, 4, 3)}, Attendance: {'09.11.2020': True}


INFO[2020-11-22 12:17:26,794]: get all students: [{'first_name': 'Piotr', 'last_name': 'Kolecki', 'full_name': 'Piotr Kolecki', 'marks': {'PiTE': (5, 3, 2, 3)}, 'attendance': {'02-11-2020': True, '09-11-2020': True, '16-11-2020': True, '23-11-2020': True}}, {'first_name': 'Jack', 'last_name': 'Sassin', 'full_name': 'Jack Sassin', 'marks': {'MoneyManagement': (2,), 'PiTE': (2,)}, 'attendance': {'09.11.2020': False}}, {'first_name': 'Janusz', 'last_name': 'Gajos', 'full_name': 'Janusz Gajos', 'marks': {'PiTE': (5,)}, 'attendance': {'09.11.2020': False, '16.11.2020': True}}, {'first_name': 'Jeb', 'last_name': 'Acpis', 'full_name': 'Jeb Acpis', 'marks': {}, 'attendance': {}}, {'first_name': 'Dorian', 'last_name': 'Kossowski', 'full_name': 'Dorian Kossowski', 'marks': {'PiTE': (5, 3)}, 'attendance': {'02.11.2020': True, '09.11.2020': True, '16.11.2020': True, '23.11.2020': True}}, {'first_name': 'Jack', 'last_name': 'Sassin', 'full_name': 'Jack Sassin', 'marks': {'MoneyManagement': (2,)}, 'attendance': {'09.11.2020': False}}, {'first_name': 'Andrzej', 'last_name': 'Pizbak', 'full_name': 'Andrzej Pizbak', 'marks': {'PiTE': (5, 4, 3)}, 'attendance': {'09.11.2020': True}}]
INFO[2020-11-22 12:17:26,809]: get all grades: {'PiTE': (5, 3, 2, 3, 2, 5, 5, 3, 5, 4, 3), 'MoneyManagement': (2, 2)}
```
