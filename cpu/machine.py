from functools import singledispatchmethod
from pathlib import Path


class Machine:
    def __init__(self, cpu, memory, display):
        self.cpu = cpu
        self.memory = memory
        self.display = display

    @singledispatchmethod
    def load(self, program) -> None:
        raise NotImplementedError()

    @load.register
    def _(self, program: str) -> None:
        self.load(Path(program))

    @load.register
    def _(self, program: Path) -> None:
        print(f"Loading: {program}")

    def boot(self, program: str) -> None:
        pass
