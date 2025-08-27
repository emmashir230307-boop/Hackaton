from tkinter import *
import consts
def start_screen():
    list = []
    def button_command(list):
        text = entry_id.get()
        list.append(text)
        return list

    root = Tk()
    root.geometry("1000x600")
    root.title(f'{consts.APP_NAME}:)')
    root.configure(bg='lightblue')
    label = Label(root, text="Hello, Welcome to Help To Go!", font=("Times New Roman", 20), fg="darkblue")
    label.pack(pady=20)

    label = Label(root, text="Please enter your ID: ", font=("Times New Roman", 12))
    label.pack(pady=10)
    entry_id = Entry(root, width = 20)
    entry_id.pack(pady=10)
    Button(root, text = "Enter" , command = button_command(list)).pack()

    label = Label(root, text="Please enter your password: ", font=("Times New Roman", 12))
    label.pack(pady=10)
    entry_id = Entry(root, width = 20)
    entry_id.pack(pady=10)
    Button(root, text = "Enter" , command = button_command(list)).pack()

    mainloop()
    print(list)

def new_user():
    root = Tk()
    root.geometry("1000x600")
    root.title("Help To Go :)")
    root.configure(bg='pink')
    label = Label(root, text="Hello, Welcome to Help To Go! \n We are happy to have you here", font=("Times New Roman", 20), fg="darkblue")
    label.pack(pady=20)
    mainloop()


def worker_screen():
    root = Tk()
    root.geometry("400x400")
    root.title("Help To Go - WORKER ACCESS ONLY")
    root.configure(bg="orange")
    label = Label(root, text="Hello, worker", font=("Times New Roman", 20))
    label.pack(pady=20)
    label = Label(root, text="please verify if this user is legitimate", font=("Times New Roman", 10))
    label.pack(pady=20)

    v = IntVar()
    radio1 = Radiobutton(root, text='legitimate', variable=v, value=1).pack(anchor=W)

    radio2 = Radiobutton(root, text='not legitimate', variable=v, value=2).pack(anchor=W)
    selected_value = v.get()
    mainloop()

    print(f"Selected value: {selected_value}")


# master = Tk()
# Label(master, text='ID').grid(row=0)
# Label(master, text='password').grid(row=1)
# Entry(master).grid(row=0, column=1)
# id = Entry(master).get()
# print(id)
# Entry(master).grid(row=1, column=1)
# password = Entry(master).get()
#

# root = Tk()
# v = IntVar()
# Radiobutton(root, text='under 18', variable=v, value=1).pack(anchor=W)
# Radiobutton(root, text='18 and above', variable=v, value=2).pack(anchor=W)

new_user()