import tkinter as tk


# Function to convert miles to kilometers and update the result label
def convert(event=None):
    result.config(text=f"{float(entry.get()) * 1.609}")


# Create the main application window
root = tk.Tk()
root.geometry("300x150")  # Set the window size to 300x150 pixels
root["bg"] = "#fff"  # Set the background color of the window to white
root["padx"] = 20  # Add horizontal padding (margin) of 20 pixels
root["pady"] = 20  # Add vertical padding (margin) of 20 pixels

# Create an entry widget to input miles
entry = tk.Entry(width=10)
entry.grid(column=1, row=0)  # Place the entry widget in column 1, row 0
entry.focus()  # Set focus to the entry widget for user convenience
entry.bind("<Return>", convert)  # Bind the Enter key event to the entry widget to trigger the conversion

# Create a label to display "mi" text
l = tk.Label(text="mi")
l.config(bg="#fff")
l.grid(column=2, row=0)  # Place the label in column 2, row 0
l.config(padx=5, pady=5)  # Add padding to the label for better appearance

# Create a label to display "is equal to" text
l1 = tk.Label(text="is equal to")
l1.grid(column=0, row=1)  # Place the label in column 0, row 1
l1["bg"] = "#fff"  # Set the background color of the label to white
l1.config(padx=5, pady=5)  # Add padding to the label for better appearance

# Create a label to display the converted kilometers
result = tk.Label(text="0")
result.grid(column=1, row=1)  # Place the label in column 1, row 1
result["bg"] = "#fff"  # Set the background color of the label to white
result.config(padx=5, pady=5)  # Add padding to the label for better appearance

# Create a label to display "km" text
l2 = tk.Label(text="km")
l2.grid(column=2, row=1)  # Place the label in column 2, row 1
l2["bg"] = "#fff"  # Set the background color of the label to white
l2.config(padx=5, pady=5)  # Add padding to the label for better appearance

# Create a button to trigger the conversion
button = tk.Button(text="convert")
button.grid(column=1, row=2)  # Place the button in column 1, row 2

# Start the Tkinter main event loop
tk.mainloop()
