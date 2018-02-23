#julia golder
#2/23/18
#fortuneTeller.py

color = input('Pick red or blue: ')
number = int(input('Pick a number from 1 - 4: '))

if color == 'red' and number == 1:
    print('')
elif color == 'red' and number == 2:
    print('')
elif color == 'blue' and number == 3:
    print('')
elif color == 'red' and number == 2:
    print('')
elif color == 'red' and number == 1:
    print('Youll recieve something you werent expecting')
elif color == 'blue' and number == 2:
    print('Today will be your most stressful day')
elif color == 'blue' and number == 4:
    print('Today will be your best day ever')
else:
    print('Try again later')