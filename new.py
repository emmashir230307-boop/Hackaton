from tkinter import *
from tkinter import messagebox
import consts, worker

def worker_or_user():
    Label(root, text="Please choose who you are: ", font=("Times New Roman", 12), bg="lightblue").pack(pady=10)
    win = Toplevel()
    var = StringVar()
    var.set(None)
    Radiobutton(win, text='Legitimate', variable=var, value='legitimate', bg="orange").pack(pady=5)
    Radiobutton(win, text='Not legitimate', variable=var, value='not_legitimate', bg="orange").pack(pady=5)

def start_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Hello, Welcome to Help To Go!",
          font=("Times New Roman", 20), fg="darkblue", bg="lightblue").pack(pady=20)

    worker_or_user()

    Label(root, text="Please enter your ID: ", font=("Times New Roman", 12), bg="lightblue").pack(pady=10)
    entry_id = Entry(root, width=20)
    entry_id.pack(pady=10)

    Label(root, text="Please enter your password: ", font=("Times New Roman", 12), bg="lightblue").pack(pady=10)
    entry_password = Entry(root, width=20, show="*")
    entry_password.pack(pady=10)

    def on_submit():
        id_num = entry_id.get()
        password = entry_password.get()
        start(root, id_num, password)

    Button(root, text="Login", command=on_submit).pack(pady=10)
    Button(root, text="Signup", command=lambda: signup(root, entry_id.get(), entry_password.get())).pack(pady=5)

def start(root, id_num, password):
    if not id_num.isdigit() or len(id_num) != 9:
        messagebox.showerror("Error", "Invalid ID. ID must be 9 digits.")
        return

    if id_num in consts.VOLUNTEER_DICT.keys():
        if password != consts.VOLUNTEER_DICT[id_num]['password']:
            messagebox.showerror("Error", "Wrong password.")
        else:
            messagebox.showinfo("Success", "Signed in successfully as volunteer!")

    elif id_num in consts.NEED_HELP_DICT.keys():
        if password != consts.NEED_HELP_DICT[id_num]['password']:
            messagebox.showerror("Error", "Wrong password.")
        else:
            messagebox.showinfo("Success", "Signed in successfully as user in need!")

    else:
        messagebox.showinfo("Info", "User not found, signing up...")
        signup(root, id_num, password)

def signup(root, id_num, password):
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Signup screen",
          font=("Times New Roman", 18), fg="darkblue", bg="lightblue").pack(pady=10)

    # קליטת עזרה
    Label(root, text="Enter your name:", bg="lightblue").pack(pady=5)
    entry_name = Entry(root, width=20)
    entry_name.pack(pady=5)
    Label(root, text="Enter your phone number:", bg="lightblue").pack(pady=5)
    entry_phone = Entry(root, width=20)
    entry_phone.pack(pady=5)
    Label(root, text="Who are you?", bg="lightblue").pack(pady=5)
    user_type_var = StringVar(root)
    user_type_var.set("who are you?")
    OptionMenu(root, user_type_var, *consts.USERS_TYPE2).pack(pady=5)
    Label(root, text="What type of help do you need?", bg="lightblue").pack(pady=5)
    help_type_var = StringVar(root)
    help_type_var.set("choose:")
    OptionMenu(root, help_type_var, *consts.HELP_OPTIONS).pack(pady=5)

    def on_submit():
        name = entry_name.get()
        phone = entry_phone.get()
        user_type = user_type_var.get().upper()
        help_type = help_type_var.get().upper()

        # בדיקות תקינות
        if not name.isalpha():
            messagebox.showerror("Error", "Invalid name. Use letters only.")
            return
        if not phone.isdigit() or len(phone) != 10 or phone[0] != "0" or phone[1] != "5":
            messagebox.showerror("Error", "Invalid phone number. Must be Israeli mobile.")
            return
        if user_type not in consts.USERS_TYPE:
            messagebox.showerror("Error", "Invalid user type.")
            return
        if help_type not in consts.HELP_OPTIONS:
            messagebox.showerror("Error", "Invalid help type.")
            return

        if user_type == consts.VOLUNTEER:
            if worker.legit():
                consts.VOLUNTEER_DICT[id_num] = {
                    'password': password,
                    'user type': user_type,
                    'help type': help_type,
                    'name': name,
                    'phone number': phone
                }
                messagebox.showinfo("Success", "Volunteer signed up successfully!")
            else:
                messagebox.showerror("Error", "Volunteer not approved.")
                return
        else:
            consts.NEED_HELP_DICT[id_num] = {
                'password': password,
                'user type': user_type,
                'help type': help_type,
                'name': name,
                'phone number': phone
            }
            messagebox.showinfo("Success", "User signed up successfully!")


    Button(root, text="Submit", command=on_submit).pack(pady=10)
    Button(root, text="Back to login", command=lambda: start_screen(root)).pack(pady=5)




root = Tk()
root.geometry("500x500")
root.title("Help To Go :)")
root.configure(bg='lightblue')

start_screen(root)
root.mainloop()
