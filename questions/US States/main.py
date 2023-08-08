import shutil
import os

"""
Example: Asks for the solution to a simple math question
"""


def giveQuestion():
    """
    Should return an object with specifications (see README.md)

    Example: question about the movie Interstellar
    """

    # Temporarily copies the relevant media to the 
    webMediaPath = os.path.abspath(os.path.join(__file__, "..\\..\\..\\view\\web\\media"))
    if not os.path.exists(webMediaPath):
        os.mkdir(webMediaPath)
    questionInterstellarPath = os.path.abspath(os.path.join(__file__, ".\\..\\media\\interstellar.jpg"))
    shutil.copyfile(questionInterstellarPath, os.path.join(webMediaPath, ".\\interstellar.jpg"))

    return {
        "type": "image",
        "question": "Hvem regisserte filmen Interstellar?",
        "resources": [
            {
                "type": "image",
                "path": "./media/interstellar.jpg"
            }
        ],
        "acceptedAnswers": ["Christopher Nolan", "Nolan"],
        "caseSensitive": False
    }


if __name__ == "__main__":
    print(giveQuestion())
