
#juliagolder
#1/29/18
#movie.py - how to calculate what movie you can watch

num = float(input('Enter your age: '))

if num >= 17:
    print(num, 'You can watch: R')
elif num >= 13:
    print(num, 'You can watch: PG-13')
elif num >= 10:
    print(num, 'You can watch: PG')
else:
    print(num, 'You can watch: G!')