import json
import tkinter as tk
from tkinter import messagebox

status_options = ["Vivo", "Morto", "Desaparecido", "Outro"]

debut_options = [
    "A Espada Vol. 1",
    "Cataclisma",
    "Cataclisma Parte II",
    "Cataclisma: Capítulo Final",
    "Mundo Isekai",
    "O Rei Amarelo",
    "O Caos Rastejante",
    "Em Breve",
    "Outro"
]

height_unit_options = ["cm", "ft", "in"]

weight_unit_options = ["kg", "lb"]

gender_options = [
    "Homem",
    "Mulher",
    "Trans",
    "Não-binário",
    "Outro",
]

orientation_options = [
    "Hétero",
    "Gay",
    "Bissexual",
    "Pansexual",
    "Outro"
]

game_options = [
    "Dungeons & Dragons",
    "Chamado de Cthulhu",
    "Ordem Paranormal",
    "Cyberpunk RED",
    "Outro"
]

player_options = [
    "Felipe Souza",
    "Gabriel Schutt",
    "Rhuan Mascaro",
    "Rodrigo Frangel",
    "Outro"
]


class CharacterCreator:
    def __init__(self, master):
        self.master = master
        master.title("Character Creator")

        # Character Name
        self.name_label = tk.Label(self.master, text="Nome do personagem:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(self.master, validate="key")
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Character Alias
        self.alias_label = tk.Label(self.master, text="Apelido do personagem:")
        self.alias_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.alias_entry = tk.Entry(self.master, validate="key")
        self.alias_entry.grid(row=1, column=1, padx=5, pady=5)

        # Character Age
        self.age_label = tk.Label(self.master, text="Idade do personagem:")
        self.age_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)

        # Character Status
        self.status_label = tk.Label(self.master, text="Status atual:")
        self.status_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.status_var = tk.StringVar(self.master)
        self.status_var.set("Vivo")
        self.status_dropdown = tk.OptionMenu(
            self.master, self.status_var, *status_options,
            command=lambda selected_option: self.update_option_entry(
                                                selected_option,
                                                self.status_entry
                                            ))
        self.status_dropdown.grid(row=3, column=1, padx=5, pady=5)
        self.status_entry_label = tk.Label(
            self.master, text="Digite seu status atual:")
        self.status_entry_label.grid(
            row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.status_entry = tk.Entry(self.master, state=tk.DISABLED)
        self.status_entry.grid(row=4, column=1, padx=5, pady=5)

        # Character Debut
        self.debut_label = tk.Label(self.master, text="Sua primeira aparição:")
        self.debut_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.debut_var = tk.StringVar(self.master)
        self.debut_var.set("A Espada Vol. 1")
        self.debut_dropdown = tk.OptionMenu(
            self.master, self.debut_var, *debut_options,
            command=lambda selected_option: self.update_option_entry(
                                                selected_option,
                                                self.debut_entry
                                            ))
        self.debut_dropdown.grid(row=5, column=1, padx=5, pady=5)
        self.debut_entry_label = tk.Label(
            self.master, text="Digite sua primeira aparição:")
        self.debut_entry_label.grid(
            row=6, column=0, padx=5, pady=5, sticky=tk.W)
        self.debut_entry = tk.Entry(self.master, state=tk.DISABLED)
        self.debut_entry.grid(row=6, column=1, padx=5, pady=5)

        # Character Race
        self.race_label = tk.Label(self.master, text="Raça do personagem:")
        self.race_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
        self.race_entry = tk.Entry(self.master)
        self.race_entry.grid(row=7, column=1, padx=5, pady=5)
        self.race_entry.insert(0, 'Ex: Humano, Elfo, Orc...')
        self.race_entry.config(fg='gray')
        self.race_entry.bind('<FocusIn>', self.on_entry_click)
        self.race_entry.bind('<FocusOut>', self.on_entry_leave)

        # Character Height
        self.height_label = tk.Label(
            self.master, text="Altura do personagem:"
        )
        self.height_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)
        self.height_entry = tk.Entry(self.master)
        self.height_entry.grid(row=8, column=1, padx=5, pady=5)
        self.height_unit = tk.StringVar(self.master)
        self.height_unit.set("cm")
        self.height_unit_dropdown = tk.OptionMenu(
            self.master, self.height_unit, *height_unit_options)
        self.height_unit_dropdown.grid(row=8, column=2, padx=5, pady=5)
        self.weight_label = tk.Label(
            self.master, text="Peso do personagem:"
        )

        # Character Weight
        self.weight_label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)
        self.weight_entry = tk.Entry(self.master)
        self.weight_entry.grid(row=9, column=1, padx=5, pady=5)
        self.weight_unit = tk.StringVar(self.master)
        self.weight_unit.set("kg")
        self.weight_unit_dropdown = tk.OptionMenu(
            self.master, self.weight_unit, *weight_unit_options
        )
        self.weight_unit_dropdown.grid(row=9, column=2, padx=5, pady=5)

        # Character Gender
        self.gender_label = tk.Label(self.master, text="Gênero do personagem:")
        self.gender_label.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)
        self.gender_var = tk.StringVar(self.master)
        self.gender_var.set("Homem")
        self.gender_dropdown = tk.OptionMenu(
            self.master, self.gender_var, *gender_options,
            command=lambda selected_option: self.update_option_entry(
                                                selected_option,
                                                self.gender_entry
                                            ))
        self.gender_dropdown.grid(row=10, column=1, padx=5, pady=5)
        self.gender_entry_label = tk.Label(
            self.master, text="Digite o gênero do personagem:")
        self.gender_entry_label.grid(
            row=11, column=0, padx=5, pady=5, sticky=tk.W)
        self.gender_entry = tk.Entry(self.master, state=tk.DISABLED)
        self.gender_entry.grid(row=11, column=1, padx=5, pady=5)

        # Character Orientation
        self.orientation_label = tk.Label(
            self.master, text="Orientação sexual do personagem:")
        self.orientation_label.grid(
            row=12, column=0, padx=5, pady=5, sticky=tk.W)
        self.orientation_var = tk.StringVar(self.master)
        self.orientation_var.set("Hétero")
        self.orientation_dropdown = tk.OptionMenu(
            self.master, self.orientation_var, *orientation_options,
            command=lambda selected_option: self.update_option_entry(
                                                selected_option,
                                                self.orientation_entry
                                            ))
        self.orientation_dropdown.grid(row=12, column=1, padx=5, pady=5)
        self.orientation_entry_label = tk.Label(
            self.master, text="Digite da orientação sexual do personagem:")
        self.orientation_entry_label.grid(
            row=13, column=0, padx=5, pady=5, sticky=tk.W)
        self.orientation_entry = tk.Entry(self.master, state=tk.DISABLED)
        self.orientation_entry.grid(row=13, column=1, padx=5, pady=5)

        # Character Game
        self.game_label = tk.Label(self.master, text="Sistema do jogo:")
        self.game_label.grid(row=14, column=0, padx=5, pady=5, sticky=tk.W)
        self.game_var = tk.StringVar(self.master)
        self.game_var.set("Dungeons and Dragons")
        self.game_dropdown = tk.OptionMenu(
            self.master, self.game_var, *game_options,
            command=lambda selected_option: self.update_option_entry(
                                                selected_option,
                                                self.game_entry
                                            ))
        self.game_dropdown.grid(row=14, column=1, padx=5, pady=5)
        self.game_entry_label = tk.Label(
            self.master, text="Digite o sistema do jogo:")
        self.game_entry_label.grid(
            row=15, column=0, padx=5, pady=5, sticky=tk.W)
        self.game_entry = tk.Entry(self.master, state=tk.DISABLED)
        self.game_entry.grid(row=15, column=1, padx=5, pady=5)

        # Character Summary
        self.summary_label = tk.Label(
            self.master, text="Escreva uma descrição curta:")
        self.summary_label.grid(row=16, column=0, padx=5, pady=5, sticky=tk.W)
        self.summary_entry = tk.Entry(self.master)
        self.summary_entry.config(
            validatecommand=(self.summary_entry.register(
                            self.validate_limit_150), "%P"))
        self.summary_entry.grid(row=16, column=1, padx=5, pady=5)

        # Character Description
        self.description_label = tk.Label(
            self.master, text="Escreva uma descrição:")
        self.description_label.grid(
            row=17, column=0, padx=5, pady=5, sticky=tk.W)
        self.description_entry = tk.Entry(self.master)
        self.description_entry.config(
            validatecommand=(self.description_entry.register(
                            self.validate_limit_350), "%P"))
        self.description_entry.grid(row=17, column=1, padx=5, pady=5)

        # Character Feats
        self.feat_label = tk.Label(self.master, text="Grandes feitos:")
        self.feat_label.grid(row=18, column=0, padx=5, pady=5, sticky=tk.W)
        self.feat_entry = tk.Entry(self.master)
        self.feat_entry.config(
            validatecommand=(self.feat_entry.register(
                            self.validate_limit_150), "%P"))
        self.feat_entry.grid(row=18, column=1, padx=5, pady=5)

        # Character Death
        self.death_label = tk.Label(self.master, text="Causa da morte:")
        self.death_label.grid(row=19, column=0, padx=5, pady=5, sticky=tk.W)
        self.death_entry = tk.Entry(self.master)
        self.death_entry.config(
            validatecommand=(self.death_entry.register(
                            self.validate_limit_50), "%P"))
        self.death_entry.grid(row=19, column=1, padx=5, pady=5)

        # Character Background
        self.background_label = tk.Label(
            self.master, text="Passado do personagem:")
        self.background_label.grid(
            row=20, column=0, padx=5, pady=5, sticky=tk.W)
        self.background_entry = tk.Entry(self.master)
        self.background_entry.config(
            validatecommand=(self.background_entry.register(
                            self.validate_limit_150), "%P"))
        self.background_entry.grid(row=20, column=1, padx=5, pady=5)

        # Character Origin
        self.origin_label = tk.Label(self.master, text="Origem do Personagem:")
        self.origin_label.grid(row=21, column=0, padx=5, pady=5, sticky=tk.W)
        self.origin_entry = tk.Entry(self.master)
        self.origin_entry.config(
            validatecommand=(self.origin_entry.register(
                            self.validate_limit_50), "%P"))
        self.origin_entry.grid(row=21, column=1, padx=5, pady=5)
        self.origin_entry.insert(0, 'Cidade de nascimento...')
        self.origin_entry.config(fg='gray')
        self.origin_entry.bind('<FocusIn>', self.on_entry_click)
        self.origin_entry.bind('<FocusOut>', self.on_entry_leave)

        # Character Alignment
        # Character Friends

        # Character Player
        self.player_label = tk.Label(self.master, text="Nome do jogador:")
        self.player_label.grid(row=22, column=0, padx=5, pady=5, sticky=tk.W)
        self.player_var = tk.StringVar(self.master)
        self.player_var.set("Felipe Souza")
        self.player_dropdown = tk.OptionMenu(
            self.master, self.player_var, *player_options,
            command=lambda selected_option: self.update_option_entry(
                                                selected_option,
                                                self.player_entry
                                            ))
        self.player_dropdown.grid(row=22, column=1, padx=5, pady=5)
        self.player_entry_label = tk.Label(
            self.master, text="Digite o nome do jogador:")
        self.player_entry_label.grid(
            row=23, column=0, padx=5, pady=5, sticky=tk.W)
        self.player_entry = tk.Entry(self.master, state=tk.DISABLED)
        self.player_entry.grid(row=23, column=1, padx=5, pady=5)

        # Button
        self.create_button = tk.Button(
            self.master, text="Criar Personagem", command=self.create_character
        )
        self.create_button.grid(row=24, column=1, padx=5, pady=5)

    def validate_limit_50(self, new_value):
        return len(new_value) <= 50

    def validate_limit_150(self, new_value):
        return len(new_value) <= 150

    def validate_limit_350(self, new_value):
        return len(new_value) <= 350

    def update_option_entry(self, selected_option, entry):
        if selected_option == "Outro":
            entry.config(state=tk.NORMAL)
        else:
            entry.config(state=tk.DISABLED)

    def create_character(self):
        character = {
            "name": self.name_entry.get(),
            "alias": self.alias_entry.get(),
            "age": self.age_entry.get(),
            "status": self.status_var.get(),
            "debut": self.debut_var.get(),
            "race": self.race_entry.get(),
            "height": f"{self.height_entry.get()} {self.height_unit.get()}",
            "weight": f"{self.weight_entry.get()} {self.weight_unit.get()}",
            "gender": self.gender_var.get(),
            "orientation": self.orientation_var.get(),
            "game": self.game_var.get(),
            "summary": self.summary_entry.get(),
            "description": self.description_entry.get(),
            "feat": self.feat_entry.get(),
            "death": self.death_entry.get(),
            "background": self.background_entry.get(),
            "origin": self.origin_entry.get(),
            # alignment
            # friends
            "player": self.player_var.get(),

        }

        with open("characters.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        data.append(character)

        with open("characters.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        messagebox.showinfo(
            "Personagem criado",
            "Personagem criado com sucesso!"
        )

    def on_entry_click(self, event):
        if self.race_entry.get() == 'Ex: Humano, Elfo, Orc...':
            self.race_entry.delete(0, tk.END)
            self.race_entry.config(fg='black')
        if self.origin_entry.get() == 'Cidade de nascimento...':
            self.origin_entry.delete(0, tk.END)
            self.origin_entry.config(fg='black')

    def on_entry_leave(self, event):
        if self.race_entry.get() == '':
            self.race_entry.insert(0, 'Ex: Humano, Elfo, Orc...')
            self.race_entry.config(fg='gray')
        if self.origin_entry.get() == '':
            self.origin_entry.insert(0, 'Cidade de nascimento...')
            self.origin_entry.config(fg='gray')


root = tk.Tk()
app = CharacterCreator(root)
root.mainloop()
