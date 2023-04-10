from utils.prompt_user_options import prompt_user_options
from utils.write_to_json import write_to_json
from utils.input_with_limit import input_with_limit
from welcome import welcome


def create_character():
    # Biographical Information
    name = input("Nome do personagem: ")
    alias = input("Apelido do personagem: ")
    age = input("Idade do personagem: ")

    # Additional Infomation
    status = prompt_user_options("status", "Status atual")
    if status == "Outro":
        status = input("Digite o status atual: ")

    debut = prompt_user_options("debut", "Sua primeira aparição")

    # Physical Information
    race = input("Raça do personagem: ")
    height = input("Altura do personagem (apenas número): ") + "m"
    weight = input("Peso do personagem (apenas número): ") + "kg"
    gender = prompt_user_options("gender", "Gênero do personagem")
    if gender == "Outro":
        gender = input("Digite o gênero do personagem: ")

    orientation = prompt_user_options(
        "orientation", "Orientação sexual do personagem")
    if orientation == "Outro":
        orientation = input("Digite a orientação sexual do personagem: ")

    # Narrative
    game = prompt_user_options("game", "Sistema do RPG")
    if game == "Outro":
        game = input("Digite o sistema do RPG: ")
    summary = input_with_limit(
        "Escreva uma descrição curta (até 150 caracteres): ", 150)
    description = input_with_limit(
        "Escreva uma descrição (até 350 caracteres): ", 350)
    feats = input_with_limit("Seus maiores feitos (até 150 caracteres): ", 150)
    death = input_with_limit("Causa da morte: ", 50)
    background = input_with_limit(
        "Escreva sobre seu passado (até 150 caracteres): ", 150
    )
    origin = input("Escreva seu local de origem: ")
    alignment = input("Alinhamento do personagem: ")
    friends = input(
        "Amizades mais próximas (separado por vírgulas): ").split(",")
    player = prompt_user_options("player", "Nome do jogador(a)")
    if player == "Outro":
        player = input("Digite o nome de jogador: ")

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
        "player": player,
    }

    return character


welcome()
new_character = create_character()
write_to_json(new_character)
