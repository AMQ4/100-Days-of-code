from res import constant
from card import Card
import pandas
import tkinter as tk
import random
from bidi.algorithm import get_display
import arabic_reshaper

timer = None


def flip(index):
    card.set_photo("./res/images/card_back.png")
    card.set_title(get_display(arabic_reshaper.reshape("بالعربية")), "#fff")
    card.set_word(get_display(arabic_reshaper.reshape(table[index]["Arabic"])), "#fff")
    table.pop(index)


def next_card():
    global timer
    if timer is not None:
        root.after_cancel(timer)
    card.set_photo("./res/images/card_front.png")
    card.set_title(get_display(arabic_reshaper.reshape("بالانجليزية")), "#000")
    i = random.randint(0, len(table))
    card.set_word(table[i]["English"], "#000")
    timer = root.after(3000, flip, i)


root = tk.Tk()
root.title("Flashy")
root.resizable(False, False)
root.config(bg=constant.BACKGROUND_COLOR)
root.config(padx=50, pady=50)

card = Card(width=constant.CARD_WIDTH, height=constant.CARD_HEIGHT, title="English")

true_image = tk.PhotoImage(file="res/images/right.png")
false_image = tk.PhotoImage(file="res/images/wrong.png")

true = tk.Button(highlightthickness=0, image=true_image, bg=constant.BACKGROUND_COLOR, borderwidth=0, command=next_card)
false = tk.Button(highlightthickness=0, image=false_image, bg=constant.BACKGROUND_COLOR, borderwidth=0,
                  command=next_card)

data = pandas.read_csv("./res/data/unigram_freq.csv")
# we can do:
# hash = {row.English: row.Arabic for (index, row) in data.iterrows()},
# but to select a random words in order, we have to generate the list of keys then choice a random
# one from it, I mean:
# english_words = list(hash.keys())
# and so no this good, but we can do better with.

table = data.to_dict(orient="records")

card.grid(column=0, row=0, columnspan=2, pady=20)
true.grid(column=1, row=1)
false.grid(column=0, row=1)

next_card()
root.mainloop()
