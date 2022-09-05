import string

print("Welcome! Lets Start!")
word = input("Please enter your word: ").upper()

def hangman():
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)

    lives = 7
    while len(word_letters) > 0 and lives > 0:
        print("You have ", lives,  " lives. Used letters are:", " ".join(used_letters))

        # to print our current word
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word is:", ' '.join(word_list))

        # the check
        user_letter = input("please enter your letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(" ")
            else:
                lives -=1
                print(f"Wrong guess.")
        elif user_letter in used_letters:
            print("\n You ve tried already this letter. Try another one.")
        else:
            print("Invalid guess")

    if lives ==0:
        print(" Sorry you ve lost")
    else:
        print("yay! You ve won. The word is: ", word)


print(hangman())








