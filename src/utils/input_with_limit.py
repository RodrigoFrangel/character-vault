from rich.console import Console

console = Console()


def input_with_limit(field_text: str, limit: int):
    field = console.input(field_text)
    while len(field) > limit:
        console.print(
            f"   !! O campo deve ter no máximo {limit} caracteres. Tente novamente.\n",
            style=("bold red"),
        )
        field = console.input(field_text)
    return field
