import tkinter as tk
from tkinter import *




def DNA_count(text):
    A = 0
    T = 0
    G = 0
    C = 0
    for i in text:
        if i == "A":
            A += 1
        elif i == "T":
            T += 1
        elif i == "G":
            G += 1
        elif i == "C":
            C += 1
        else:
            pass
    return A,T,G,C
def get_text():
    text = entry.get()
    label.config(text="A: %s T: %s G: %s C: %s" % DNA_count(text))
    #print(DNA_count(text))
window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Count Bases", command=get_text)
button.pack()
print(get_text)
#DNA_counted = DNA_count(text)
label = tk.Label(window, text = " ")
label.pack()

window.mainloop()
