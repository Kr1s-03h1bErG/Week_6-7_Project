from rich import pretty, print as rprint, console, style
from rich.pretty import pprint
from rich.style import Style
from rich.console import Console
console = Console()

console.print("[white][not bold]what the[/not bold][/white] hell", style = 'bold red ')