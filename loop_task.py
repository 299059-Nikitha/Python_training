#Iterate 0 to 10 using for loop, do the same using while loop.
for a in range(11):
    print(a)

#Iterate 10 to 0 using for loop, do the same using while loop.
b=10
while(b>=0):
    print(b)
    b=b-1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(7):
    for j in range(7):
        print("# ",end=' ')
    print()

#Print the following pattern using loops
for i in range(11):
    print(f"{i} X {i}={i*i}")


#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2==0:
        print(i)


#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i%2!=0:
        print(i)


#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum=0
for i in range(101):
    sum = sum + i
print(sum)


#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even=0
odd=0
for i in range(101):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print(f"sum of even is {even} and sum of odd {odd}")

#Iterate through the list, ['Python', 'Numpy','Pandas','Scikit', 'Pytorch'] using a for loop and print out the items.
#Use for loop to iterate from 0 t

a=['Python', 'Numpy','Pandas','Scikit', 'Pytorch']
for i in a:
    print(i)
    
#Use nested loops to create the following:
a=int(input("enter the range:"))
for i in range(a):
    for j in range(a-i):
        print(sep=" ")
    for j in range(2*i+1):
        print("#",end=" ")
    print()
