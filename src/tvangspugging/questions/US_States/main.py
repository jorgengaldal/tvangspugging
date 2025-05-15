import json
import os
import random
from util.use_media import use_media

"""
Example: Asks for the solution to a simple math question
"""

QUESTION = "Hvilken stat i USA er dette?"


def giveQuestion():
    """
    Should return an object with specifications (see README.md)

    Example: question about the movie Interstellar
    """

    with open(os.path.join(os.path.dirname(__file__), "states.json"), encoding="utf-8") as file:
        states = json.load(file)

    state = random.choice(states)

    statePath = state["path"]
    answer = state["state"]

    # Temporarily copies the relevant media to the 
    use_media(__file__, statePath)

    return {
        "type": "image",
        "question": QUESTION,
        "resources": [
            {
                "type": "image",
                "path": statePath
            }
        ],
        "acceptedAnswers": [answer],
        "caseSensitive": False
    }


if __name__ == "__main__":
    print(giveQuestion())
