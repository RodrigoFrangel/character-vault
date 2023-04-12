import tkinter as tk
import json

status_options = ["Vivo", "Morto", "Desaparecido", "Outro"]
debut_options = [
    "A Espada Vol. 1",
    "Cataclisma",
    "Cataclisma Parte II",
    "Cataclisma: Capítulo Final",
    "Mundo Isekai",
    "O Rei Amarelo",
    "O Caos Rastejante"
]


class CharacterCreator:
    def __init__(self, master):
        self.master = master
        master.title("Character Creator")

        self.name_label = tk.Label(master, text="Nome do personagem:")
        self.name_label.pack()

        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.status_label = tk.Label(master, text="Status atual:")
        self.status_label.pack()

        self.status_var = tk.StringVar(master)
        self.status_var.set(status_options[0])

        self.status_menu = tk.OptionMenu(
          master, self.status_var, *status_options, command=self.update_status
        )
        self.status_menu.pack()

        self.status_entry = tk.Entry(master)
        self.status_entry.pack()

        self.debut_label = tk.Label(master, text="Sua primeira aparição:")
        self.debut_label.pack()

        self.debut_var = tk.StringVar(master)
        self.debut_var.set(debut_options[0])

        self.debut_menu = tk.OptionMenu(master, self.debut_var, *debut_options)
        self.debut_menu.pack()

        self.height_label = tk.Label(
          master, text="Altura do personagem (apenas número):"
        )
        self.height_label.pack()

        self.height_entry = tk.Entry(master)
        self.height_entry.pack()

        self.background_label = tk.Label(
          master, text="Escreva sobre seu passado (até 150 caracteres):"
        )
        self.background_label.pack()

        self.background_entry = tk.Entry(master)
        self.background_entry.pack()

        self.friends_label = tk.Label(
            master, text="Amizades mais próximas (separado por vírgulas):"
        )
        self.friends_label.pack()

        self.friends_entry = tk.Entry(master)
        self.friends_entry.pack()

        self.submit_button = tk.Button(
            master, text="Criar personagem", command=self.create_character
        )
        self.submit_button.pack()

    def update_status(self, value):
        if value == "Outro":
            self.status_entry.config(state='normal')
        else:
            self.status_entry.delete(0, tk.END)
            self.status_entry.config(state='disabled')

    def create_character(self):
        name = self.name_entry.get()
        status = self.status_var.get() \
            if self.status_var.get() == "Outro" \
            else self.status_var.get()
        debut = self.debut_var.get()
        height = self.height_entry.get() + "m"
        background = self.background_entry.get()
        friends = self.friends_entry.get().split(",")

        character = {
            "name": name,
            "status": status,
            "debut": debut,
            "height": height,
            "background": background,
            "friends": friends,
        }

        self.write_to_json(character)
        self.clear_fields()

    def write_to_json(self, character):
        try:
            with open("characters.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(character)

        # Write the updated data to the file
        with open("characters.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)
        self.debut_var.set(debut_options[0])
        self.height_entry.delete(0, tk.END)
        self.background_entry.delete(0, tk.END)
        self.friends_entry.delete(0, tk.END)


root = tk.Tk()
app = CharacterCreator(root)
root.mainloop()
