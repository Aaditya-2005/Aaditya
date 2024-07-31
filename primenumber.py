num = range(1, 100)
counter = 0
for i in num:
    for b in range(1, 100):
        if (i % b == 0):
            counter += 1
    if (counter == 2):
        print(i, "is a prime number")
    else:
        print(i, "is not a prime number ")
    counter = 0


