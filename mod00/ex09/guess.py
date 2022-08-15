import random


if __name__ == '__main__':
    print('This is an interactive guessing game!')
    print('You have to enter a number between 1 and 99 to find out the secret number.')
    print("Type 'exit' to end the game.")
    print('Good luck!\n')
    attempts = 0
    n = random.randint(1, 99)
    while True:
        x = input("What's your guess between 1 and 99?\n>> ")
        attempts += 1
        if x == 'exit':
            print('Goodbye!')
            break
        try:
            try:
                x = int(x)
                nb = True
            except Exception:
                nb = False
            assert nb, "That's not a number."
            if x > n:
                print("Too high!")
            elif x < n:
                print("Too low!")
            else:
                if n == 42:
                    print('The answer to the ultimate question of life,', end=' ')
                    print('the universe and everything is 42.')
                if attempts == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!")
                    print('You won in', attempts, 'attempts!')
                break
        except AssertionError as msg:
            print(msg)
