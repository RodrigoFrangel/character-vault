# Description

> This is a Python script that allows the user to create a dictionary of characters using a command line interface. After filling in the character information, the program will store the information in a JSON file named `characters.json`.

## Requirements
- `Python 3.x`
- `rich==10.11.0`
- `inquirer==3.7.0`

## How to use
1. Clone or download the repository to your local machine.
2. Install the dependencies.
```
pip install -r requirements.txt
```
3. Navigate to the project directory in your terminal.
4. Run the script.

```
python character_codex.py
```
5. The program will clear the console and print a welcome message with instructions on how to use the script.
6. Follow the prompts to enter character information. You can use the arrow keys to select from a list of options for some fields, or type in your own response.
7. Once you have finished entering all of the character's information, the program will write the character dictionary to a JSON file named `characters.json`.
8. You can access the `characters.json` file to view the characters you have created.

**Note for Windows users:** The console may not clear automatically when running the script. If this happens, you can manually clear the console by running the `cls` command in the terminal.

## Fields
The following is a list of the fields that are included in the character dictionary:

- `name`: the name of the character
- `alias`: the character's nickname or alias
- `age`: the character's age
- `status`: the character's current status (e.g. "Vivo", "Morto", "Desaparecido")
- `debut`: the first appearance of the character (e.g. "A Espada Vol. 1", "Cataclisma")
- `race`: the character's race
- `height`: the character's height in meters
- `weight`: the character's weight in kilograms
- `gender`: the character's gender (e.g. "Homem", "Mulher", "Trans")
- `orientation`: the character's sexual orientation (e.g. "Hétero", "Gay", "Bissexual")
- `summary`: a brief summary of the character (limited to 150 characters)
- `description`: a description of the character (limited to 350 characters)
- `feats`: the character's greatest accomplishments (limited to 150 characters)
- `death`: the cause of the character's death (limited to 50 characters)
- `background`: the character's backstory (limited to 150 characters)
- `origin`: the character's place of origin
- `alignment`: the character's moral alignment
- `friends`: the character's closest friends (comma-separated)
- `player`: the name of the player who created the character.

## Supported platforms
The script should run on any operating system that has Python 3.x installed. The console may not clear automatically on Windows, so Windows users may need to manually clear the console using the `cls` command.

## Contributing
Contributions to this project are welcome. To contribute, please create a pull request with your changes.