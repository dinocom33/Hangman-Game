import random

words_list = ["world", "hello", "look", "house", "country"]
random.shuffle(words_list)
correct_answer = list(words_list[0])

letter_counter = 0  # count guessed letters and stops the game after last guessed one
incorrect_answers = 10

display_word = []  # empty list. it will keep correct answer
used_letters = []  # this list will collect all used letters
display_word.extend(correct_answer)  # adds correct answer
used_letters.extend(display_word)


# iterate through the list and replace all letters with "_"
for i in range(len(display_word)):
    display_word[i] = "_"

print(*display_word, sep=" ")  # add space between characters and display them to the player
print()

# asking player to guess a letter
while letter_counter < len(correct_answer) and incorrect_answers > 0:
    player_guess = input("Please guess a letter: ").lower()
    print()

    for i in range(len(correct_answer)):
        if correct_answer[i] == player_guess and player_guess in used_letters:
            display_word[i] = player_guess
            letter_counter += 1
            used_letters.remove(player_guess)
    if player_guess not in display_word:
        incorrect_answers -= 1
        print(f"Sorry, wrong guess! You have {incorrect_answers} chances left!")

    print(f"You have guessed: {letter_counter} correct letters")
    print(*display_word, sep=" ")
    print()

if incorrect_answers > 0:
    print(f"Well done. You guessed all {letter_counter} letters. You win the game")
else:
    print("Sorry you lose the game!")
