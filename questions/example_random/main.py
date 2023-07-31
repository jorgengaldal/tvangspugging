"""
Example: Asks for the solution to a simple math question
"""

from random import randint

QUESTION_FORMAT = "Hva er kvadratet av {num1} pluss {num2}?"


def giveQuestion():
    """
    Should return a tuple of (str: question, list[str]: acceptedAnswers)

    Example: (square of num1) plus num2
    """
    num1 = randint(0, 10)
    num2 = randint(0, 100)

    resultQuestion = QUESTION_FORMAT.format(num1=num1, num2=num2)

    answer = int(num1**2 + num2)

    return {
        "type": "text",
        "question": resultQuestion,
        "resources": [

        ],
        "acceptedAnswers": [str(answer)],
        "caseSensitive": False
    }


if __name__ == "__main__":
    print(giveQuestion())
