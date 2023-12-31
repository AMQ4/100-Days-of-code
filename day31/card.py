import _tkinter
from tkinter import Canvas, PhotoImage

from res import constant


class Card(Canvas):
    def __init__(self, width=0, height=0, photo=None, title=None, word=None):
        """
        Initialize the Card object.

        Parameters:
            width (int): Width of the card.
            height (int): Height of the card.
            photo (PhotoImage): The initial photo to be displayed on the card if there.
            title (str): Initial title to be displayed on the card.
            word (str): Initial word to be displayed on the card.
        """
        super().__init__(height=height, width=width)

        self.config(highlightthickness=0, bg=constant.BACKGROUND_COLOR)
        self.__width = width
        self.__height = height
        self.__title_written = title if title is not None else ""
        self.__word_written = word if word is not None else ""

        self.__photo = PhotoImage() if photo is None else photo
        self.__image = self.create_image(self.__width // 2, self.__height // 2, image=self.__photo)

        self.__word = self.create_text(self.__width // 2, self.__height // 2, text=self.__word_written,
                                       font=constant.WORD_FONT)
        self.__title = self.create_text(self.__width // 2, self.__height // 6, text=self.__title_written,
                                        font=constant.TITLE_FONT)

    def set_photo(self, path):
        """
        Set a photo for the card.

        Parameters:
            path (str): Path to the photo file.
        """
        try:
            self.__photo.config(file=path)
        except _tkinter.TclError as message:
            print(message)

    def set_title(self, title, color="#000", font=constant.TITLE_FONT):
        """
        Set the title for the card.

        Parameters:
            title (str): The text to be displayed as the title.
            color (str): Text color (default is black).
            font (tuple): Font settings (default is TITLE_FONT).
        """
        self.itemconfig(self.__title, text=title, fill=color, font=font)
        self.__title_written = title

    def set_word(self, word, color="#000", font=constant.WORD_FONT):
        """
        Set the word text for the card.

        Parameters:
            word (str): The word text to be displayed on the card.
            color (str): Text color (default is black).
            font (tuple): Font settings (default is WORD_FONT).
        """
        self.itemconfig(self.__word, text=word, fill=color, font=font)
        self.__word_written = word

    def get_title(self):
        """
        Get the current title displayed on the card.

        Returns:
            str: The title text.
        """
        return self.__title_written

    def get_word(self):
        """
        Get the current word displayed on the card.

        Returns:
            str: The word text.
        """
        return self.__word_written
