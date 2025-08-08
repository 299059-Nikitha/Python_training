# Write a function called is_prime, which checks if a number is prime.
import math
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i==0:
            return 0
        return 1
a=int(input("enter the num:"))
if is_prime(a)==1:
    print("prime")
else:
    print("not prime")

# Write a functions which checks if all items are unique in the list.
flag=1
def check(n):
    for i in n:
        if n.count(i)!=1:
            return 0
    return 1
li=[1,2,3,4,5,1]
if check(li)==1:
    print("unique")
else:
    print("duplicate is present")

# Write a function which checks if all the items of the list are of the same data type.
def check_all(items):
    first= items[0]
    for i in items:
        if not isinstance(i, type(first)):
            return 0
    return 1
li = ['Nikitha', 1, 2, 'Narayana']
if check_all(li) == 1:
    print("same data type")
else:
    print("different")

# Write a function which check if provided variable is a valid python variable
def variable(a):
    if a[0]>='A' and a[0]<='Z' or a[0]>='a' and a[0]<='z' or a[0]=='_':
        return 1
    return 0
a="1Nikitha"
if variable(a)==1:
    print("valid variable")
else:
    print("invalid variable")