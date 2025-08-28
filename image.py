import tkinter
from tkinter import PhotoImage


def get_image(root):
    image = PhotoImage(file="help_togo.png")

    image_label = tkinter.Label(root, image)
    image_label.pack()

