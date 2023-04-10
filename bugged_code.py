# from rich.console import Console
# from rich.markdown import Markdown

# console = Console()


# def input_markdown(text):
#     return console.print(Markdown(text))


# def input_with_limit(field_text: str, limit: int):
#     field = input_markdown(field_text)
#     while len(field) > limit:
#         console.print(
#             f"   !! O campo deve ter no máximo {limit} caracteres. Tente novamente.\n",
#             style=("bold red")
#         )
#         field = input_markdown(field_text)
#     return field
