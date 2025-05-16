import os
import random
import importlib
import sys
import importlib.util
from pathlib import Path
from tvangspugging.model.config import config


def getQuestion():
    # Chooses random question path
    # TODO: Fix paths
    QUESTION_DIR = Path(__file__) / ".." / ".." / "questions"
    # TODO: Goto next type if question pack can not be imported.
    wantedQuestionPacks = config()["question_packs"] 
    possiblePathChoices = [package for package in QUESTION_DIR.iterdir() if package.name in wantedQuestionPacks]
    randomQuestionPath = random.choice(possiblePathChoices) / "main.py"

    # Dynamically imports module
    spec = importlib.util.spec_from_file_location("main", randomQuestionPath.absolute())
    if spec is None or spec.loader is None:
        raise ImportError("Could not import question pack correctly")
    
    module = importlib.util.module_from_spec(spec)

    sys.modules["main"] = module
    spec.loader.exec_module(module)

    return module.giveQuestion()


if __name__ == "__main__":
    print(getQuestion())
