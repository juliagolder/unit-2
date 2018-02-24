#Julia golder
#2/24/18
#adventure.py


print('A bear is chasing you')
print('You come to a river')
choice1 = input('Do you jump in the river?')

if choice1 == 'y' or choice1 == 'yes':
    print('Yay! You know how to swim')
    print('Wait theres a giant fish coming!!')
    choice2 = input('Do you try to fight off the fish')
    
    if choice2 == 'yes':
        print('You couldnt fight off the fish, and youre dead')
    else:
        print('Good choice! You out swam the fish')
        print('Looking back at the fish, there was a shark in front of you and now youre dead')
else:
    print('You keep running and you find a bridge!')