# TODO решите задачу
import json
def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total = 0.0

    for item in data:
        if 'score' in item and 'weight' in item:
            total += item['score'] * item['weight']

    return round(total, 3)


print(task())
