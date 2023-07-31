import re
import json

with open("fraWikipedia.txt", encoding="utf-8") as file:
    fullText = file.read()
    lines = [line for line in fullText.split("\n")][0::2]
    resultList = []

    doubleBrackets = re.compile("\[\[(.*?)]]")
    for line in lines:
        # print(line)
        before, after = line.split("||")
        country = doubleBrackets.findall(before)
        country = [c.split("|")[1] if "|" in c else c for c in country][0]
        print(country)
        capitals = doubleBrackets.findall(after)
        capitals = [c.split("|")[1] if "|" in c else c for c in capitals]
        print(capitals)

        instanceDict = {"country": country, "capital": capitals}
        resultList.append(instanceDict)

with open("capitals.json", "w", encoding="utf-8") as file:
    json.dump(resultList, file, ensure_ascii=False)