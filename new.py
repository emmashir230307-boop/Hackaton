from tkinter import *
from tkinter import messagebox
import consts, worker

def start_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Hello, Welcome to Help To Go!",
          font=("Times New Roman", 20), fg="darkblue", bg="lightblue").pack(pady=20)

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
            main_menu(root, "volunteer", id_num)

    elif id_num in consts.NEED_HELP_DICT.keys():
        if password != consts.NEED_HELP_DICT[id_num]['password']:
            messagebox.showerror("Error", "Wrong password.")
        else:
            messagebox.showinfo("Success", "Signed in successfully as user in need!")
            main_menu(root, "need_help", id_num)

    else:
        messagebox.showinfo("Info", "User not found, signing up...")
        signup(root, id_num, password)

def signup(root, id_num, password):
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Signup screen (new user)",
          font=("Times New Roman", 18), fg="purple", bg="lightblue").pack(pady=10)

    Label(root, text="Enter your name:", bg="lightblue").pack(pady=5)
    entry_name = Entry(root, width=20)
    entry_name.pack(pady=5)

    Label(root, text="Enter your phone number:", bg="lightblue").pack(pady=5)
    entry_phone = Entry(root, width=20)
    entry_phone.pack(pady=5)

    Label(root, text="What are you?", bg="lightblue").pack(pady=5)
    user_type_var = StringVar(root)
    user_type_var.set(consts.USERS_TYPE[0])
    OptionMenu(root, user_type_var, *consts.USERS_TYPE).pack(pady=5)

    Label(root, text="What type of help do you need/offer?", bg="lightblue").pack(pady=5)
    help_type_var = StringVar(root)
    help_type_var.set(consts.HELP_OPTIONS[0])
    OptionMenu(root, help_type_var, *consts.HELP_OPTIONS).pack(pady=5)

    def on_submit():
        name = entry_name.get()
        phone = entry_phone.get()
        user_type = user_type_var.get().upper()
        help_type = help_type_var.get().upper()

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

        if user_type == consts.DONOR:
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

        main_menu(root, user_type, id_num)

    Button(root, text="Submit", command=on_submit).pack(pady=10)
    Button(root, text="Back to login", command=lambda: start_screen(root)).pack(pady=5)

def main_menu(root, user_type, id_num):
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text=f"Main Menu ({user_type})",
          font=("Times New Roman", 18), fg="green", bg="lightblue").pack(pady=20)

    Button(root, text="View Profile", width=20,
           command=lambda: view_profile(root, user_type, id_num)).pack(pady=5)
    Button(root, text="Search Users", width=20,
           command=lambda: messagebox.showinfo("Search", "Search screen (to be implemented)")).pack(pady=5)
    Button(root, text="Settings", width=20,
           command=lambda: messagebox.showinfo("Settings", "Settings screen (to be implemented)")).pack(pady=5)
    Button(root, text="Logout", width=20, command=lambda: start_screen(root)).pack(pady=20)

def view_profile(root, user_type, id_num):
    for widget in root.winfo_children():
        widget.destroy()

    if user_type == consts.DONOR:
        user_data = consts.VOLUNTEER_DICT.get(id_num)
    else:
        user_data = consts.NEED_HELP_DICT.get(id_num)

    if not user_data:
        messagebox.showerror("Error", "User data not found!")
        main_menu(root, user_type, id_num)
        return

    Label(root, text=f"Profile ({user_type})", font=("Times New Roman", 18), fg="blue", bg="lightblue").pack(pady=10)
    for key, value in user_data.items():
        Label(root, text=f"{key}: {value}", bg="lightblue").pack(pady=2)

    Button(root, text="Back to Main Menu", command=lambda: main_menu(root, user_type, id_num)).pack(pady=10)



root = Tk()
root.geometry("500x500")
root.title("Help To Go :)")
root.configure(bg='lightblue')

start_screen(root)
root.mainloop()
