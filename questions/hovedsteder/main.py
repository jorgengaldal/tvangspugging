"""
"capitals.json" is made from the file "fraWikipedia.txt" using "sanitizeFile.py".
Source: https://no.wikipedia.org/wiki/Liste_over_hovedsteder_etter_land
The following countries have then had their entry manually changed:
Nauru
Kamerun
Brasil
Chile
Colombia
Costa Rica
Finland
Island
Kosovo
Moldova

TODO: Legg til "Hovedsteder i andre land og områder" og "Hovedsteder i delvis eller ikke anerkjente stater"

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
        "acceptedAnswers": answer,
        "caseSensitive": False
    }
