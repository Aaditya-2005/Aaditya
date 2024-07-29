#Write a Python program that removes all negative numbers from a list and returns a new list containing only non-negative numbers.
a=int(input("enter amount of entries:"))
total_entries=range(0,a)
list1=[]
list_original=[]
for b in total_entries:
    x=int(input("enter a number: "))
    list1.append(x)
print(list1)
for m in list1:
    if(m>0):
        list_original.append(m)
print(list_original)



