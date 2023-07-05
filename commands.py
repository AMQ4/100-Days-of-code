import platform
import os

def clear():
    """Clears the terminal.

    This function uses the `os.system()` function to clear the terminal. The specific command that is used depends on the operating system. For Windows, the `cls` command is used. For other operating systems, the `clear` command is used.

    Args:
        None

    Returns:
        None
    """

    if platform.system() == 'Windows':
        os.system('cls')
        return
    os.system('clear')
