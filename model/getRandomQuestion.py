import os
import random
import importlib

import sys

def getQuestion():
    # Chooses random question path 
    QUESTION_DIR = os.path.abspath(__file__ + "\\..\\..\\questions")
    randomQuestionPath = os.path.join(QUESTION_DIR, random.choice(os.listdir(QUESTION_DIR)), "main.py")

    # Dynamically imports module
    spec = importlib.util.spec_from_file_location("main", randomQuestionPath)
    module = importlib.util.module_from_spec(spec)
    sys.modules["main"] = module
    spec.loader.exec_module(module)

    return module.giveQuestion()
