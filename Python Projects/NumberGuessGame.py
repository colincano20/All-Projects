import random  # Importing random module at the top

def friendColin(name=None):
    if name:
        print(f'\nWelcome back, {name}!')
    else:
        name = input('What is your name? ')
        print('Nice to meet you ' + name)
    return name  # Return the name for use in the main loop

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    guessUser = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < guessUser:
                print("Too low! Try again.")
            elif guess > guessUser:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number {guessUser} in {attempts} attempts.")
                return attempts  # Return the number of attempts

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

def avgGuess(total_attempts, games_played):
    if games_played == 0:  # To avoid division by zero
        return 0
    return total_attempts / games_played  # Calculate average attempts

# Run the functions
if __name__ == "__main__":
    total_attempts = 0
    games_played = 0
    name = None

    while True:
        name = friendColin(name)
        attempts = guessing_game()  # Get the attempts from the game
        total_attempts += attempts  # Add to total attempts
        games_played += 1  
        
        average = avgGuess(total_attempts, games_played)  # Calculate average guesses
        

        again = input("Would you like to play again? (yes/no): ").lower()
        if again != 'yes':
            print(f"Your average attempts per game was: {average:.2f}")
            break
