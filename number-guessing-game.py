import random
secret_number = random.randint(1,100)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
""")
level = {
    1 : 10,
    2 : 5,
    3 : 3
}
dificulty = int(input('Enter your choice > '))
if dificulty not in level.keys():
    print('Choose from 1 (Easy), 2 (Medium) or 3 (Hard)')
else:
    print(f"Great! You have selected the {dificulty} difficulty level. Let's start the game!")
    count = 0
    for guesses_taken in range(level[dificulty]):
        guess = int(input('Enter your guess > '))
        count +=1
        if guess < secret_number:
            print('Incorrect! Your guess is too low.')
        elif guess > secret_number:
            print('Incorrect! Your guess is too high.')
        else:
            break
if guess == secret_number:
    print('Good job! You got it in '+str(count)+' guesses.')
else:
    print('Nope. The number was '+str(secret_number)+'.')