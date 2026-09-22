from crud_user import get_response, get_player_data, is_user_in_user, login, register
from curd_game import add_game, read_game

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
    print(login_stats)
    player_data = get_player_data(login_stats[1])
    print(player_data)
    #crud uses wow
    choice = input('Would you like to: \n1) Delete one of your own games\n2) Post a new game\n3) Update the information for one of your games\n4) View available games\n')
    #delete
    if choice == 1:
        gamename = input('What game do you want to delete?')
        delete_game(gamename, login_stats[1])
    #create
    elif choice == 2:
        name = input('What is the name of the game you want to post? ')
        genre = input('What genre is the game? ')
        price = input('How much does the game cost? (If free enter 0) ')
        add_game(name, genre, login_stats[1], price)
    #update
    elif choice == 3:
        name = input('What is the name of the game you want to update? ')
        #update_game(name, username)
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


# def update_game(game_name, username):
    

def view_game(game_name): #username to enable/disable delete and update
    game_data = read_game(game_name)
    # print(game_data) # this is just the games data idk what else to say about it 
    print(f"{game_data["game"]} is a {game_data["genre"]} game that is made by {game_data["dev"]} and costs {game_data["price"]}$")
# system()
view_game("Project Zomboid")