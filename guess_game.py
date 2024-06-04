import random


def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty):
    return int(input(f"Guess a number between 0 to {difficulty}: "))

def compare_results(random_number, user_guess):
    return random_number == user_guess

def play(difficulty):
    random_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    print(f"The random number is: {random_number}")
    res = compare_results(random_number, user_guess)
    print("You guess it!" if res else "Wrong guess!")
    return res