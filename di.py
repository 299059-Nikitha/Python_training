# Create an empty dictionary called bird
bird={}
# Add name, color, breed, legs, age to the bird dictionary
bird['name']='crow'
bird['color']='black'
bird['breed']='male'
bird['age']=10
print(bird)

# Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys for the dictionary
student_dict={'first_name':'Nikitha','last_name':'laxman','gender':'female', 'age':22, 'marital_status':'single', 'skills':['c','python','ardino uno'], 'country':'india', 'city':'banglore','address':'ecity'}

# Get the length of the student dictionary
print(len(student_dict))

# Get the value of skills and check the data type, it should be a list
print(student_dict['skills'])

# Modify the skills values by adding one or two skills
student_dict['skills'].extend(['c++','linux'])
print(student_dict['skills'])

# Get the dictionary keys as a list
li=[]
for i in student_dict.keys():
    li.append(i)
print(li)

# Get the dictionary values as a list
li1=[]
for j in student_dict.values():
    li1.append(j)
print(li1)

# Change the dictionary to a list of tuples using items() method
for k in student_dict.items():
    print(list(k))

# Delete one of the items in the dictionary
student_dict['skills'].remove('c')
print(student_dict)

# Delete one of the dictionaries
del student_dict['address']
print(student_dict)