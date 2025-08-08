"""Area of a circle is calculated as follows: area = π x r x r and perimeter = 2 x π x r.
Write a function that calculates area_of_circle and perimeter_of_circle."""
def area_of_circle(r):
    pi=22/7
    ar=pi * r * r
    return ar
def perimeter_of_circle(r):
    pi=22/7
    peri = 2*pi*r
    return peri
area=int(input("enter the radius:"))
print(area_of_circle(area))
perimeter=int(input("enter the radius"))
print(perimeter_of_circle(perimeter))

"""Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
Check if all the list items are number types. If not do give a reasonable feedback."""
def add_all_nums(li):
    sum=0
    for i in li:
        if isinstance(i,(int,float)):
            sum=sum + i
        else:
            return 'error in ur list'
    return sum
li=[1,2,3,4,5]
print(add_all_nums(li))
li1=[1,'nikitha']
print(add_all_nums(li1))

"""Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
Write a function which converts °C to °F, convert_celsius_2_fahrenheit."""
def convert_celsius_2_fahrenheit(C):
    F = (C * 9 / 5) + 32
    return F
C=int(input("enter the celsius:"))
print(convert_celsius_2_fahrenheit(C))

"""Write a function called check_season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer."""
def check_seson(month):
    if month == 'december' or 'january' or 'february':
        return 'winter'
    if month == 'march' or 'april' or 'may':
        return 'spring'
    if month =='june' or 'jul' or 'august':
        return 'summer'
    if month == 'september' or'october' or 'november':
        return 'Autum'
month=input("enter the month:").lower()
print(check_seson(month))

"""Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list."""
def print_list(li):
    for i in li:
        print(i,end=' ')
    print()
li=[1,2,3,4,5,6,7,8,9,0]
print_list(li)

"""Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)."""
def reverse_list(li):
    n=len(li)-1
    for i in range(n//2):
        temp=li[i]
        li[i]=li[n-i]
        li[n-i]=temp
    return li
li=['Narayana','Laxman','vijayalatha']
print(reverse_list(li))

"""print(reverse_list([1, 2, 3, 4, 5])) #[5, 4, 3, 2, 1] print(reverse_list1(["A", "B", "C"])) #["C", "B", "A"]"""
def reverse_list(li):
    n=li[::-1]
    return n
li1=[1,2,3,4,5]
print(reverse_list(li1))
li2=['A','B','C']
print(reverse_list(li2))

"""Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items"""
def capitalize_list_items(items):
    li1= []
    for i in items:
        if i.islower():
            li1.append(i.upper())
        else:
            li1.append(i)
    return li1
b = ['laxman', 'narayana', 'nikitha', 'vijayalatha', 'manju', 'pooja']
print(capitalize_list_items(b))

"""Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end"""
def add_item(li):
    li.append(5)
    return li
li=[1,2,3,4]
print(add_item(li))

"""food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'] print(add_item(food_staff, 'Fungi'))
 ['Potato', 'Tomato', 'Mango', 'Milk', 'Fungi'] numbers = [2, 3, 7, 9] print(add_item(numbers, 5)) #[2, 3, 7, 9, 5]"""
def add_item(li1,add):
    li1.append(add)
    return li1
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff,'Fungi'))
numbers = [2, 3, 7, 9]
print(add_item(numbers,5))

"""Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'] print(remove_item(food_staff, 'Mango')) # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9] print(remove_item(numbers, 3)) # [2, 7, 9]"""
def remove_item(li1,remov):
    li1.remove(remov)
    return remov
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
remove_item(food_staff,'Mango')
print(food_staff)
numbers = [2, 3, 7, 9]
remove_item(numbers,3)
print(numbers)

"""Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5)) # 15 print(sum_all_numbers(10)) # 55 print(sum_all_numbers(100)) # 5050"""
def sum_of_numbers(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum
def sum_all_numbers(n1):
    sum=0
    for i in range(n1+1):
        sum=sum+i
    return sum
print(sum_of_numbers(5))
print(sum_all_numbers(10))
print(sum_all_numbers(100))

"""Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range."""
def sum_of_odd(n):
    sum=0
    for i in range(n):
        if i%2!=0:
            sum=sum+i
    return sum
n=int(input("enter the range:"))
print(sum_of_odd(n))

"""Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range"""
def sum_of_even(n):
    sum1=0
    for i in range(n):
        if i%2==0:
            sum1=sum1+i
    return sum1
n=int(input("enter the range:"))

print(sum_of_even(n))
