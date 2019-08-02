def modulus(a, b)
    print(a%b)
def addition(a, b):
    print(a + b)
def multiplication(a, b):
    print(a*b)
def division(a, b):
    print(a/b)
def subtraction(a, b):
    print(a-b)
def factors(x):
    a = []
    for i in range(1, x+1):
        if x%i == 0:
            a.append(i)
    print(a)

print('welcome to the calculator!! what would you like to calculate?')
choose = input('modulus(m), addition(+), multiplication(*), division(/), subtraction(-), or see all factors(&)')
if choose == 'm':
    sca
