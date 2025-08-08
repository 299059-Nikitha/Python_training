"""Declare a function named evens_and_odds. It takes a positive integer as parameter and
it counts number of evens and odds in the number."""
def even_add_odd(num):
    even=0
    odd=0
    for i in range(num+1):
        if i%2==0:
            even=even+i
        else:
            odd=odd+i
    return even,odd
n=int(input("enter the range:"))
print("even and odd count:",even_add_odd(n))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fac=1
    while(num!=0):
        fac=fac*num
        num=num-1
    return fac
n=int(input("enter the number"))
if n==0:
    print("cannot be factoried")
else:
    print(factorial(n))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    if value == None :
        return True
    else:
        return False
a=[]
print(is_empty(a))

# Write different functions which take lists.They should calculate_mean, calculate_median,
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(li):
    sum=0
    n=len(li)
    for i in li:
        sum=sum+i
    div=sum/n
    return div
def  calculate_median(li):
    n=len(li)
    li1=sorted(li)
    print(li1)
    if n%2!=0:
        return li1[(len(li)//2)]
    if n%2==0:
        return li1[(n//2)-1 : n//2+1]
def calculate_mode(li):
    di={}
    for i in li:
        di[i]=li.count(i)
    return di
def calculate_range(li):
    range=max(li)-min(li)
    return range
import math
def calculate_variance(li):
    sum=0
    li1=[]
    i_square_add=0
    n=len(li)
    for i in li:
        sum=sum+i
    print(sum)
    div1=sum/n
    print(div1)
    for i in li:
        i_div=i-div1
        li1.append(i_div)
    print(li1)
    for j in li1:
        i_square=j**2
        i_square_add=i_square_add+i_square
    print(i_square_add)
    variance=i_square_add/n-1
    return math.sqrt(variance)
import math
def calculate_std(li):
    n=len(li)
    sum=0
    square=0
    for i in li:
        sum=sum+i
    div=sum/5
    for i in li:
        square=square+(i-div)**2
    s=square/n-1

    return math.sqrt(s)

li=[7,5,4,3,1,8,0,2,1,9]
li1=[82,93,98,89,89]
print(calculate_median(li))
print(calculate_mode(li))
print(calculate_range(li))
print(calculate_variance(li))
print(calculate_std(li))
print(calculate_std(li1))