# Character Vault - Cataloging Characters Across Campaigns

> This project aims to create a tool that allows users to create and store information about fictional characters in an RPG (Role Playing Game). The tool allows the user to input biographical and physical information, as well as narrative details about the character. The character data is stored in a JSON file.

## How to use
1. Open the file create_character.py in a Python IDE or text editor.
2. Run the file.
3. Follow the prompts to input information about the character, including name, age, race, gender, orientation, and narrative details such as description and background.
4. Once all information has been entered, the character data will be saved to a JSON file named characters.json.

## Dependencies
This project requires Python 3 and the json library.

## Files
### **create_character.py**
This file contains the code for creating a new character and saving the character data to a JSON file.

### **characters.json**
This file is the database where all characters created by the user are stored in JSON format. Each character is stored as a dictionary within a list.

## Functions
### **create_character()**
This function prompts the user to input information about the character and returns a dictionary containing the character's data.

### **write_to_file(character)**
This function takes a dictionary containing the character data and writes it to the characters.json file. If the file does not exist, it will be created.

## Contributing
Contributions to this project are welcome. To contribute, please create a pull request with your changes.