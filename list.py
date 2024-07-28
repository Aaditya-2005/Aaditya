#Write a Python program that creates a list of numbers from 1 to 10,
#then uses a for loop to create a new list with the squares of those numbers answer of this
lisp = []
lisp2 = []
oddlisp=[]
nu = range(0, 11)
for x in nu:
    lisp.append(x)
print(lisp)
for x in nu:
    lisp2.append(x)
print(lisp2)
for x in lisp2:
    if (x%2!=0):
        oddlisp.append(x)
print(oddlisp)











