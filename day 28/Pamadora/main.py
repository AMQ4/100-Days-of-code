# Import necessary libraries
from res import constant
import tkinter as tk
import pygame

# Global variables for controlling the timer and repetitions
rep = 1
timer = None


# Function to reset the timer and start a new session
def reset():
    global timer, rep
    # Reset the timer display to 00:00
    canvas.itemconfig(text_timer, text="00:00")
    # Cancel any ongoing timer
    if timer is not None:
        root.after_cancel(timer)
    # Reset the session status and repetition count
    status.config(text="Timer", fg=constant.GREEN)
    rep = 1
    period.config(text="")


# Function to start the timer based on the session type (work or break)
def start():
    if rep & 1 == 0:
        # If the current session is a break, start the next work session
        start_break()
    else:
        # If the current session is work, start the next break session
        start_period()


# Function to update the timer display during the session
def update_timer(ms):
    global timer, rep
    __ms = ms - 1
    min = ms // 60
    ms = ms % 60

    # Format the time in 00:00 format for display
    if min < 10:
        if ms < 10:
            time_in_00_00_format = f"0{min}:0{ms}"
        else:
            time_in_00_00_format = f"0{min}:{ms}"
    else:
        if ms < 10:
            time_in_00_00_format = f"{min}:0{ms}"
        else:
            time_in_00_00_format = f"{min}:{ms}"
    canvas.itemconfig(text_timer, text=time_in_00_00_format)

    # If there is still time remaining in the session, update the timer again after 1 second
    if __ms >= 0:
        timer = root.after(1000, update_timer, __ms)
    else:
        # If the session has ended, increment the repetition count
        rep += 1
        # Play different sounds based on the type of session (work or break)
        if rep & 1 == 0:
            if rep % 8 == 0:
                pygame.mixer.music.load("./res/coco.mp3")
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.load("./res/short_break.mp3")
                pygame.mixer.music.play()

            # Start the next break session
            start_break()
            # Add a check mark after each work session is done
            period.config(text=period.cget("text") + "✓")
        else:
            # Play the sound for the work session
            pygame.mixer.music.load("./res/work_session.mp3")
            pygame.mixer.music.play()
            # Start the next work session
            start_period()


# Function to start the break session
def start_break():
    global rep, timer

    if timer is not None:
        root.after_cancel(timer)

    # Set the appropriate status and timer display for the break session
    if rep % 8 == 0:
        status.config(text="Break", fg=constant.PINK, font=(constant.FONT_NAME, 36, "bold"), bg=constant.YELLOW)
    else:
        status.config(text="Break", fg=constant.RED, font=(constant.FONT_NAME, 36, "bold"), bg=constant.YELLOW)
    canvas.itemconfig(text_timer, text="20:00" if rep % 8 == 0 else "05:00")
    start_counting = constant.LONG_BREAK_MS if rep % 8 == 0 else constant.SHORT_BREAK_MS
    # Start counting down the timer for the break session
    timer = root.after(1000, update_timer, start_counting)


# Function to start the work session
def start_period():
    global timer

    if timer is not None:
        root.after_cancel(timer)

    # Set the appropriate status and timer display for the work session
    status.config(text="Work", fg=constant.GREEN, font=(constant.FONT_NAME, 36, "bold"), bg=constant.YELLOW)
    canvas.itemconfig(text_timer, text="25:00")
    start_counting = constant.WORK_MS
    # Start counting down the timer for the work session
    timer = root.after(1000, update_timer, start_counting)


# Initialize pygame for audio playback
pygame.init()

# Create the Tkinter root window
root = tk.Tk()
root.title("Pamadora")
root.config(bg=constant.YELLOW, pady=100, padx=200)
root.resizable(False, False)

# Create the Tkinter widgets for the timer application
status = tk.Label(text="Timer", fg=constant.GREEN, font=(constant.FONT_NAME, 36, "bold"), bg=constant.YELLOW)
period = tk.Label(fg=constant.GREEN, font=(constant.FONT_NAME, 30, "bold"), bg=constant.YELLOW)

image = tk.PhotoImage(file="./res/tomato.png")

canvas = tk.Canvas(width=200, height=223, highlightthickness=0, bg=constant.YELLOW)
canvas.create_image(100, 111, image=image)
text_timer = canvas.create_text(100, 130, text="00:00", font=(constant.FONT_NAME, 26, "bold"), fill="#fff")

start = tk.Button(text="start", bg="#fff", highlightthickness=0, command=start)
reset = tk.Button(text="reset", bg="#fff", highlightthickness=0, command=reset)

# Grid layout for the widgets
status.grid(column=1, row=0)
period.grid(column=1, row=4)
canvas.grid(column=1, row=1)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

# Start the Tkinter main loop
tk.mainloop()
