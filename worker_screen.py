from tkinter import *
from tkinter import messagebox

def worker_screen_func():
    win = Toplevel()
    win.geometry("400x300")
    win.title("Help To Go - WORKER ACCESS ONLY")
    win.configure(bg="orange")
    Label(win, text="Hello, worker", font=("Times New Roman", 20), bg="orange").pack(pady=20)
    Label(win, text="Please verify if this user is legitimate", font=("Times New Roman", 12), bg="orange").pack(pady=10)

    var = StringVar()
    var.set(None)
    Radiobutton(win, text='Legitimate', variable=var, value='legitimate', bg="orange").pack(pady=5)
    Radiobutton(win, text='Not legitimate', variable=var, value='not_legitimate', bg="orange").pack(pady=5)

    def on_submit():
        value = var.get()
        if value == 'legitimate':
            messagebox.showinfo("Info", "User approved.", parent=win)
        elif value == 'not_legitimate':
            messagebox.showwarning("Info", "User not approved.", parent=win)
        else:
            messagebox.showwarning("Info", "Please choose an option", parent=win)

    Button(win, text="Submit", command=on_submit).pack(pady=20)

# root = Tk()
# root.geometry("300x200")
# root.title("Main")
#
# Button(root, text="Open Worker Screen", command=worker_screen_func).pack(pady=50)
#
# root.mainloop()
