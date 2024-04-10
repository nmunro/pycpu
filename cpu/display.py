class Display:
    def __init__(self, width: int = 80, address: str = "0x00000000"):
        self.width = width

    def __str__(self) -> str:
        return f"Basic Terminal (Width: {self.width})"

    def __repr__(self) -> str:
        return f"<Display: {str(self)}>"
