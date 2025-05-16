"""
For testing purposes
"""

from tvangspugging.model.getRandomQuestion import getQuestion

failed_attempts = 0
while True:
    questionObject = getQuestion()
    if questionObject["type"] != "text":
        failed_attempts += 1
        if failed_attempts >= 100:
            break
        continue

    guess = input(questionObject["question"] + " ")

    # Also takes care of if caseSensitive
    if ((not questionObject["caseSensitive"] and guess in questionObject["acceptedAnswers"]) or
            (guess.lower() in (x.lower() for x in questionObject["acceptedAnswers"]))):
        print("Correct answer!")
    else:
        print("Wrong answer!")
        print("Correct answer is " + str(questionObject["acceptedAnswers"]))
