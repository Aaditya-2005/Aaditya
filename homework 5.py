a=int(input("Enter number of entries"))
total_entries=range(0,a)
list=[]
for i in total_entries:
    entry=int(input("enter entries:"))
    list.append(entry)
print(list)
list.reverse()
print(list)