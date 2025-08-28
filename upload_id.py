import tkinter as tk
from tkinter.filedialog import askopenfile

import consts

image=''
def upload_id(id_num):
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Please upload your ID picture as a PDF file")
    root.configure(bg="PeachPuff2")
    tk.Label(root, text="Hey beloved volunteer!", font=("Times New Roman", 20),
             bg="PeachPuff2").pack(pady=20)
    tk.Label(root, text="For verification we need your id picture. \n Our team will report back with an answer within two days. \n Thank you for understanding!",
             font=("Times New Roman", 12), bg="PeachPuff2").pack(pady=10)
    def file():
        image = askopenfile(mode='rb', filetypes=[('PDF File', '*.PDF')])
        if image is not None:
            consts.IMAGES[id_num]=image

    open = tk.Button(root, text="Load file here", command=lambda: file())
    open.pack()
    root.mainloop()

