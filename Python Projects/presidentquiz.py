from random import randint

def quiz():
    D = {
        1: "George Washington", 2: "John Adams", 3: "Thomas Jefferson", 4: "James Madison",
        5: "James Monroe", 6: "John Quincy Adams", 7: "Andrew Jackson", 8: "Martin Van Buren",
        9: "William Henry Harrison", 10: "John Tyler", 11: "James Polk", 12: "Zachary Taylor",
        13: "Millard Fillmore", 14: "Franklin Pierce", 15: "James Buchanan", 16: "Abraham Lincoln",
        17: "Andrew Johnson", 18: "Ulysses Grant", 19: "Rutherford Hayes", 20: "James Garfield",
        21: "Chester Arthur", 22: "Grover Cleveland", 23: "Benjamin Harrison", 24: "Grover Cleveland*",
        25: "William McKinley", 26: "Theodore Roosevelt", 27: "William Howard Taft", 28: "Woodrow Wilson",
        29: "Warren Harding", 30: "Calvin Coolidge", 31: "Herbert Hoover", 32: "Franklin Roosevelt",
        33: "Harry Truman", 34: "Dwight Eisenhower", 35: "John Kennedy", 36: "Lyndon Johnson",
        37: "Richard Nixon", 38: "Gerald Ford", 39: "Jimmy Carter", 40: "Ronald Reagan",
        41: "George Bush", 42: "Bill Clinton", 43: "George Bush", 44: "Barack Obama",
        45: "Donald Trump", 46: "Joe Biden", 47: "Donald Trump*"
    }
    print("Welcome to the President Guessing Game! You will be randomly asked what was the number of a certain president. \nThere will be 5 questions. If you see an *, it means it was their 2nd non-consecutive term.")
    
    # Get a random president number
    random_number = randint(1,47)
    president_name = D[random_number]
    score = 0
    # Ask user for input
    Q1 = input(f"What number president was {president_name} ? ")
    
    # Check if the answer is correct
    if Q1.isdigit() and int(Q1) == random_number:
        print('Yes, that’s correct!')
        score +=1
    else:
        print(f'No, the correct answer is {random_number}.')
    random_number = randint(1,47)
    president_name = D[random_number]

    Q2 = input(f"What number president was {president_name} ? ")
    if Q2.isdigit() and int(Q2) == random_number:
        print('Yes, that’s correct!')
        score +=1
    else:
        print(f'No, the correct answer is {random_number}.')

    random_number = randint(1,47)
    president_name = D[random_number]

    Q3 = input(f"What number president was {president_name} ? ")
    if Q3.isdigit() and int(Q3) == random_number:
        print('Yes, that’s correct!')
        score +=1
    else:
        print(f'No, the correct answer is {random_number}.')
 
    random_number = randint(1,47)
    president_name = D[random_number]

    Q4 = input(f"What number president was {president_name} ? ")
    if Q4.isdigit() and int(Q4) == random_number:
        print('Yes, that’s correct!')
        score +=1
    else:
        print(f'No, the correct answer is {random_number}.')

    random_number = randint(1,47)
    president_name = D[random_number]

    Q5 = input(f"What number president was {president_name} ? ")
    if Q5.isdigit() and int(Q5) == random_number:
        print('Yes, that’s correct!')
        score +=1
    else:
        print(f'No, the correct answer is {random_number}.')
    

    if score == 5:
        print("Wow! You got a perfect score of",score)
    elif score == 4:
        print("Okay good job. You did good with a score of", score)
    elif score == 3:
        print("You did decent.... with a score of",score)
    elif score == 2:
        print("Wow.... really? You only got a score of",score)
    elif score == 1:
        print("You really need to get smarter.... how did you get a score of",score)
    elif score == 0:
        print("Did you skip history class? Embarassing.... you got 0 right....")

    if score >= 3:
        print("You have scored at least 3/5! You have unlocked the next level!")
        # Get a random president number
        random_number = randint(1, 46)
        correct_name = D[random_number]

        # Ask user to guess the president's name based on the number
        print(f"Who was the {random_number}th president?")
        Q1 = input("Enter the president's name: ").strip()

        # Check if the user's guess is correct
        if Q1.lower() == correct_name.lower():
            print("Correct!")
            score +=1
        else:
            print(f"No, the correct answer was {correct_name}.")

        random_number = randint(1, 46)
        correct_name = D[random_number]
        print(f"Who was the {random_number}th president?")
        Q1 = input("Enter the president's name: ").strip()
        if Q1.lower() == correct_name.lower():
            print("Correct!")
            score +=1
        else:
            print(f"No, the correct answer was {correct_name}.")

        random_number = randint(1, 46)
        correct_name = D[random_number]
        print(f"Who was the {random_number}th president?")
        Q1 = input("Enter the president's name: ").strip()
        if Q1.lower() == correct_name.lower():
            print("Correct!")
            score +=1
        else:
            print(f"No, the correct answer was {correct_name}.")
        print(f"Your final score was: {score}")
    else:
        print("I am sorry, but you scored too low to move on...")

    '''
    add section if u get at least 3/5, where u guess president based off number(vise versa essentially)
    '''

quiz()
