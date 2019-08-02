def prime(x):
    b = 0
    for y in range(1, x+1):
        if x%y == 0:
            b += 1
    if b == 2:
        print('yes')
    else:
        print('no')

x = int(input('enter a number')) 

prime(x)
