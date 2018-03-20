#julia golder
#3/20/18
#quiz2.py

word1 = input('Enter a word')
word2 = input('Enter a word')

length1 = int(len(word1))
length2 = int(len(word2))

if length1 == length2:
    print('The words are the same length!')
elif length1 > length2:
    print('The first word is longer')
else:
    print('The second word is longer')

if 'P' in word1 and word2 or 'p' in word1 and word2:
    print('Both words contain P')
elif 'P' in word1 or 'p' in word1:
    print('p is in the first word')
elif 'P' in word2 or 'p' in word2:
    print('p is in the second word')
else:
    ('Neither word has p')
    
print('Enter 2 numbers that add up to 12')

num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

if num1 + num2:
    print('This adds up to 12!')
else:
    ('This does not add up to 12')
