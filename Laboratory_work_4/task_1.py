# TODO решите задачу
import json

json_file_name = "input.json"

def task() -> float:
    with open(json_file_name) as file:
        data = json.load(file)

    result = 0.0

    for i in range(len(data)):
       result += (data[i]["score"] * data[i]["weight"])

    return round(result, 3)


print(task())

