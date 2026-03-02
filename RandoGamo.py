import random as r

num1 = int(input("Let's play a guessing game\nEnter lower bound: "))
num2 = int(input('Enter upper bound: '))

secret = r.randint(num1, num2)

while True:
    guess = int(input('Enter your guess: '))
    if guess == secret:
        print('Congrats! You Win!!')
        break
    else:
        print('Guess again')
