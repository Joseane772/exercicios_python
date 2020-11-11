import random
n = random.randint(1, 10)
nog = 0
p = input("hello, what's your name?")
print("Okay!\n "+p+" I am guessing a number between 1 and 10:")
while nog < 5:
    g = int(input())
    nog += 1
    if g < n:
        print('your guess is too low')
    if g > n:
        print('your guess is too high')
    if g == n:
        break
if g == n:
    print('yay! You guessed the number in ' + str(n) + ' tries')
else:
    print('OH! You did not guess the correct number, the number was' + str(nog))
