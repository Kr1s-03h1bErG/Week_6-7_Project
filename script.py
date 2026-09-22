from crud_user import get_response, get_player_data, is_user_in_user, login, register
from curd_game import add_game, read_game
#dictionary
#usernames as values orkeys?
#its beautiful im a genius
# games = {
#     #hear me out; 'examplegame' : {'creator' : 'exampleuser', 'description' : 'words', 'buycount' : number, 'price' : number} I JUST MAE SOME BULLLSHITTTTTT
# }
#master function ooopooioioooooioiuuoi
def system():
    print("Welcome to Steam Access")
    while True:
        login_stats = login()
        if login_stats[0]: #untill you login successfully
            break
        else: 
            register()
    #prints username + games owned
    print(login_stats)
    player_data = get_player_data(login_stats[1])
    print(player_data)
    
    




#crud functions woah
#we don't need more information for delete update and view right? it can just get information from the dictionary
def post_game(username): #does username need to be an argument here or will it automatically take it from the login thing or smth
    game = input("What is the game name?: ").capitalize()
    genre = input("What is the game genre?: ").capitalize()
    price = get_response("What is the games price?: ")
    add_game(game, genre, username, price)

# def delete_game(game_name, username):


# def update_game(game_name, username):
    

def view_game(game_name): #username to enable/disable delete and update? #will delete and update be accessible on their own or only through view
    game_data = read_game(game_name)
    print(game_data)
# system()
post_game("kris")