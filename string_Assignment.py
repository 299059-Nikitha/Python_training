# # Write a Python program that takes a string and removes all vowels.
a=list("Nikitha")
for i in a:
    if i in 'aeiouAEIOU':
        a.remove(i)
print(a)

# Given a string, write a program to count the frequency of each character.
a='Nikitha'
fre={ }
for ele in a:
    if ele in fre:
        fre[ele]=fre[ele]+1
    else:
        fre[ele]=1
print(fre)

# Write code to reverse the order of words in a sentence, without using built-in reverse functions
b='Nikitha is good girl'
for i in range(len(b)):
    a=b[i-len(b)-1::-1]
print(a)

# Write a program to check if a string is a palindrome, ignoring spaces and punctuation,
a="Nikitha"
if a is a[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

# Write code to convert a string so that the first letter of each word is capitalized (like title case), without using .
# with out using Title()
a='nikitha is good girl'
b=' '
for i in range(len(a)):
    if i==0 or a[i-1]==' ' :
        b=b+a[i].upper()
    else:
        b = b + a[i]
print(b)
