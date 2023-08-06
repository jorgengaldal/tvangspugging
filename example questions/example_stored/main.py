"""
Example: Asks for the capital of a country
"""

import json
import random
import os

QUESTION_FORMAT = "Hva er hovedstaden i {country}?"


def giveQuestion():
    """
    Should return a tuple of (str: question, list[str]: acceptedAnswers)

    Example: capital in countries
    """

    with open(os.path.join(os.path.dirname(__file__), "capitals.json"), encoding="utf-8") as file:
        capitals = json.load(file)

    country = random.choice(capitals)

    question = QUESTION_FORMAT.format(country=country["country"])
    answer = country["capital"]

    return {
        "type": "text",
        "question": question,
        "resources": [
        ],
        "acceptedAnswers": [answer],
        "caseSensitive": False
    }


if __name__ == "__main__":
    print(giveQuestion())
