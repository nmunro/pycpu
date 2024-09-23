import curses


class Display:
    def __init__(self, screen, width: int = 80, address: str = "0x00000000"):
        self.width = width
        self.address = address
        self.screen = screen
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        self.screen.clear()

    def write_byte(self, b: str) -> None:
        self.screen.addstr(b)
        self.screen.refresh()

    def close(self) -> None:
        self.screen.getkey()
        self.screen.keypad(False)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def __str__(self) -> str:
        return f"Basic Terminal (Width: {self.width})"

    def __repr__(self) -> str:
        return f"<Display: {str(self)}>"
