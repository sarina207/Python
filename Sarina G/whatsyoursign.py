print('welcome to the sarina HoroscopeGen!')
name = input('please enter your name')
month = int(input('please enter your birth month (i.e. 12 for december, 5 for may'))
date = int(input('please enter your birth date i.e. 1, 12, 27'))
print('generating your horoscope sign')
if month == 3 and date >= 21 or month == 4 and date <= 20:
    print('you are an aries!')
    print('you need to pay taxes to sarina to stay in your house. approach her with $5 or more.')

elif month == 4 and date >= 21 or month == 5 and date <= 21:
    print('you are a taurus!')
    print('you need to pay taxes to sarina to stay in your house. approach her with $5 or more.')

elif month == 5 and date >= 22 or month == 6 and date <= 20:
    print('you are a gemini!')
    print('you are okay awesome. you\'re also a loyal friend and people like you for your clumsiness as well.')

elif month == 6 and date >= 22 or month == 7 and date <= 22:
    print('you are a cancer!')
    print('you need to pay taxes to sarina to stay in your house. approach her with $5 or more.')

elif month == 7 and date >= 23 or month == 8 and date <= 21:
    print('you are an leo!')
    print('you are fairly awesome. no taxes for the next two years.')

elif month == 8 and date >= 22 or month == 9 and date <= 23:
    print('you are a virgo!')
    print('you need to pay taxes to sarina to stay in your house. approach her with $5 or more.')

elif month == 9 and date >= 24 or month == 10 and date <= 23:
    print('you are a libra!')
    print('you are fairly awesome. no taxes for the next two years.')

elif month == 10 and date >= 24 or month == 11 and date <= 22:
    print('you are a scorpio!')
    if name == 'chloe':
        print('you are fairly awesome. no taxes for the next two years.')
    else:
        print('you need to pay taxes to sarina to stay in your house. approach her with $5 or more.')

elif month == 11 and date >= 23 or month == 12 and date <= 22:
    print('you are a sagittarius!')
    print('you are the best of the best. don\'t even bother paying for your house:  you\'ve earned it.')

elif month == 12 and date >= 23 or month == 1 and date <= 20:
    print('you are a capricorn!')
    print('you need to pay taxes to sarina to stay in your house. approach her with $5 or more.')

elif month == 1 and date >= 21 or month == 2 and date <= 19:
    print('you are an aquarius!')
    if name == 'neige':
        print('you are the best of the best. you are an endearing friend and people love you. don\'t bother paying taxes for the next 5 years.')        
    else:
        print('you need to pay taxes to sarina to stay in your house. approach her with $5 or more.')

elif month == 2 and date >= 20 or month == 3 and date <= 20:
    print('you are a pisces!')
    if name[0] == 'v':
        print('you are fierce and are a clear frenemy. you don\'t have to pay taxes but watch out for sarina :)')
    else:
        print('you need to pay taxes to sarina to stay in your house. approach her with $5 or more.')

print('have a wonderful day!')
