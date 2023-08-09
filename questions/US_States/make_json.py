import json
import os

result = []

for dir in os.listdir(".\\media\\"):
    state = dir.split(".")[0]
    print(state)
    result.append({"state": state, "path": "./media/" + dir})

with open("states.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False)

