def fizz_buzz(x):
    if x%3 == 0 and x%5 == 0:
        print('fizzbuzz')
    elif x%3 == 0:
        print('fizz')
    elif x%5 == 0:
        print('buzz')
    else:
        print(x)
x = int(input('enter a number'))
fizz_buzz(x)
