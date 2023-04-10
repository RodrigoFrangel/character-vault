import json


def write_to_json(character):
    try:
        with open("characters.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(character)

    # Write the updated data to the file
    with open("characters.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
