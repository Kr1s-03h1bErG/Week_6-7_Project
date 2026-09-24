from crud_user import get_player_data
def add_game_to_user(game_name, username):
    user_key = username + ":"
    with open("user.txt", "r") as file:
        lines = file.readlines()
    with open("user.txt", "w") as file:
        for line in lines:
            if user_key in line:
                if game_name not in line:
                    file.write(line + ":" + game_name)
            else:
                file.write(line)

def add_game(game_name, genre, username, price):
    with open("game.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if game_name in line:
                return False
    with open("game.txt", "a") as file:
        file.write(f"\n{game_name}:genre,{genre}:dev,{username}:price,{price}")
        add_game_to_user(game_name,username)
        return True
        
def read_game(original_game_name):
    game_key = original_game_name + ":"
    game_data = {"game": original_game_name} # initialize player_game_data
    with open("game.txt", "r") as file:
        for line_number, line in enumerate(file, 1): # starts numbering at 1
            line = line.strip() #this also removes \n which is helpful
            if game_key in line:
                player_data = line.split(":") # seperate user and password from game data
                # print(player_data)
                player_data.pop(0)
                # print(player_data)
                for player_entry in player_data:
                    gd = player_entry.split(",") # split game_id from position
                    game_data[gd[0]] = gd[1]
                    # ^ just adds a dict of game_id and position in to games list in dict 
        return game_data

def del_game(game_name, username):
    game_data = read_game(game_name)
    if len(game_data) == 4:
        if game_data['dev'] == username:
            user_data = username + ":"
            with open("game.txt", "r") as file:
                lines = file.readlines()
            with open("game.txt", "w") as file:
                for line in lines:
                    if user_data in line:
                        file.write("\n")
                    else:
                        file.write(line)

            with open("user.txt", "r") as file:
                lines = file.readlines()
            with open("game.txt", "w") as file:
                for line in lines:
                    if user_data in line and game_name in line:
                        player_data = get_player_data(username)
                        new_line = player_data[user] + ":"
                        for game in player_data["games"]:
                           new_line += game["games"] + ":"
                        file.write(new_line) #need to pull user data and use it here 
                    else:
                        file.write(line)
    else:
        print("Game was not found!")                

def upd_game(game_name, username, change, change_data):
    game_data = read_game(game_name)
    print(game_data)
    print(len(game_data))
    if len(game_data) == 4:
        if game_data["dev"] == username:
            user_data = game_name + ":"
            if change in game_data:
                game_data[change] = change_data
            else:
                return False
            with open("game.txt", "r") as file:
                lines = file.readlines()
            with open("game.txt", "w") as file:
                for line in lines:
                    if user_data in line:
                        file.write(f"{game_data["game"]}:genre,{game_data["genre"]}:dev,{game_data["dev"]}:price,{game_data["price"]}")
                    else:
                        file.write(line)
    else:
        print("Game was not found!")

# del_game("Project Zomboid", "The Indie Stone")
# print(read_game("Project Zomboid"))
# print(add_game("Project Zomboid", "Isometric Survival", "kris", 25))
# add_game_to_user("Project Zomboid", "kris")
# upd_game("Project Zomboid", "kris", "dev", "The Indie Stone")
#9/24 this really all works 