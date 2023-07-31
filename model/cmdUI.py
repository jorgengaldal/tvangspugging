"""
For testing purposes
"""

from getRandomQuestion import getQuestion

while True:
    questionObject = getQuestion()
    if questionObject["type"] != "text":
        continue

    guess = input(questionObject["question"] + " ")

    # Also takes care of if caseSensitive
    if ((not questionObject["caseSensitive"] and guess in questionObject["acceptedAnswers"]) or
            (guess.lower() in (x.lower() for x in questionObject["acceptedAnswers"]))):
        print("Correct answer!")
    else:
        print("Wrong answer!")
