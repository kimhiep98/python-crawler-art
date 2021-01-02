from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import get_artists_info


window = Tk()

window.title("Welcome to crawler app")

window.geometry('750x500')


def clicked_setURL():
    if (txt_path.get() != ''):
        if (txt_url.get() != ''):
            get_artists_info.get_artists_info(txt_url.get(), txt_path.get())
            messagebox.showinfo('Message', "Crawl finished")

        else:
            messagebox.showinfo('Message', "Url mustn't be empty")

    else:
        messagebox.showinfo('Message', "Path mustn't be empty")


def clicked_setPath():
    filename = filedialog.askdirectory(initialdir="/", title="Select folder")
    txt_path.insert(0, filename)


# url crawl data
lbl_url = Label(window, text="URL: ")
lbl_url.place(relx=0.25, rely=0.25, anchor='center')
lbl_url.config(font=("Courier", 18))


txt_url = Entry(window, width=60)
txt_url.place(relx=0.53, rely=0.25, anchor='center')
# txt_url.config(font)

btn_url = Button(window, text="Get data", command=clicked_setURL)
btn_url.place(relx=0.82, rely=0.25, anchor='center')
# path save

lbl_path = Label(window, text="Save path: ")
lbl_path.place(relx=0.2, rely=0.4, anchor='center')
lbl_path.config(font=("Courier", 18))

txt_path = Entry(window, width=60)
txt_path.place(relx=0.53, rely=0.4, anchor='center')


btn_path = Button(window, text="Browser", command=clicked_setPath)
btn_path.place(relx=0.82, rely=0.4, anchor='center')


window.mainloop()
