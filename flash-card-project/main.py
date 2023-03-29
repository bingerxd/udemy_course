from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

try:
    file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    file = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = file.to_dict(orient="records")

current_word = {}

def generate_word():
    global current_word, timer
    screen.after_cancel(timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(text, text=current_word["French"], fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    screen.after_cancel(show_translation)
    timer = screen.after(2000, func=show_translation)

def show_translation():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(text, text=current_word["English"], fill="white")

def right_button_function():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",  index=False)
    generate_word()

screen = Tk()
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
screen.title("Flashy")

timer = screen.after(2000, func=show_translation)

canvas = Canvas(height=526, width=800)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
text = canvas.create_text(400, 263, text="French", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_button_function)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

generate_word()

screen.mainloop()
