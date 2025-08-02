# 1)Sum of Positive Numbers Until Zero Take integer inputs from the user until they enter 0.Print the sum of only positive numbers.
sum=0
while True:
    n=int(input("enter only number:"))
    if n>0:
        sum=sum+n
    if n<0:
        continue
    if n==0:
        break
print("sum:",sum)

# 2)Student Grade Classifier (if-elif-else) Input 3 subject marks. Use if-elif-else to assign grade:
#≥90 → A,75-89 → B,60-74 → C,<60 → F
total = 0
for i in range(3):
    marks = int(input("enter the marks:"))
    total = total + marks
average = total / 3
print(average)
if average >= 90:
    print("A")
elif average >= 75:
    print("B")
elif average >= 60:
    print("C")
else:
    print("F")

# 3)Given a list of tuples[(10, 2), (5, 0), (8, 4)],divide first by second only if second is not zero. tup=[(10, 2), (5, 0), (8, 4)]
for i in range(len(tup)):
    if tup[i][1]==0:
        continue
    print(tup[i][0]/tup[i][1])

#5).Hollow Pyramid Pattern with Numbers
# 	 1
#   1 2
#  1   3
# 1     4
#1 2 3 4 5
num = int(input("Enter number: "))
for i in range(1, num + 1):
    # Leading spaces
    print(" " * (num - i), end="")

    if i == 1:
        print("1", end="")
    elif i == 2:
        print("1 2", end="")
    elif i == num:
        print(" ".join([str(x) for x in range(1, i + 1)]), end="")
    else:
        print("1", end="")
        print(" " * (2 * (i - 2) + 1), end="")
        print(f"{i}", end="")
    print()

#------------------------------------------------------------------------------------------------------------
#1)Calculate BMI Take height and weight from user, computeBMI = weight / height²,result.[float, input / output, basic operators]
wight=float(input("weight:"))
height=float(input("enter height:"))
BMI=wight/height**2
print(BMI)

#2)Given a list, count how many numbers are odd vs even. [list, int, loop, if-else, bool]
li=[ ]
even=0
odd=0
a=int(input("enter the range:"))
for i in range(a):
    user=int(input("enter only number:"))
    li.append(user)
    if user%2==0:
        even=even+1
    else:
        odd=odd+1
print("summ of even and odd",even,odd)

#3)Input username and password.  If username is correct: Check password Else invalid password
a={"user_name1":"Laxman@123","user_name2":"Narayana","user_name3":"Nikitha",}
user_name=input("enter the user_name:")
pass_word=input("enter the password:")
if user_name in a:
    if pass_word==a[user_name]:
        print("perfect")
    else:
        print("invalid password")
else:
    print("invalid username")

#5)Hourglass Star Pattern Input = 5
#*********
# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******
#*********
# a=int(input("enter the range:"))
for i in range(1,a+1):
     for j in range(1,a-i+1):
         print(" ",end='')
     for j in range(1,2*i-1):
         print("*",end='')
     print()
for i in range(a-1,0,-1):
     for j in range(1,a-i+1):
         print(" ",end='')
     for j in range(1,2*i):
         print("*",end='')
     print()

#-----------------------------------------------------------------------------------------------------------------
#1)Add Two Floats and Print Boolean Input two float values. Print True if their sum > 100, else False. [float, bool, input, if-else]
a=float(input("enter num1:"))
b=float(input("enter num2:"))
c=a+b
if c>100:
    print("True")
else:
    print("False")

#2)Reverse List Manually Input a list of integers and reverse it manually (no slicing). [list, loops, index handling]
li=[]
for i in range(0,10):
    a=int(input("enter num:"))
    li.append(a)
print(li)
n=len(li)
for j in range(10//2):
    temp=li[j]
    li[j]=li[10-j-1]
    li[10-j-1]=temp
print(li)

#3)Leap Year Checker (if-elif-else) A year is leap if: Div by 4 and not by 100 or Div by 400 [int, conditionals]
year=int(input("enter"))
if year%4==0:
    if year%100!=0:
        print("leap year")
    else:
        print("not leap year")
else:
    if year%400==0:
        print("leap year")
    else:
        print("not leap year")

#-------------------------------------------------------------------------------------------------------------------------
#1)Simple Calculator Using Operators Input two integers and an operator (+, -, *, /). Perform operation. [int, operators, if-elif-els
one=int(input("enter int num:"))
two=int(input("enter int num:"))
operator=input("select the operator + - * /:")
if operator== '+':
    print(one+two)
if operator== '-':
    print(one-two)
if operator== '*':
    print(one*two)
if operator== '/':
    print(one/two)

#2)Float List: Avg > 60 Check Input N floats. Calculate average and check if > 60. Print True/False. [float, list, loop, bool]
sum=0
li=[ ]
n=int(input("enter the range:"))
for i in range(n):
    a=float(input("enter the number:"))
    li.append(a)
    sum=sum+a
average=sum/n
print(li)
print(average)
print(sum)

#3)Login Attempt Limit with While Loop Give user 3 attempts to enter correct password. Lock account after 3 wrong attempts.
# [while, break, if]
login={"user1":"narayana@123","user2":"laxman@9845","user3":"vijayalatha"}
username=input("enter the username:")
if username in login:
    i=0
    while i<3:
        password=input("enter the password:")
        if password==login[username]:
            print("perfect")
            break
        else:
            i=i+1
            remaining=3-i
            if 3>0:
                print(f"incorrect password{remaining}")
            else:
                print("accout lock")

#4)Pascal Triangle Full Pattern Input = 5 Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
for i in range(0,5):
    for j in range(0,5-i-1):
        print(end='')
    a=1
    for j in range(i+1):
        print(a,end='')
        a=a*(i-j)//(j+1)
    print( )
#--------------------------------------------------------------------------------------------------------------------------
#1)Area Calculator for Circle or Square Input shape type (circle or square) and compute area.
# [if-elif-else, float, operators]
a=input("select area of circle or square to calculate:")
if a=='circle':
    r=float(input("enter the value:"))
    A=22/7 * r**2
    print(A)
elif a=='square':
    s=float(input("enter the value:"))
    A=s**2
    print(A)
else:
    print("invalid")

# #2)List Intersection Without `\ Input two lists, print common elements without using set`.[list, loops, conditionals]
a=[]
b=[]
c=[]
range1=int(input("enter the range for a:"))
range2=int(input("enter the range for b:"))
for i in range(range1):
    c1=int(input("enter the number:"))
    a.append(c1)
print(a)
for j in range(range2):
    c2=int(input("enter the number:"))
    b.append(c2)
print(b)
for k in range(len(a)):
    for j in range(len(b)):
        if a[k] == b[j]:
            c.append(a[k])
print(c)


#3)Temperature Alert System (Nested If) Input temperature and humidity:If temp > 40: If humidity > 60 → “Hot & Humid”  Else → “Only Hot”
temp=int(input("enter the temp:"))
humidity=int(input("enter the humidity:"))
if temp>40:
    if humidity>60:
        print("hot and humidity")
    else:
        print("only hot")
else:
    print("no hot and humidity")

# 5. Double-sided Arrow Pattern Input: 5 Output:
#        1
#      2 1 2
#    3 2 1 2 3
#  4 3 2 1 2 3 4
#5 4 3 2 1 2 3 4 5

for i in range(1,5+1):
    for j in range(5-i):
        print(" ",end='')
    for j in range(i,0,-1):#left side
        print(j,end='')
    for j in range(2, i + 1):#right side
        print(j, end='')
    print( )

