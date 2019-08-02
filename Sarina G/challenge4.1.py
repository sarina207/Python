def car_speed(speed):
    if speed < 70:
        print('ok')
    else:
        b = 0
        points = 0
        c = speed-70
        d = 0
        while d < c:
            b += 1
            d += 1
            if b == 5:
                points += 1
                b = 0
        if points >= 12:
            print('license suspended')
        else:
            print('bad bad bad')
x = int(input('enter your car speed'))
car_speed(x)
