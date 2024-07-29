#Write a Python program that creates a new list containing only the odd numbers from a given list of numbers.
a=int(input("enter the number of entries"))
total_entries=range(0, a)
list=[]
list2=[]
for i in total_entries:
    entry=int(input("enter entries:"))
    list.append(entry)
print(list)
for x in list:
    if (x%2!=0) :
        list2.append(x)
print(list2)
