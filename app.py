
games = [
    {
        "id": 1, 
        "filename": "memory_game",
        "title": "Memory Game", 
        "description": "a sequence of numbers will appear for 1 second and you have to guess it back."
    }, 
    {
        "id": 2, 
        "filename": "guess_game",
        "title": "Guess Game",
        "description": "guess a number and see if you chose like the computer."
    }, 
    {
        "id": 3, 
        "filename": "currency_roulette_game",
        "title": "Currency Roulette",
        "description": "try and guess the value of a random amount of USD in ILS"
    }
]

def run_game(filename, difficulty):
    # module_name = f"file{file_num}"
    module = __import__(filename)
    module.play( difficulty )

def welcome():
    username = input("Please enter your name: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")
    

def start_play():
    quit = False
    while not quit:

        game = {}
        
        print("Please choose a game to play:")
        for game in games:
            print(f"{game['id']}. {game['title']} - {game['description']}")
        game_id = input("> ")

        game_ids = [game['id'] for game in games]
        if game_id.isdigit() and int(game_id) in game_ids:
            selected_game = next((game for game in games if game['id'] == int(game_id)), None)
            if selected_game:
                print(f"You selected the game: {selected_game['title']}")
                game["filename"] = selected_game["filename"]
                # Add game logic here
            else:
                print("Invalid game selection.")
                return
        else:
            print("Invalid game selection.")
            return

        game_difficult = input("select a difficulty level between 1 and 5: ")
        if game_difficult.isdigit() and int(game_difficult) in range(1, 5):
            print(f"You selected difficulty level: {game_difficult}")
            game["difficulty"] = int(game_difficult)
        else: 
            print("Invalid difficulty selection.")
            return
        
        run_game(game["filename"], game["difficulty"])

        
        play_again = input(f"Do you want to play again? (y/n): ")
        if play_again.lower() == "n":
            quit = True
            print("Thanks for playing!")