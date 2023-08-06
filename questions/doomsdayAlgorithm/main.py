from datetime import date
import numpy

QUESTION_FORMAT = "Hvilken ukedag er {dato}?"

def giveQuestion():
    """
    Returns a question about the weekday of a random date betw
    """
    UKEDAGER = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]

    number_of_years_to_sample_from = 800
    days_per_year = 365  # Approx., but good enough
    days_of_spread = number_of_years_to_sample_from * days_per_year

    rng = numpy.random.default_rng()
    today_ordinal = date.today().toordinal()

    # Ensures year is within the sample spectrum, retries if not.
    dato = date.max
    while (abs(dato.year - date.today().year) > (number_of_years_to_sample_from / 2)):
        random_ordinal = int(rng.normal(loc=today_ordinal, scale=days_of_spread))
        dato = date.fromordinal(random_ordinal)

    resultQuestion = QUESTION_FORMAT.format(dato=dato.strftime("%d.%m.%Y"))

    ukedag_tall = dato.weekday()
    answer = [UKEDAGER[ukedag_tall], str(ukedag_tall)]

    return {
        "type": "text",
        "question": resultQuestion,
        "resources": [

        ],
        "acceptedAnswers": answer,
        "caseSensitive": False
    }


if __name__ == "__main__":
    print(giveQuestion())
