def factors(x):
    a = []
    for i in range(1, x+1):
        if x%i == 0:
            a.append(i)
    print(a)

x = int(input('enter a number'))
factors(x)
