def new_game():
    guesses = []
    question_nu = 1
    correct_answer = 0


    for key in questions:
        print(key)
        print("--------------")
        for i in options[question_nu-1]:
            print(i)

        print("--------------")
        guess = input("Type Answer(A/B/C/D): ").upper()
        guesses.append(guess)

        correct_answer += check_answer(questions.get(key), guess)

        question_nu += 1
    display_score(correct_answer, guesses)
def check_answer(answers, guess):
    if answers == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
def display_score(correct_answer, guesses):
    print("--------------")
    print("RESULTS")
    print("--------------")
    print("Answers: ", end="")
    for key in questions:
        print(questions.get(key), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    print("--------------")

    score = int((correct_answer/len(questions))*100)
    print("You Scored: "+str(score)+"%")
    print("--------------")
def play_again():
    resume = input("Wanna Play again?(type YES or NO): ")
    if resume == "YES":
        return True
    else:
        return False

questions = {"Who has won the most driver championships?": "D",
             "Who has the longest streak of race wins?": "B",
             "Who has the most pole positions?": "A",
             "Who has the most race starts without a win?": "B"}

options = [["A. Schumacher", "B. Hamilton", "C. Vettel", "D. Both A & B"],
           ["A. Vettel", "B. Verstappen", "C. Hamilton", "D. Schumacher"],
           ["A. Hamilton", "B. Schumacher", "C. Verstappen", "D. Vettel"],
           ["A. Norris", "B. Magnussen", "C. Grosjean", "D. Stroll"]]

new_game()

while play_again():
    new_game()
print("--------------")

print("Lame Jackass Loser")