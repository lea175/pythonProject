import json
import random

secret = random.randint(1, 30)
guess = None
attempts = 0
secret_number_file = "secret_number_best_score.txt"

with open(secret_number_file, "r") as attempts_file:
    attempts_from_file = int(attempts_file.read())
    print(f"Best score: {attempts_from_file} attempts.")

with open ("secret_number_attempts.json", "r") as all_attempts_file:
    logged_attempts = json.loads(all_attempts_file.read())
    print(f"The number of all game attempts: {logged_attempts}")

while True:
    guess = int(input("What is your guess? "))
    attempts = attempts + 1

    if guess == secret:
        print(f"Congratulations, it is {secret}")
        print(f"Number of attempts: {attempts}")
        with open ("secret_number_attempts.json", "w") as score_file:
            score_file.write(json.dumps(logged_attempts.append(attempts)))

        if attempts < attempts_from_file:
            with open(secret_number_file, "w") as attempts_file:
                attempts_file.write(str(attempts))
        break

    hint = None
    if guess > secret:
        hint = "smaller"
    else:
        hint = "bigger"

    print(f"Sorry, your guess is incorrect, try something {hint}")
