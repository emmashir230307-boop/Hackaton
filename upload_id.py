import tkinter as tk

from tkinter.filedialog import askopenfile
def upload_id():
    root = tk.Tk()
    def file():
        image = askopenfile(mode='rb', filetypes=[('PDF File', '*.PDF')])
        if image is not None:
            content = image.read()
            print(content)

    open = tk.Button(root, text="Open Image", command=lambda: file())
    open.pack()
    root.mainloop()

upload_id()
