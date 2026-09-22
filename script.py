from crud_user import get_response, get_player_data, is_user_in_user, login, register
from curd_game import add_game, read_game
from rich import print as rprint, pretty
from rich.panel import Panel

#master function ooopooioioooooioiuuoi
def system():
    print("Welcome to Steam Access")
    while True:
        login_stats = login()
        if login_stats[0]: #until you login successfully
            break
        else: 
            register()
    #prints username + games owned
    print(Panel([darkblue]login_stats))
    player_data = get_player_data(login_stats[1])
    print(player_data)
    #crud uses wow
    choice = input('Would you like to: \n1) Delete one of your own games\n2) Post a new game\n3) Update the information for one of your games\n4) View available games\n')
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

# def delete_game(game_name, username):

def update_game(game_name, username):
    pass
    
def view_game(game_name): #username to enable/disable delete and update
    game_data = read_game(game_name)
    # print(game_data) # this is just the games data idk what else to say about it 
    print(f"{game_data["game"]} is a {game_data["genre"]} game that is made by {game_data["dev"]} and costs {game_data["price"]}$")
# system()
view_game("Project Zomboid")