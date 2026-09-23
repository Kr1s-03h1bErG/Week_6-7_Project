from rich import pretty, print as rprint, console, style, panel, padding, layout
from rich.pretty import pprint
from rich.style import Style
from rich.console import Console
from rich.padding import Padding
from rich.layout import Layout
console = Console()

#yes that's necessary

#need fancy print for layout function specifically (rprint, won't work for most other things i think???) the docs are missing so much shit wtf
layout = Layout()
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)
layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)
# print(layout) <- this doesn't work

rprint(layout) #<- this does


# console.print("[white][not bold]what the[/not bold][/white] hell", style = 'bold red underline')
# console.print(Padding("Welcome to Steam Access", (1, 1), style = 'bold on blue', expand=False))
# print(layout)