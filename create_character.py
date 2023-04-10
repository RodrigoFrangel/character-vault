import inquirer
import json


# Define a function to gather character information
def create_character():
    # Biographical Information
    name = input("Nome do personagem: ")
    alias = input("Apelido do personagem: ")
    age = input("Idade do personagem: ")

    # Use inquirer to display options for "status"
    status_choices = ["Vivo", "Morto", "Desaparecido", "Outro"]
    status = inquirer.prompt([
        inquirer.List('status',
                      message="Status atual",
                      choices=status_choices,
                      ),
    ])['status']
    debut_choices = [
        "Cataclisma",
        "Cataclisma Parte II",
        "Cataclisma: Capítulo Final",
        "O Rei Amarelo",
        "O Caos Rastejante",
        "Mundo Isekai",
        "A Espada Vol. 1"
    ]
    debut = inquirer.prompt([
        inquirer.List('debut',
                      message="Sua primeira aparição",
                      choices=debut_choices,
                      ),
    ])['debut']

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
    gender = inquirer.prompt([
        inquirer.List('gender',
                      message="Gênero do personagem",
                      choices=gender_choices,
                      ),
    ])['gender']
    orientation_choices = [
        "Hétero",
        "Gay",
        "Bissexual",
        "Pansexual",
        "Outro"
    ]
    orientation = inquirer.prompt([
        inquirer.List('orientation',
                      message="Orientação sexual do personagem",
                      choices=orientation_choices,
                      ),
    ])['orientation']
    # Narrative
    game_choices = [
        "Dungeons and Dragons",
        "Chamado de Cthulhu",
        "Cyberpunk RED",
        "Ordem Paranormal",
        "Outro"
    ]
    game = inquirer.prompt([
        inquirer.List('game',
                      message="Sistema do RPG",
                      choices=game_choices,
                      ),
    ])['game']
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
