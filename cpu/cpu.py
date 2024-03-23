class CPU:
    CLOCK_FREQUENCY_OPTIONS = [
        "hz",
        "khz"
        "mhz"
    ]

    def __init__(self, reg_count: int = 8, reg_prefix: str = "r", clock_speed: int = 1, clock_freq: str = "hz") -> None:
        self.registers_count = reg_count

        for reg in range(self.registers_count):
            setattr(self, f"{reg_prefix}{reg}", 0)

        self.speed = clock_speed
        self.freq = clock_freq
        self._memory = None

    @property
    def registers(self):
        return "\n".join([f"r{reg}: {getattr(self, f'r{reg}')}" for reg in range(self.registers_count)])

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

    def load(self):
        pass

    def boot(self, program: str):
        pass

    def __str__(self) -> str:
        return f"{self.speed}{self.freq}, {self.registers_count} registers"

    def __repr__(self) -> str:
        return "<CPU: {str(self)}>"
