# Importing necessary libraries and modules
import random
import tkinter as tk

import arabic_reshaper
import pandas

from bidi.algorithm import get_display
from card import Card
from res import constant

# Global variables
timer = None
table = {}
i = 0


def load():
    global data
    """
    Load data from a CSV file into the 'table' dictionary and initialize the game.

    Returns:
        None
    """
    global table
    data = pandas.read_csv("./res/data/unigram_freq.csv")
    table = data.to_dict(orient="records")
    next_card()
    retry.grid_forget()
    card.grid(columnspan=3)
    false.grid(column=0, row=1)
    true.grid(column=2, row=1)


def reload():
    """
    Reset the card and show a message indicating the completion of 5000 English words.

    Returns:
        None
    """
    card.set_word(get_display(arabic_reshaper.reshape("تهانينا! لقد اتممت 5000 كلمة انجليزية للتو.")), color="#fff",
                  font=("Arial", 30, "normal"))
    card.set_title("")
    card.set_photo("./res/images/card_back.png")
    false.grid_forget()
    true.grid_forget()
    retry.grid()
    card.grid(columnspan=1)


def save():
    """
    Save the remaining words in the 'table' dictionary to a CSV file and close the application window.

    Returns:
        None
    """
    if len(table) != 0:
        unused = pandas.DataFrame(table)
        unused = pandas.DataFrame({
            "English": unused["English"],
            "Arabic": unused["Arabic"]
        })
        unused.to_csv("./res/data/unused.csv")
    root.destroy()


def flip(index):
    """
    Flip the card to show the Arabic translation for the selected word.

    Parameters:
        index (int): Index of the word in the 'table' dictionary to flip.

    Returns:
        None
    """
    card.set_photo("./res/images/card_back.png")
    card.set_title(get_display(arabic_reshaper.reshape("بالعربية")), "#fff")
    card.set_word(get_display(arabic_reshaper.reshape(table[index]["Arabic"])), "#fff")


def know():
    """
    Remove the current word from the 'table' dictionary and move to the next card.

    Returns:
        None
    """
    global table
    table.pop(i)
    next_card()


def next_card():
    """
    Show the next word in the card and set a timer to flip the card after 3 seconds.

    Returns:
        None
    """
    global timer, i
    if timer is not None:
        root.after_cancel(timer)
    if len(table) == 0:
        reload()
    else:
        card.set_photo("./res/images/card_front.png")
        card.set_title(get_display(arabic_reshaper.reshape("بالانجليزية")), "#000")
        i = random.randint(0, len(table) - 1)
        card.set_word(table[i]["English"], "#000")
        timer = root.after(3000, flip, i)


# Creating the Tkinter root window
root = tk.Tk()
root.title("Flashy")
root.resizable(False, False)
root.config(bg=constant.BACKGROUND_COLOR)
root.config(padx=50, pady=50)

# Creating the card and buttons
card = Card(width=constant.CARD_WIDTH, height=constant.CARD_HEIGHT, title="English")

true_image = tk.PhotoImage(file="res/images/right.png")
false_image = tk.PhotoImage(file="res/images/wrong.png")
retry_image = tk.PhotoImage(file="./res/images/reload.png")
retry = tk.Button(image=retry_image, command=load, bg=constant.BACKGROUND_COLOR, borderwidth=0, highlightthickness=0,
                  activebackground=constant.BACKGROUND_COLOR, cursor="hand2")
true = tk.Button(highlightthickness=0, image=true_image, bg=constant.BACKGROUND_COLOR, borderwidth=0, command=know,
                 activebackground=constant.BACKGROUND_COLOR, cursor="hand2")
false = tk.Button(highlightthickness=0, image=false_image, bg=constant.BACKGROUND_COLOR, borderwidth=0,
                  command=next_card, activebackground=constant.BACKGROUND_COLOR, cursor="hand2")

# Placing the card and buttons on the grid
card.grid(column=0, row=0, columnspan=3, pady=20)
false.grid(column=0, row=1)
true.grid(column=2, row=1, padx=0)
retry.grid(column=1, row=1)

# Loading data from a CSV file into the 'table' dictionary and initializing the game
data = pandas.read_csv("./res/data/unused.csv")
table = data.to_dict(orient="records")
retry.grid_forget()
next_card()

# Binding the save function to the window close event
root.protocol("WM_DELETE_WINDOW", save)

# Start the Tkinter main event loop
root.mainloop()
