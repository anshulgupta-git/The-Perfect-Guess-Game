import random

n=random.randint(1,100)
a=0
guesses=0

while a!=n:
    a=int(input("Enter your guess: "))
    guesses=guesses+1
    if a>n:
        print("Too high! Try again.")
    elif a<n:
        print("Too low! Try again.")
    
print("Congratulations! You guessed the number.")
print(f"It took you {guesses} guesses.")