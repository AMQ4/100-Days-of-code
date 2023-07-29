from res import constant
import tkinter as tk
import tkinter.messagebox
from day5 import password_generator


def add():
    data = open("./res/data.txt", 'a')

    if len(website.get().strip()) == 0 or len(uname.get().strip()) == 0 or len(password.get().strip()) == 0:
        tk.messagebox.showerror(title="Error", message="You should not let any field empty.")
        return

    response = tk.messagebox.askokcancel(title=website.get(),
                                         message=f"Email: {uname.get()}\nPassword: {password.get()}")

    if response:
        data.write(f"{website.get()}|{uname.get()}|{password.get()}\n")

        uname.delete(0, tk.END)
        password.delete(0, tk.END)
        website.delete(0, tk.END)

    data.close()


def random_pass():
    global password
    if len(password.get()) != 0:
        password.delete(0, tk.END)
    password.insert(index=0, string=password_generator.generate(10, 4, 2))


root = tk.Tk()
root.title("Password Manager")
root.config(padx=75, pady=75)
root.config(bg="#fff")
root.resizable(False, False)

logo = tk.PhotoImage(file=constant.LOGO)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0, bg="#fff")
canvas.create_image(constant.LOGO_WIDTH // 2, constant.LOGO_HEIGHT // 2, image=logo)

label1 = tk.Label(text="Website:", bg="#fff")
label2 = tk.Label(text="Email/Username:", bg="#fff")
label3 = tk.Label(text="Password:", bg="#fff")

website = tk.Entry(width=35, bg="#fff")
website.focus()
uname = tk.Entry(width=35, bg="#fff")
password = tk.Entry(width=17, bg="#fff")

uname.insert(tk.END, "example@email.com")

generatepassword = tk.Button(text="Generate Password", bg="#fff", pady=0, padx=5, command=random_pass)
add = tk.Button(text="Add", bg="#fff", width=35, padx=0, pady=0, command=add)

label1.grid(column=0, row=1)
label2.grid(column=0, row=2)
label3.grid(column=0, row=3)
website.grid(column=1, row=1, columnspan=2, pady=3)
uname.grid(column=1, row=2, columnspan=2, pady=3)
password.grid(column=1, row=3, pady=3, padx=2)
generatepassword.grid(column=2, row=3, pady=3)
add.grid(column=1, row=4, columnspan=2, pady=3)
canvas.grid(column=1, row=0, columnspan=2)

tk.mainloop()
