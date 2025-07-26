#Create a dictionary named student_info with the following keys:
#student_name, age, roll_no, class, section, percentage, college_name
#a)Print all the keys and values from the dictionary.
import copyreg

student_info={"student_name":"Nikitha", "age":22, "roll_no":1," class":"BE", "section":"A", "percentage":90, "college_name":"TOCE"}
for i in student_info.keys():
    print("keys:",i)
for i in student_info.values():
    print("values:",i)
#b)Add a new key-value pair: 'email': 'student@example.com' to the dictionary.
student_info["email"]="student@example.com"
print(student_info)

#c)Delete the section key from the dictionary.
del student_info["section"]
print(student_info)

#Use a loop to print all key-value pairs in the dictionary in the format:Key --> Value
for i in student_info.items():
    print(i)

#Check if the key 'college_name' exists in the dictionary or not.
flag=0
for i in student_info.keys():
    if(student_info["college_name"]):
        flag=1
if flag==1:
    print("present")
else:
    print("not present")

#You are given three sets representing students enrolled in different courses:
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Bob", "Eve", "Frank", "David"}
cpp_students = {"Charlie", "George", "Eve", "Henry"}
#Find students who are enrolled in all three courses.
all_course=python_students.intersection(java_students,cpp_students)
print(f"enrolled in all three courses : {all_course}")

#Find students who are enrolled in only Python course.
print(python_students.difference(java_students,cpp_students))

#Find students who are enrolled in both Python and Java.
py_jav=python_students.intersection(java_students)
print(py_jav)

#Find students who are enrolled in either Python or Java but not both.
print("either:",python_students^java_students)


#Find the list of all unique students enrolled in any course.
print(python_students.union(java_students,cpp_students))

#Find students who are in Java or C++, but not in Python.
both=java_students.union(cpp_students)
print("not py:",both.difference(python_students))



#Check if all Python students are also Java students.
print("python students in java:",python_students.intersection(java_students))



#Add a new student "Jones" to the Python set.
python_students.add("Jones")
print(python_students)

#Remove "Frank" from the Java set.
print(java_students.remove("Frank"))
print(java_students)

#Clear the cpp_students set.
cpp_students.clear()
print(cpp_students)
