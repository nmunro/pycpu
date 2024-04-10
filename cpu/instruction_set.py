class Instruction:
    def __init__(self, name: str, opcode: int, operands: int) -> None:
        self.name = name
        self.opcode = opcode
        self.operands = operands

    def __str__(self) -> str:
        return f"{self.name} ({self.opcode})"

    def __repl__(self) -> str:
        return f"<Instruction: {str(self)}>"


class InstructionSet:
    def __init__(self, name: str) -> None:
        self.name = name

    def __getitem__(self, instruction_name: str) -> Instruction:
        return getattr(self, instruction_name)

    def __iadd__(self, instruction: Instruction) -> None:
        setattr(self, instruction.name, instruction)
        return self

instruction_set = InstructionSet("NMunro")
instruction_set += Instruction("HLT", 0, 0)
instruction_set += Instruction("NOP", 1, 0)

instruction_set += Instruction("ADD", 101, 3)
instruction_set += Instruction("SUB", 102, 3)
instruction_set += Instruction("MUL", 103, 3)
instruction_set += Instruction("DIV", 104, 3)
instruction_set += Instruction("MOD", 105, 3)
instruction_set += Instruction("INC", 106, 1)
instruction_set += Instruction("DEC", 107, 1)

instruction_set += Instruction("JMP", 201, 1)
instruction_set += Instruction("JIF", 202, 3)
instruction_set += Instruction("MOV", 203, 2)

instruction_set += Instruction("EQL", 301, 3)
instruction_set += Instruction("GT", 302, 3)
instruction_set += Instruction("GTE", 303, 3)
instruction_set += Instruction("LT", 304, 3)
instruction_set += Instruction("LTE", 305, 3)
instruction_set += Instruction("AND", 306, 3)
instruction_set += Instruction("OR", 307, 3)
instruction_set += Instruction("NOT", 308, 3)
instruction_set += Instruction("MOV", 309, 2)
