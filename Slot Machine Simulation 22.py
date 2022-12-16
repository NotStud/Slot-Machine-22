import random

money = int(input('Enter the amount of Money you want to gamble (Whole Value): '))
win = 0
play ='y'
win = 0

while play == 'y':
    num1 = random.randint(0,5)
    num2 = random.randint(0,5)
    num3 = random.randint(0,5)

    if num1 == 0:
        print('Cherries')
    elif num1 == 1:
        print('Oranges')
    elif num1 == 2:
        print('Plums')
    elif num1 == 3:
        print('Bells')
    elif num1 == 4:
        print('Melons')
    elif num1 == 5:
        print('Bars')

    if num2 == 0:
        print('Cherries')
    elif num2 == 1:
        print('Oranges')
    elif num2 == 2:
        print('Plums')
    elif num2 == 3:
        print('Bells')
    elif num2 == 4:
        print('Melons')
    elif num2 == 5:
        print('Bars')

    if num3 == 0:
        print('Cherries')
    elif num3 == 1:
        print('Oranges')
    elif num3 == 2:
        print('Plums')
    elif num3 == 3:
        print('Bells')
    elif num3 == 4:
        print('Melons')
    elif num3 == 5:
        print('Bars')

    if num1 == num2 == num3:
        print('Congrats! You won 3 times your bet!')
        win =+ (money * 3)
        play = input('Would you like to play again? (y or n): ')
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print('You have won twice your amount')
        win =+ (money * 2)
        play = input('Would you like to play again? (y or n): ')

    else:
        print('Aww man! You lost!')
        win = (money - money) 
        play = input('Would you like to play again? (y or n): ')

print('Your final total is:', win)
