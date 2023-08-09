from util.use_media import use_media

"""
Example: Asks for the director of Interstellar, with an image
"""


def giveQuestion():
    """
    Should return an object with specifications (see README.md)

    Example: question about the movie Interstellar
    """

    # Temporarily copies the relevant media to the
    use_media(__file__, ".\\media\\interstellar.jpg")

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
