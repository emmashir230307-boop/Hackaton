import connections
import new
import map
import consts
import tkinter as tk
from tkinter import *
import worker_screen

def main():
    root = Tk()
    root.geometry("500x500")
    root.title("Help To Go :)")
    root.configure(bg='lightblue')
    new.start_screen(root)
    root.mainloop()

if __name__ == '__main__':
    main()