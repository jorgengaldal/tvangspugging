import os
import random
import importlib
import sys


def getQuestion():
    # Chooses random question path
    QUESTION_DIR = os.path.abspath(__file__ + "\\..\\..\\questions\\")
    randomQuestionPath = os.path.join(QUESTION_DIR, random.choice(
        [path for path in os.listdir(QUESTION_DIR) if (not "__pycache__" in path) and os.path.isdir(os.path.join(QUESTION_DIR, path))]),
        "main.py")  # Ensures that only directories (and not __pycache__) are chosen.

    # Dynamically imports module
    spec = importlib.util.spec_from_file_location("main", randomQuestionPath)
    module = importlib.util.module_from_spec(spec)
    sys.modules["main"] = module
    spec.loader.exec_module(module)

    return module.giveQuestion()


if __name__ == "__main__":
    print(getQuestion())
