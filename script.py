from crud_user import get_response, get_player_data, is_user_in_user, login, register
from curd_game import add_game, read_game, del_game , upd_game , add_game_to_user
from rich import pretty, print as rprint, console, style, panel, padding
from rich.pretty import pprint
from rich.style import Style
from rich.console import Console
from rich.padding import Padding
console = Console() #DO NOT DELETE ME
#yes that's reallynecessary


#master function ooopooioioooooioiuuoi
def system():
    console.print(Padding("Welcome to Steam Access", (1, 1), style = 'bold on blue', expand=False))
    while True:
        login_stats = login()
        if login_stats[0]: #until you login successfully
            break
        else: 
            register()
    #prints username + games owned
    print((login_stats))
    player_data = get_player_data(login_stats[1])
    print(player_data)
    #crud uses wow
    choice = get_response('Would you like to: \n1) Delete one of your own games\n2) Post a new game\n3) Update the information for one of your games\n4) View available games\n')
    #delete
    if choice == 1:
        delete_game(login_stats[1])
    #create
    elif choice == 2:
        post_game(login_stats[1])
    #update
    elif choice == 3:
        update_game(login_stats[1])
    #read
    elif choice == 4:
        name = input('What game do you want to see the information for? ')
        view_game(name)

#crud functions woah
def post_game(username): 
    game = input("What is the game name?: ").capitalize()
    genre = input("What is the game genre?: ").capitalize()
    price = get_response("What is the games price?: ")
    add_game(game, genre, username, price)
    print(f"made {game}!")
    

def delete_game(username):
    game = input("What is the game name?: ").capitalize()
    del_game(game, login_stats[1])
    print(f"Deleted {game}!")

def update_game(username):
    game = get_response("What is the games name you wish to edit?: ")
    print("Parts of a game are: game, dev, price, and genre")
    key = get_response("What is the part of the game data you wish to edit?: ")
    data = get_response("What is the new game data?: ")
    upd_game(game, username, key, data)
    
def view_game(game_name): #username to enable/disable delete and update
    game_data = read_game(game_name)
    # print(game_data) # this is just the games data idk what else to say about it 
    print(f"{game_data["game"]} is a {game_data["genre"]} game that is made by {game_data["dev"]} and costs {game_data["price"]}$")
system()
