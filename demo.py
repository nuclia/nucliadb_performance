import random
import json

measure = [
    {"name": "speed_1", "value": float(random.randint(20, 24))},
    {"name": "speed_2", "value": float(random.randint(200, 240))},
    {"name": "speed_3", "value": float(random.randint(1, 10))},
]

with open("metrics.json", "w") as f:
    f.write(json.dumps(measure))
