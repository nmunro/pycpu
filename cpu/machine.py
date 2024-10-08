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
        with program.open("rb") as p:
            print(p.read())

    def boot(self) -> None:
        print("Attempting to boot cpu")
        self.cpu.run()
