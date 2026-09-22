def add_game_to_user(game_name, username):
    user_key = username + ":"
    with open("user.txt", "r") as file:
        lines = file.readlines()
    with open("user.txt", "w") as file:
        for line in lines:
            if user_key in line:
                if game_name not in line:
                    file.write(line + game_name + ":")
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
    game_name = original_game_name + ":"
    with open("game.txt", "r") as file:
        for line_number, line in enumerate(file, 1): # starts numbering at 1
            line = line.strip() #this also removes \n which is helpful
            game_data = {"game": original_game_name} # initialize player_game_data
            if game_name in line:
                player_data = line.split(":") # seperate user and password from game data
                print(player_data)
                player_data.pop(0)
                print(player_data)
                for game in player_data:
                    gd = game.split(",") # split game_id from position
                    game_data[gd[0]] = gd[1]
                    # ^ just adds a dict of game_id and position in to games list in dict 
                return game_data

def del_game(game_name, username):
    if read_game(game_name)["dev"] == username:
        user_data = username + ":"
        with open("game.txt", "r") as file:
            lines = file.readlines()
        with open("game.txt", "w") as file:
            for line in lines:
                if user_data not in line:
                    file.write(line)

def upd_game(game_name, username, change, change_data):
    game_data = read_game(game_name)
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

# del_game("Project Zomboid", "The Indie Stone")
# print(read_game("Project Zomboid"))
# print(add_game("Project Zomboid", "Isometric Survival", "kris", 25))
# add_game_to_user("Project Zomboid", "kris")
# upd_game("Project Zomboid", "kris", "dev", "The Indie Stone")
#9/22 this all works 