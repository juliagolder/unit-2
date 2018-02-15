
#julia golder
#2/14/18
#unitConverter.py - how to convert units


print('1: kilometers to Miles')
print('2: Kilograms to Pounds')
print('3: Liters to Gallons')
print('4: Celsius to Fahrenheit')
number = int(input('Choose a number: '))


if number == 1:
    celcius = int(input('Enter Degrees in Celcius: '))
    fahrenheit = celcius * 1.8 + 32
    print(celcius,'degrees Celsius is', fahrenheit,'degres in Fahrenheit')
elif number == 3:
    kilograms = int(input('Enter a number of Kilograms: '))
    pounds = kilograms/0.453592
    print(kilograms,'Kilograms is', pounds,'pounds')
elif number == 2:
    liters = int(input('Enter amount in liters: '))
    gallons = liters/3.785411784
    print(liters,'liters is', gallons,' gallons')
elif number == 4:
    kilometers = int(input('Enter a number of Kilometers'))
    miles = kilometers/1.60934
    print(kilometers,'kilometers is', miles,'miles')
else:
    print('Error, number not an option')