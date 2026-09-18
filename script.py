from crud_user import get_response, get_player_data, is_user_in_user, login, register
#dictionary
#usernames as values orkeys?
#its beautiful im a genius
# games = {
#     #hear me out; 'examplegame' : {'creator' : 'exampleuser', 'description' : 'words', 'buycount' : number, 'price' : number} I JUST MAE SOME BULLLSHITTTTTT
# }
#master function ooopooioioooooioiuuoi
def system()
    print("Welcome to Steam Access")
    while True:
        login_stats = login()
        if login_stats[0]: #untill you login successfully
            break
        else: 
            register()
    #prints username + games owned
    player_data = get_player_data(login_stats[1], login_stats[2])
    print(player_data)
    
    




#crud functions woah
#we don't need more information for delete update and view right? it can just get information from the dictionary
def post_game(game_name, description, price, buycount, username) #does username need to be an argument here or will it automatically take it from the login thing or smth
    #does this even need to be more than just a whole bunch of inputs?
 
def delete_game(game_name, username)


def update_game(game_name, username)


def view_game(game_name, username) #username to enable/disable delete and update? #will delete and update be accessible on their own or only through view

