class InvalidMemoryLocation(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return f"<InvalidMemoryLocation: {str(self)}>"


class VM:
    def __init__(self, word_length: int = 8, size: int = 8) -> None:
        if size % word_length != 0:
            raise ValueError(f"Size ({size}) must be divisible by word_length {word_length}")

        self.word_length = 8
        self.size = size

        for row in range(int(self.size / self.word_length)):
            for col in range(self.word_length):
                setattr(self, f"{row}x{str(col).zfill(2)}", "00")

    def read_memory_location(self, location: str) -> str:
        return self[location]

    def write_memory_location(self, location: str, value: str) -> None:
        self[location] = value

    def __str__(self) -> str:
        return f"Size: {self.size}, Word Length: {self.word_length}"

    def __repr__(self) -> str:
        return f"<VM: {str(self)}>"

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        if getattr(self, item):
            setattr(self, item, value)
