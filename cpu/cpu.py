class Register:
    def __init__(self, name: str, protected: bool = False) -> None:
        self.name = name
        self.value = 0
        self.protected = protected

    def __str__(self) -> str:
        return f"{self.name}: {self.value}"

    def __repr__(self) -> str:
        return f"<Register: {str(self)}>"

class CPU:
    CLOCK_FREQUENCY_OPTIONS = [
        "hz",
        "khz"
        "mhz"
    ]

    def __init__(self, registers: list | None, clock_speed: int = 1, clock_freq: str = "hz", word_length: int = 8) -> None:
        self.word_length = word_length
        self.registers_count = 0
        self._registers = []

        for reg in [reg for reg in registers if reg.protected]:
            setattr(self, reg.name, reg)
            self.registers_count += 1
            self._registers.append(reg)

        for reg in [reg for reg in registers if not reg.protected]:
            setattr(self, reg.name, reg)
            self._registers.append(reg)

        self.speed = clock_speed
        self.freq = clock_freq

    @property
    def registers(self) -> str:
        return "\n".join([f"{getattr(self, reg.name)}" for reg in self._registers])

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, memory):
        self._memory = memory


    def fetch(self):
        pass

    def execute(self):
        pass

    def __str__(self) -> str:
        return f"{self.speed}{self.freq}, {self.registers_count} registers"

    def __repr__(self) -> str:
        return "<CPU: {str(self)}>"
