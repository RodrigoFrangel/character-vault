from utils.prompt_user_options import prompt_user_options
from utils.write_to_json import write_to_json


def create_character():
    # Biographical Information
    name = input("Nome do personagem: ")
    alias = input("Apelido do personagem: ")
    age = input("Idade do personagem: ")

    # Additional Infomation
    status = prompt_user_options("status", "Status atual")
    debut = prompt_user_options("debut", "Sua primeira aparição")

    # Physical Information
    race = input("Raça do personagem: ")
    height = input("Altura do personagem (apenas número): ") + "m"
    weight = input("Peso do personagem (apenas número): ") + "kg"
    gender = prompt_user_options("gender", "Gênero do personagem")
    orientation = prompt_user_options(
        "orientation", "Orientação sexual do personagem"
    )

    # Narrative
    game = prompt_user_options("game", "Sistema do RPG")
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
    player = prompt_user_options("player", "Nome do jogador(a)")

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


new_character = create_character()
write_to_json(new_character)
