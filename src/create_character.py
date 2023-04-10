import inquirer
import json

from options import (
     status_options,
     debut_options,
     gender_options,
     orientation_options,
     game_options,
     player_options
)


# Define a function to gather character information
def create_character():
    # Biographical Information
    name = input("Nome do personagem: ")
    alias = input("Apelido do personagem: ")
    age = input("Idade do personagem: ")

    # Use inquirer to display options for "status"
    status = inquirer.prompt([
        inquirer.List('status',
                      message="Status atual",
                      choices=status_options,
                      ),
    ])['status']
    debut = inquirer.prompt([
        inquirer.List('debut',
                      message="Sua primeira aparição",
                      choices=debut_options,
                      ),
    ])['debut']

    # Physical Information
    race = input("Raça do personagem: ")
    height = input("Altura do personagem (apenas número): ") + "m"
    weight = input("Peso do personagem (apenas número): ") + "kg"
    gender = inquirer.prompt([
        inquirer.List('gender',
                      message="Gênero do personagem",
                      choices=gender_options,
                      ),
    ])['gender']
    orientation = inquirer.prompt([
        inquirer.List('orientation',
                      message="Orientação sexual do personagem",
                      choices=orientation_options,
                      ),
    ])['orientation']

    # Narrative
    game = inquirer.prompt([
        inquirer.List('game',
                      message="Sistema do RPG",
                      choices=game_options,
                      ),
    ])['game']
    summary = input("Escreva uma descrição curta (150): ")[:150]
    description = input("Escreva uma descrição (350): ")[:350]
    feats = input("Seus maiores feitos (150): ")[:150]
    death = input("Causa da morte: ")[:50]
    background = input("Escreva sobre seu passado (150): ")[:150]
    origin = input("Escreva seu local de origem: ")
    alignment = input("Alinhamento do personagem: ")
    friends = input(
        "Amizades mais próximas (separado por vírgulas): "
    ).split(",")
    player = inquirer.prompt([
        inquirer.List('player',
                      message="Nome do jogador(a)",
                      choices=player_options,
                      ),
    ])['player']

    # Create a dictionary to store the character information
    character = {
        "name": name,
        "alias": alias,
        "age": age,
        "status": status,
        "debut": debut,
        "race": race,
        "height": height,
        "weight": weight,
        "gender": gender,
        "summary": summary,
        "orientation": orientation,
        "game": game,
        "description": description,
        "feats": feats,
        "death": death,
        "background": background,
        "origin": origin,
        "alignment": alignment,
        "friends": friends,
        "player": player
    }

    return character


def write_to_file(character):
    try:
        with open("characters.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(character)

    # Write the updated data to the file
    with open("characters.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


new_character = create_character()
write_to_file(new_character)
