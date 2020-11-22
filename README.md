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

# Issues
* no data validation
    * very easy to break json input
    * user typo may create new subject
* School / Class are similar yet different enough for separate classes