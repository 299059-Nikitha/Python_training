#Create list called "even", store all the even numbers, in the range of 1 to 20.
even=[]
for i in range(1,21):
    if i%2==0:
        even.append(i)
print(even)

#Create list called "odd", store all the odd numbers, int the range of 1,20.
odd=[]
for j in range(1,21):
    if j%2!=0:
        odd.append(j)
print(odd)

#Take "even" and "odd" list  from previous solution, merge it in new list called "numbers" and sort it.
numbers=even+odd
print(numbers)
numbers.sort()
print(numbers)

#Create a nested list for called "Students" for 5 student, each index store the student information. ex.. ["name",roll,marks].
Students=[["Laxman",1,100],["Vijetha",17,90],["Pooja",4,80],["Ankitha",22,96],["Manjunath",7,86]]

#Write a Python program to find the second largest number in a list.
li=[2,5,6,7,8,9,10]
li.sort()
print(li[5])

#Given a tuple of numbers, find the max and min elements.
tup = (11,26,45,23,15,18)
print(f"max {max(tup)}")
print(f"max {min(tup)}")

#retrieve the 'G' from following list using positive indexing
L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]
print(L1[3][2][2][1][1])

#WAP to retrieve the 'Sweet' string from the following nested list using Positive indexing
L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]
print(L2[1][2][1][2])

#WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
s2 = "Hello I am going to Bengaluru How are you doing?"
print(s2[-19:-29:-1])

#WAP to print unique element from list.
nums = [4,3,5,6,3,4,6]
for i in nums:
    flag = 0
    for j in nums:
        if j==i:
            flag=1
            break
if flag==0:
    print(i)



