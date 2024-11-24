import curses


class Display:
    def __init__(self, screen, width: int = 80, height: int = 24) -> None:
        self.screen = screen
        self.width = width
        self.height = height

        # Create a new window with the specified dimensions
        self.window = curses.newwin(height, width, 0, 0)

        curses.noecho()
        curses.cbreak()
        self.window.keypad(True)
        self.window.clear()

    def write_byte(self, y: int = 0, x: int = 0, s:str = "") -> None:
        if (y+1, x+1) != self.window.getmaxyx():
            self.window.addch(y, x, s)

        else:
            self.window.insch(y, x, s)

        self.window.refresh()

    def close(self) -> None:
        self.window.getkey()
        self.window.keypad(False)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def __str__(self) -> str:
        return f"Basic Terminal (Width: {self.width}, Height {self.height})"

    def __repr__(self) -> str:
        return f"<Display: {str(self)}>"

    def refresh(self) -> None:
        pass
