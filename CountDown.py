import random
import itertools
import time
import sqlite3

def sql():
    conn = sqlite3.connect("word_database.db")

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS words_table (
            words TEXT
        )
    """)
    conn.commit()
    conn.close()


character_list = list(range(9))
def select_characters():
    for i in range(1,10):
        selection = input('v for vowel, c for constant:')
        if selection == 'v':
            characters = "aeiou"
            random_index = random.randint(0, len(characters) - 1)
            random_char = characters[random_index]
            character_list[i -1] = random_char
            print('letter', i, 'Is', random_char)
        else:
            characters = "bcdfghjklmnpqrstvwxyz"
            random_index = random.randint(0, len(characters) - 1)
            random_char = characters[random_index]
            character_list[i -1] = random_char
            print('letter', i, 'Is', random_char)
    return character_list

def dictionary_reader():
    words_array = []
    try:
        with open("words.txt", "r") as file:
            for line in file:
                word = line.strip().replace("-", "")
                conn = sqlite3.connect("word_database.db")
                cur = conn.cursor()
                cur.execute("INSERT INTO words_table (words) VALUES (?)", (word,))
                conn.commit()
                conn.close()
    except FileNotFoundError:
        print("Error: File 'words.txt' not found.")
    return words_array

# def check_guess(possible_answers, game_letters, user_guess):
#     if user_guess in possible_answers:
#         sorted_guess = "".join(sorted(user_guess))
#         for combination in itertools.permutations(game_letters, len(user_guess)):
#             sorted_combination = "".join(sorted(combination))
#             if sorted_guess == sorted_combination:
#                 return len(user_guess)
#     return 0

def check_guess2(pos_answers, answer):
    for i in range(0, len(pos_answers)):
        if answer == pos_answers[i]:
            score = len(answer)
        else:
            score = 0
    return score


def timer(seconds):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= seconds:
            print("Time's up!")
            break
        else:
            print(f"Time remaining: {int(seconds - elapsed_time)} seconds", end="\r")
            time.sleep(0.1)


# def main():
#     print('Hello and welcome to the Count Down!!')
#     pos_answers = []
#     pos_answers = dictionary_reader
#     print(pos_answers)
#     char = select_characters()
#     print(char)
#     timer(30)
#     guess = input('Guess a word:')
#     #score = check_guess(pos_answers, char, guess)
#     score = check_guess2(pos_answers, guess)
# main()

dictionary_reader()