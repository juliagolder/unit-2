#julia golder
#2/23/18
#fortuneTeller.py

color = input('Pick red or blue: ')
number = int(input('Pick a number from 1 - 4: '))

if color == 'red' and number == 1:
    print('You will find something lucky in the next week')
elif color == 'red' and number == 2:
    print('You wont live your longest life')
elif color == 'blue' and number == 3:
    print('YOURE GETTING A SURPRISE!')
elif color == 'red' and number == 2:
    print('Your life will carry on the same')
elif color == 'red' and number == 1:
    print('Youll recieve something you werent expecting')
elif color == 'blue' and number == 2:
    print('Today will be your most stressful day')
elif color == 'blue' and number == 4:
    print('Today will be your best day ever')
else:
    print('Try again later :(')