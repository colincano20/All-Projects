import random

def bridgeQuiz():
    score = 0
    questions = 6
    Q1 = input("Do you like to play baseball? (yes/no): ").lower()
    if Q1 == 'yes':
        score += 1
        Q1yes = input("Do you like basketball? (yes/no):").lower()
        if Q1yes == 'yes':
           score +=1
    elif Q1 == 'no':
        Q1no = input("Do you like MLB The Show? (yes/no):").lower()
        if Q1no == 'yes':
            score += 1
    Q2 = input("Do you like the Iowa Hawkeyes? (yes/no)").lower()
    if Q2 == 'yes':
        score += 1
        Q2yes = input("Do you like the Chicago Cubs? (yes/no)").lower()
        if Q2yes == 'yes':
            score += 1
    elif Q2 == 'no':
        Q2no = input("Do you like the Phoenix Suns? (yes/no)").lower()
        if Q2no == 'yes':
            score += 1
    Q3 = input("Do you like Minecraft? (yes/no)").lower()
    if Q3 == 'yes':
        score += 1
        Q3yes = input("Do you like CFB 25? (yes/no)").lower()
        if Q3yes == 'yes':
            score += 1
    elif Q3 == 'no':
        Q3no = input("Do you Grand Theft Auto 5? (yes/no)").lower()
        if Q3no == 'yes':
            score += 1
    

    #final score and message
    if score / questions == 1:
        print("Congrats, you got a perfect score of", score)
    elif score / questions >= .5:
        print("You have some room to improve, but you still got a score of", score)
    elif score / questions < .5:
        print("You did bad.... you got a score of", score)
    


'''
add more questions,, add more functions that interconnect.
'''

    
bridgeQuiz()