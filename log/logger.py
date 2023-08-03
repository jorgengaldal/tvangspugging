import datetime


def logQuestion(questionObject, answer):
    with open("./log/logs", "a") as file:
        print(f"""{datetime.datetime.now().isoformat()}]{questionObject["question"]}]{';'.join(questionObject["acceptedAnswers"])}]{answer}""",
              file=file)
