
import new

from tkinter import *


def main():
    root = Tk()
    root.geometry("500x500")
    root.title("Help To Go :)")
    root.configure(bg='lightblue')
    new.start_screen(root)
    root.mainloop()

if __name__ == '__main__':
    main()