import requests
import random
import html

url = 'https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple'

def get_question():
    response = requests.get(url)
    data = response.json()
    fetch_question = data['results'][0]['question']
    question = html.unescape(fetch_question)
    return question, data

def get_options(data):
    correct_answer = data['results'][0]['correct_answer']
    incorrect_answers = list(data['results'][0]['incorrect_answers'])
    multiple_choice = incorrect_answers + [correct_answer]
    random.shuffle(multiple_choice)
    letters = ['A', 'B', 'C', 'D']
    options = dict(zip(letters, multiple_choice))
    return options, correct_answer

def display(question, options):
    print(f"{question} Choose A, B, C or D {options}")

def choose_answer():
    user_answer = input(f"Which answer is correct? (A, B, C or D)").upper()
    return user_answer

def check_answer(user_answer, correct_answer, options):
    if options[user_answer] == correct_answer:
        print("Correct!")
    else:
        print(f"False! The correct answer is: {correct_answer}")

questions_answered = 0
score = 0

def update(score, questions_answered, user_answer, correct_answer, options):
    if options[user_answer] == correct_answer:
        questions_answered += 1
        score += 1
        return score, questions_answered
    else:
        questions_answered += 1
        return score, questions_answered

name = input(f"Welcome to Triviant, please enter your name: ")
print(f"Hello {name}, you will get 5 questions. Can you get them all right? Good luck!")

while questions_answered < 5:
    question, data = get_question()
    options, correct_answer = get_options(data)
    display(question, options)
    user_answer = choose_answer()
    check_answer(user_answer, correct_answer, options)
    score, questions_answered = update(score, questions_answered, user_answer, correct_answer, options)
    print(f"Your score is: {score} out of {questions_answered}")

print(f"Thank you for playing Triviant, {name}. See you next time!")