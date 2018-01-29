
#julia golder
#1/29/18
#gradeCalculator.py - how to calculate your letter grade

num = float(input('Enter a number: '))

if num >= 90:
    print(num, 'you earned an A')
elif num >= 80:
    print(num, 'you earned a B')
elif num >= 70:
    print(num, 'you earned an C')
elif num >= 60:
    print(num, 'you earned an D')
else:
    print(num, 'is NC')
