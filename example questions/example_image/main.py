"""
Example: Asks for the solution to a simple math question
"""

def giveQuestion():
    """
    Should return an object with specifications (see README.md)

    Example: question about the movie Interstellar
    """
    
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


if __name__== "__main__":
    print(giveQuestion())
