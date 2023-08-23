import random

script_path = "/config/lannistajakuha.txt"
with open(script_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

random_line = random.choice(lines).strip()
print(random_line)