from rich import pretty, print as rprint, console, style, panel, padding
from rich.pretty import pprint
from rich.style import Style
from rich.console import Console
from rich.padding import Padding
console = Console()
#yes that's necessary

# console.print("[white][not bold]what the[/not bold][/white] hell", style = 'bold red underline')
console.print(Padding("Welcome to Steam Access", (1, 1), style = 'bold on blue', expand=False))
