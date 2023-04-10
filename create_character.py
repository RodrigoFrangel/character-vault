import inquirer
import json
import os


# Adicione a função get_choice aqui
def get_choice(prompt_message, choices):
    return inquirer.prompt([
        inquirer.List('choice',
                      message=prompt_message,
                      choices=choices,
                      ),
    ])['choice']


# Define a function to gather character information
def create_character():
    # Biographical Information
    name = input("Nome do personagem: ")
    alias = input("Apelido do personagem: ")
    age = input("Idade do personagem: ")

    # Use inquirer to display options for "status"
    status_choices = ["Vivo", "Morto", "Desaparecido", "Outro"]
    status = get_choice("Status atual", status_choices)
    debut_choices = [
        "Cataclisma",
        "Cataclisma Parte II",
        "Cataclisma: Capítulo Final",
        "O Rei Amarelo",
        "O Caos Rastejante",
        "Mundo Isekai",
        "A Espada Vol. 1"
    ]
    debut = get_choice("Sua primeira aparição", debut_choices)

    # Physical Information
    race = input("Raça do personagem: ")
    height = input("Altura do personagem: ") + "m"
    weight = input("Peso do personagem: ") + "kg"
    gender_choices = [
        "Homem",
        "Mulher",
        "Trans",
        "Não-binário",
        "Outro",
    ]
    gender = get_choice("Gênero do personagem", gender_choices)
    orientation_choices = [
        "Hétero",
        "Gay",
        "Bissexual",
        "Pansexual",
        "Outro"
    ]
    orientation = get_choice("Orientação sexual do personagem", orientation_choices)
    # Narrative
    game_choices = [
        "Dungeons and Dragons",
        "Chamado de Cthulhu",
        "Cyberpunk RED",
        "Ordem Paranormal",
        "Outro"
    ]
    game = get_choice("Sistema do RPG", game_choices)
    summary = input("Escreva uma descrição curta (150): ")[:150]
    description = input("Escreva uma descrição (350): ")[:350]
    feats = input("Seus maiores feitos (150): ")[:150]
    death = input("Causa da morte: ")[:50]
    background = input("Escreva sobre seu passado (150): ")[:150]
    alignment = input("Alinhamento do personagem: ")
    friends = [friend.strip() for friend in input("Amizades mais próximas (separado por vírgulas): ").split(",")]
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
    filename = "characters.json"

    # Check if the file exists and create an empty list or read its content
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = []

    data.append(character)

    # Write the updated data to the file
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


new_character = create_character()
write_to_file(new_character)
