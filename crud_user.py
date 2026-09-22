# checks if user is in db returns Bool
def is_user_in_user(username):
    user_data = username + ":"
    with open("user.txt", "r") as file:
        for line_number, line in enumerate(file, 1): # starts numbering at 1
            if user_data in line:
                return True
        return False

#checks Returns if it succeeded or failed (bool)
def login():
    while True:
        need_login = get_response("Do you need to login? Y/N: ")
        if need_login:
            username = get_response("What is your Username?: ")
            return is_user_in_user(username) , username
        else: # return that it failed to login so we can register later
            print("Failed to find name in db/user didn't need to")
            return False , ""
#Returns suceeded or failed (bool) and player name
def add_user(username):
    with open("user.txt", "a") as file:
        file.write(f"\n{username}:")
        return True
# this returns if it registered sucessfuly as a
def register():
    need_register = get_response("Do you need to register? Y/N: ")
    while True:
        if need_register:
            username = get_response("What will be your Username?: ")
            if is_user_in_user(username):
                print("username already in db restarting register")
            else:
                return add_user(username) 
        else: # return that it failed to login so we can register later
            print("User Didn't need to register for new account! ")
            return False
#returns dict of playwer data shown below games is a list of games that builds per game 
# dict {"username": username, "games": [{"game_id": "1", "position": 2}]}
def get_player_data(game_name):
    user_data = game_name + ":"
    with open("user.txt", "r") as file:
        for line_number, line in enumerate(file, 1): # starts numbering at 1
            line = line.strip() #this also removes \n whitch is helpfull
            game_data = {"user": game_name} # initialize player_game_data
            if user_data in line:
                player_data = line.split(":") # seperate user and password from game data
                player_data.pop(0)
                if len(player_data[0]) == 0: # if no games in player data
                    game_data["games"] = []
                    return game_data
                for game in player_data:
                    gd = game.split(",") # split game_id from position
                    game_data[gd[0]] = gd[1]
                    # ^ just adds a dict of game_id and position in to games list in dict 
                return game_data

def get_response(text):
    player_response = input(text)
    stripped_player_response = player_response.strip()
    nice_player_response = stripped_player_response.lower()
    # makes the response useable 

    # checks if y/n and sets it to false or True

    if nice_player_response == "y":
        return True
    elif nice_player_response == "n":
        return False
    # checks if y/n and sets it to false or True

    # checks if player input is a number
    # print(nice_player_response)
    # print(type(nice_player_response))
    try:
        old_player_response = nice_player_response
        nice_player_response = int(nice_player_response)
        nums = [1,2,3,4,5,6,7,8,9,0]
        if  nice_player_response in nums:
            return int(nice_player_response)
    except:
        nice_player_response = old_player_response
    return nice_player_response


