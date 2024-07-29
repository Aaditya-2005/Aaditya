#Write a Python program that finds the maximum and minimum values in a list of numbers.
maximum=0
minimum=0
mist=[]
a=int(input("enter number of entries:"))
total_entries= range(0,a)
for i in total_entries:
    entry=int(input('ENTER A  NUMBER:'))
    mist.append(entry)
print(mist)

print(min(mist),("min"))
print(max(mist),("max"))

