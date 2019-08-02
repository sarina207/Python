import random

def seven_of_five():
    a = []
    b = 0
    c = []
    for x in range(1, 100):
        if x%5 == 0:
            a.append(x)
    a.sort()
    while b < 7:
        c.append(random.choice(a))
        b += 1
    print(c)

seven_of_five()
