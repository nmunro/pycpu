class InvalidMemoryLocation(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return f"<InvalidMemoryLocation: {str(self)}>"


class VM:
    def __init__(self, word_length: int = 8, total_size: int = 8) -> None:
        self.word_length = 8
        self.size = total_size
        self.memory = [
            ["00" for _ in range(int(self.size / self.word_length))]
            for _ in range(self.word_length)
        ]

    def _convert_memory_location(self, location: str) -> int:
        offset, value = location.split("x")
        offset = int(offset)
        value = int(value)

        if offset >= len(self.memory):
            raise InvalidMemoryLocation(f"Offset {offset} does not exist")

        if value >= self.word_length:
            raise InvalidMemoryLocation(f"Location {location} does not exist")

        return offset, value

    def read_memory_location(self, location: str) -> str:
        x, y = self._convert_memory_location(location)
        return self.memory[x][y]

    def write_memory_location(self, location: str, value: str) -> None:
        x, y = self._convert_memory_location(location)
        self.memory[x][y] = value

    def __str__(self) -> str:
        return "\n".join([
            f"{num}x{str(b).zfill(2)}: {self.memory[b]}"
            for num, b in enumerate(range(int(self.size / self.word_length)))
        ])

    def __repr__(self) -> str:
        return f"<VM: {str(self)}>"
