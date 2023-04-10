import json


# Define a function to gather character information
def create_character():
    # Biographical Information
    name = input("Nome do personagem: ")
    alias = input("Apelido do personagem: ")
    age = input("Idade do personagem: ")
    status = input("Status atual (vivo/morto/desaparecido): ")
    debut = input("Sua primeira aparição: ")

    # Physical Information
    race = input("Raça do personagem: ")
    height = input("Altura do personagem: "),
    weight = input("Peso do personagem: "),
    gender = input("Gênero do personagem: "),
    orientation = input("Orientação sexual do personagem: "),

    # Narrative
    game = input("Nome do RPG: ")
    summary = input("Escreva uma descrição curta (150): ")[:150]
    description = input("Escreva uma descrição (350): ")[:350]
    feats = input("Seus maiores feitos (150): ")[:150]
    death = input("Causa da morte: ")[:50]
    background = input("Escreva sobre seu passado (150): ")[:150]
    alignment = input("Alinhamento do personagem: ")
    friends = input(
        "Amizades mais próximas (separado por vírgulas): "
    ).split(",")
    player = input("Nome do jogador(a): ")

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
        json.dump(data, file, indent=4)


new_character = create_character()
write_to_file(new_character)
