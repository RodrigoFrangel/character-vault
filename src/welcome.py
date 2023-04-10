import os

from rich.console import Console

console = Console()


def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("""
        Bem-vindo ao [bold]Character Codex[/bold]!

        [reverse][bold] COMO USAR [/bold][/reverse]
        Basta seguir as instruções e preencher os dados
        Demora apenas alguns minutos, então, tome seu tempo
        Ao finalizar, verifique o arquivo [bold]characters.json[/bold]
        """)
