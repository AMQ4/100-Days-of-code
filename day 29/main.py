# Import required modules
from day5 import password_generator
from res import constant
import tkinter as tk
import tkinter.messagebox
import pyperclip  # pyperclip library for clipboard functionality

# Function to handle adding new data (website, username, and password)
def add():
    # Open the data file in append mode
    data = open("./res/data.txt", 'a')

    # Check if any of the input fields are empty, and display an error message if so
    if len(website.get().strip()) == 0 or len(uname.get().strip()) == 0 or len(password.get().strip()) == 0:
        tk.messagebox.showerror(title="Error", message="You should not leave any field empty.")
        return

    # Ask for user confirmation to save the data
    response = tk.messagebox.askokcancel(title=website.get(),
                                         message=f"Email: {uname.get()}\nPassword: {password.get()}")

    # If the user confirms, save the data to the file
    if response:
        data.write(f"{website.get()}|{uname.get()}|{password.get()}\n")

        # Clear the input fields after saving
        uname.delete(0, tk.END)
        password.delete(0, tk.END)
        website.delete(0, tk.END)

        # Copy the generated password to the clipboard using pyperclip
        pyperclip.copy(password.get())

    data.close()  # Close the file after writing

# Function to generate a random password and display it in the password entry field
def random_pass():
    global password
    if len(password.get()) != 0:
        password.delete(0, tk.END)
    password.insert(index=0, string=password_generator.generate(10, 4, 2))

# Create the main application window
root = tk.Tk()
root.title("Password Manager")
root.config(padx=75, pady=75)
root.config(bg="#fff")
root.resizable(False, False)

# Load the logo image from the constant module
logo = tk.PhotoImage(file=constant.LOGO)

# Create a canvas to display the logo image
canvas = tk.Canvas(width=200, height=200, highlightthickness=0, bg="#fff")
canvas.create_image(constant.LOGO_WIDTH // 2, constant.LOGO_HEIGHT // 2, image=logo)

# Create labels and entry fields for website, email/username, and password
label1 = tk.Label(text="Website:", bg="#fff")
label2 = tk.Label(text="Email/Username:", bg="#fff")
label3 = tk.Label(text="Password:", bg="#fff")

website = tk.Entry(width=35, bg="#fff")
website.focus()
uname = tk.Entry(width=35, bg="#fff")
password = tk.Entry(width=17, bg="#fff")

# Set a default email/username value (you can change this if needed)
uname.insert(tk.END, "example@email.com")

# Create buttons to generate a random password and to add the data
generatepassword = tk.Button(text="Generate Password", bg="#fff", pady=0, padx=5, command=random_pass)
add_button = tk.Button(text="Add", bg="#fff", width=35, padx=0, pady=0, command=add)

# Grid layout for placing the widgets on the window
label1.grid(column=0, row=1)
label2.grid(column=0, row=2)
label3.grid(column=0, row=3)
website.grid(column=1, row=1, columnspan=2, pady=3)
uname.grid(column=1, row=2, columnspan=2, pady=3)
password.grid(column=1, row=3, pady=3, padx=2)
generatepassword.grid(column=2, row=3, pady=3)
add_button.grid(column=1, row=4, columnspan=2, pady=3)
canvas.grid(column=1, row=0, columnspan=2)

# Start the main event loop of the application
tk.mainloop()
