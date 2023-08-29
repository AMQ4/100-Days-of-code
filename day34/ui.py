import tkinter

THEME_COLOR = "#375362"


class QuizInterface:
    """
    This class provides the graphical user interface for the Quizzler game.
    It uses the tkinter library for GUI components and display.
    """

    def __init__(self):
        """
        Initialize the QuizInterface with tkinter components and styling.
        """
        self._root = tkinter.Tk()
        self._root.config(pady=20, padx=20)
        self._root.title("Quizzler")
        self._root.config(background=THEME_COLOR)

        # Create GUI components
        self._score = tkinter.Label(fg="#fff", text="Score: 0", font=("Arial", 18, "bold"), background=THEME_COLOR,
                                    highlightthickness=0)
        self._canvas = tkinter.Canvas(width=300, height=250, bg="#fff", highlightthickness=0, borderwidth=0)
        self._question = self._canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"), fill=THEME_COLOR,
                                                  width=228)
        self._true_image = tkinter.PhotoImage(file="./images/true.png")
        self._true = tkinter.Button(highlightthickness=0, image=self._true_image, borderwidth=0, bg=THEME_COLOR,
                                    activebackground=THEME_COLOR, cursor="hand2")
        self._false_image = tkinter.PhotoImage(file="./images/false.png")
        self._false = tkinter.Button(highlightthickness=0, image=self._false_image, borderwidth=0,
                                     activebackground=THEME_COLOR, cursor="hand2", bg=THEME_COLOR)

        # Place GUI components on the grid
        self._score.grid(column=0, row=0, columnspan=2)
        self._canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self._true.grid(column=0, row=2)
        self._false.grid(column=1, row=2)

    def set_question(self, question):
        """
        Update the displayed question on the canvas.
        :param question: The question text to be displayed.
        """
        self._canvas.itemconfig(self._question, text=question)

    def main_loop(self):
        """
        Start the main event loop to display the GUI.
        """
        self._root.mainloop()
