import random as r


def set_target() -> int:
    num1 = num2 = None
    print("Let's play a guessing game")
    while True:
        try:
            if num1 is None:
                num1 = int(input("Enter lower bound: "))
            else:
                num2 = int(input('Enter upper bound: '))

            if num1 is not None and num2 is not None:
                break
            else:
                continue
        except ValueError:
            print('Input must be a number')
            continue
    return r.randint(num1, num2)

def set_guess() -> int | None:
    guess = None
    while True:
        try:
            guess = int(input('Enter your guess: '))
            break
        except ValueError:
            print('Input must be a number')
            continue
    return guess

def check_guess(num1: int, num2: int) -> str | None:
    if num1 == num2:
        return 'Congrats!\nYou Win!!!'
    else:
        return check_guess(num1, set_guess())


if __name__ == '__main__':
    print(check_guess(set_target(), set_guess()))