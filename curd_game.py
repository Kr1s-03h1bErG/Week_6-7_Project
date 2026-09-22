def add_game(game_name, genre, username, price):
    with open("game.txt", "a") as file:
        file.write(f"\n{game_name}:{genre}:{username}:{price}")
        return True
        
def read_game(original_game_name):
    game_name = original_game_name + ":"
    with open("game.txt", "r") as file:
        for line_number, line in enumerate(file, 1): # starts numbering at 1
            line = line.strip() #this also removes \n whitch is helpfull
            game_data = {"game": original_game_name} # initialize player_game_data
            if game_name in line:
                player_data = line.split(":") # seperate user and password from game data
                games_real_name = player_data.pop(0)
                for game in player_data:
                    gd = game.split(",") # split game_id from position
                    game_data[gd[0]] = gd[1]
                    # ^ just adds a dict of game_id and position in to games list in dict 
                return game_data

# def delete_game(game_name, username):
print(read_game("Project Zomboid"))
# add_game("Project Zomboid", "Isometric Survival", "The Indie Stone", 25)