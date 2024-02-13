# Project: Recreation of the popular WORDLE game
# Name: Akili Tulloch
# Thoughts: Happy I was able to accomplish this because I've wanted to recreate this game for a while,
# and it's nice to know I've learned enough to create something like this. Also, I feel like there are
# better alternatives than using the tkinter module.


import requests
from tkinter import *
from tkinter import messagebox

my_screen = Tk()
my_screen.title("Worldle!")
my_screen.config(bg="white", width=500, height=500)


def check_digit():
    for i in range(5):
        entry_list[current_row][i].config(state='disabled')
        if word_grid[current_row][i] in rand_word_letters:
            if word_grid[current_row][i] == rand_word_letters[i]:
                entry_list[current_row][i].config(disabledbackground="green")
            else:
                entry_list[current_row][i].config(disabledbackground="gold")
        else:
            entry_list[current_row][i].config(disabledbackground="grey")

    # BELOW CODE DOES NOT ACCOUNT FOR REPEATED LETTERS
    # for letter in word_grid[current_row]:
    #     index_position = word_grid[current_row].index(letter)
    #     for i in range(5):
    #         entry_list[current_row][index_position].config(state='disabled')
    #         if letter in rand_word_letters:
    #             if rand_word_letters[index_position] == letter:
    #                 entry_list[current_row][index_position].config(disabledbackground="green")
    #             else:
    #                 entry_list[current_row][index_position].config(disabledbackground="grey")


def check_word():
    if word_grid[current_row] == rand_word_letters:
        messagebox.showinfo(title="You won!", message=f"You got it correct! The word was {random_word}")
    if current_row >= 5:
        messagebox.showinfo(title="You lose!", message=f"HAHAHA! You lost dumbass!")


def update_board():
    global current_row
    global word_grid
    for i in range(5):
        word_grid[current_row][i] = entry_list[current_row][i].get()
    check_digit()
    check_word()
    print_board()
    current_row += 1


def print_board():
    for row in word_grid:
        print(row)


def validate(entry):
    if len(entry) == 0:
        return True
    elif len(entry) == 1 and entry.isalpha():
        return True
    else:
        return False


# should create an entry_list that looks like
# [[row0column0 entry, row0column1 entry, row0column2 entry...], [row1column0 entry, row1column1 entry,
# row1column2 entry], [row2column0 entry, row2column1entry...]...]
def create_board():
    vcmd = (my_screen.register(validate), '%P')
    for i in range(6):
        entry_list.append([])
        for j in range(5):
            entry = Entry(my_screen, width=5, font='Courier, 25', validate="key", validatecommand=vcmd)
            entry.grid(row=i, column=j)
            entry_list[-1].append(entry)
    enter_button = Button(text="Enter Word", width=55, command=update_board)
    enter_button.config()
    enter_button.grid(columnspan=5)


# using API to get a random word of the day
def get_wordle():
    url = "https://wordle-game-api1.p.rapidapi.com/word"
    headers = {
        "X-RapidAPI-Key": "ef6601ebc6mshcc642ccba90451ep1195d6jsn69cb049bcfbe",
        "X-RapidAPI-Host": "wordle-game-api1.p.rapidapi.com"
    }
    response = requests.get(url=url, headers=headers)
    return response.json()["word"]


random_word = get_wordle()
rand_word_letters = []
for digit in random_word:
    rand_word_letters.append(digit)

# establishing entry_list (a list of entries with column and row numbers), current_row keeps track of the row
# number the user is on (increments +1 after every guess), word_grid holds the values of word guesses to make
# for easy comparison
entry_list = []
current_row = 0
word_grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


create_board()

my_screen.mainloop()
