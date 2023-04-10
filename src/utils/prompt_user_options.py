import inquirer

from utils.user_options import *


def prompt_user_options(field, text):
    options = inquirer.prompt(
        [
            inquirer.List(
                field,
                message=text,
                choices=eval(f"{field}_options"),
            ),
        ]
    )
    return options[field]
