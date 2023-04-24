BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

# ---------------------------- FLASH CARD ------------------------------- #
data=pd.read_csv("words.csv")
to_learn=data.to_dict(orient='records')
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word,text=current_card["French"])
    flip_timer=window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title,text='English',fill="white")
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)



# ---------------------------- FlIP CARD ------------------------------- #




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("FLASH CARD")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, flip_card)

# card front canvas
canvas=Canvas(height=536,width=820,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_image = PhotoImage(file="card_front.png")
card_back_image=PhotoImage(file="card_back.png")
canvas_image=canvas.create_image(400, 260, image=card_front_image)
canvas.grid(row=0, column=0,columnspan=2)
# change card



"""buttons"""
# wrong button
wrong_button_image=PhotoImage(file='wrong.png')
wrong_button=Button(image=wrong_button_image,bd=0,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

# right button
right_button_image=PhotoImage(file='right.png')
right_button=Button(image=right_button_image,highlightthickness=0,bd=0,command=next_card)
right_button.grid(row=1,column=1)

"""labels"""
# french translated label
card_title=canvas.create_text(400, 150, text="French", fill="black", font=("arial",40,"italic"))
canvas.grid()
# french label
card_word=canvas.create_text(400, 263, text="trouve", fill="black", font=("arial",60,"bold"))
canvas.grid()



























window.mainloop()