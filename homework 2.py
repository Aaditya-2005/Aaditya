#Write a Python program that takes a list of numbers and counts how many of them are even and how many are odd.
oddsum=0
evensum=0
list1=[]
a=int(input("enter total entries:"))
numbers=range(0,a)
for i in numbers :
    entry=int(input("enter total entries"))
    list1.append(entry)
print(list1)
if (entry%2==0):
    evensum= evensum+entry
else:
    oddsum=oddsum+entry
    print(oddsum,"odd")
    print(evensum,"even")

