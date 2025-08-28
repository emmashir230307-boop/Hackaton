from tkinter import *
import consts
import menu


def start_screen2():
    list = []
    def button_command(list):
        text = entry_id.get()
        list.append(text)
        return list

    root = Tk()
    root.geometry("1000x600")
    root.title("Help To Go :)")
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

    var = StringVar()
    result = StringVar
    radio1 = Radiobutton(root, text='legitimate', variable=var, value=1)
    radio2 = Radiobutton(root, text='not legitimate', variable=var, value=2)
    selected_value = var.get()
    mainloop()

    print(f"Selected value: {selected_value}")


def start_screen3():
    result = {}

    def check_id(id_num,password):
        while not id_num.isdigit() or len(id_num) != 9:
            Label(root, text="Invalid ID. \n Please enter your ID: ", font=("Times New Roman", 12)).pack(pady=10)
            entry_id = Entry(root, width=20)
            entry_id.pack(pady=10)
        if id_num in consts.VOLUNTEER_DICT.keys():
            if password != consts.VOLUNTEER_DICT['ID']['[password']:
                Label(root, text="wrong password", font=("Times New Roman", 12)).pack(pady=10)
            else:
                Label(root, text="signed in successfully", font=("Times New Roman", 12)).pack(pady=10)

    def submit():
        result["data"] = (entry_id.get(), entry_password.get())
        root.quit()

    root = Tk()
    root.geometry("800x500")
    root.title("Help To Go :)")
    root.configure(bg='lightblue')
    Label(root, text="Hello, Welcome to Help To Go!", font=("Times New Roman", 20), fg="darkblue").pack(pady=20)

    #תעודת זהות
    Label(root, text="Please enter your ID: ", font=("Times New Roman", 12)).pack(pady=10)
    entry_id = Entry(root, width=20)
    entry_id.pack(pady=10)

    #סיסמא
    Label(root, text="Please enter your password: ", font=("Times New Roman", 12)).pack(pady=10)
    entry_password = Entry(root, width=20)
    entry_password.pack(pady=10)

    check_id(entry_id.get(), entry_password.get())
    Button(root, text="Login", command=submit).pack(pady=20)

    root.mainloop()
    root.destroy()

    return result.get("data")  # מחזירים את הטאפל



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

from tkinter import *
import consts  # נניח שהקובץ שלך עם המילונים נקרא consts.py

def start_screen():
    result = {}

    def on_submit():
        result["data"] = (entry_id.get(), entry_password.get())
        root.quit()

    root = Tk()
    root.geometry("500x300")
    root.title("Help To Go :)")
    root.configure(bg='lightblue')

    Label(root, text="Hello, Welcome to Help To Go!", font=("Times New Roman", 20), fg="darkblue").pack(pady=20)

    Label(root, text="Please enter your ID: ", font=("Times New Roman", 12)).pack(pady=10)
    entry_id = Entry(root, width=20)
    entry_id.pack(pady=10)

    Label(root, text="Please enter your password: ", font=("Times New Roman", 12)).pack(pady=10)
    entry_password = Entry(root, width=20, show="*")
    entry_password.pack(pady=10)

    Button(root, text="Login", command=on_submit).pack(pady=20)

    root.mainloop()
    root.destroy()

    return result.get("data")

def start(id_num, password):
    # בדיקה בסיסית על ת"ז
    while not id_num.isdigit() or len(id_num) != 9:
        print('Invalid id')
        id_num = input("Enter id number: ")

    # בדיקת משתמש במילון מתנדבים
    if id_num in consts.VOLUNTEER_DICT.keys():
        if password != consts.VOLUNTEER_DICT[id_num]['password']:
            print('Wrong password')
        else:
            print('signed in successfully')

    # בדיקת משתמש במילון נזקקים
    elif id_num in consts.NEED_HELP_DICT.keys():
        if password != consts.NEED_HELP_DICT[id_num]['password']:
            print('Wrong password')
        else:
            print('signed in successfully')

    # אם המשתמש לא קיים בשני המילונים
    else:
        menu.signup(id_num, password)

# ---------------- הפעלה ----------------
user_data = start_screen()
if user_data:
    user_id, user_password = user_data
    start(user_id, user_password)
