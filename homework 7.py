#Write a Python program that calculates the sum of only the positive numbers in a list.

a=int(input("enter amount of entries:"))
total_entries=range(0,a)
list1=[]
list_original=[]
sum=0
for b in total_entries:
    x=int(input("enter a number: "))
    list1.append(x)
print(list1)
for m in list1:
    if(m>0):
        list_original.append(m)
        sum= sum+ m
print(sum)