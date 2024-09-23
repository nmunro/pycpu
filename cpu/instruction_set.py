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
instruction_set += Instruction("halt", 0, 0)
instruction_set += Instruction("nop", 1, 0)

instruction_set += Instruction("add", 2, 3)
instruction_set += Instruction("sub", 3, 3)
instruction_set += Instruction("mul", 4, 3)
instruction_set += Instruction("div", 5, 3)
instruction_set += Instruction("mod", 6, 3)
instruction_set += Instruction("inc", 7, 1)
instruction_set += Instruction("dec", 8, 1)

instruction_set += Instruction("jmp", 9, 1)
instruction_set += Instruction("jif", 10, 3)

instruction_set += Instruction("mov", 11, 2)
instruction_set += Instruction("move.b", 11, 2)
instruction_set += Instruction("move.w", 12, 2)
instruction_set += Instruction("move.l", 13, 2)

instruction_set += Instruction("eql", 14, 3)
instruction_set += Instruction("gt", 15, 3)
instruction_set += Instruction("gte", 16, 3)
instruction_set += Instruction("lt", 17, 3)
instruction_set += Instruction("lte", 18, 3)
instruction_set += Instruction("and", 19, 3)
instruction_set += Instruction("or", 20, 3)
instruction_set += Instruction("not", 21, 3)

instruction_set += Instruction("org", 22, 1)

instruction_set += Instruction("cmp", 23, 2)
instruction_set += Instruction("cmp.b", 23, 2)
instruction_set += Instruction("cmp.w", 24, 2)
instruction_set += Instruction("cmp.l", 25, 2)

instruction_set += Instruction("bra", 26, 1)
instruction_set += Instruction("beq", 27, 1)

instruction_set += Instruction("dc", 28, 2)
instruction_set += Instruction("dc.b", 28, 2)
instruction_set += Instruction("dc.w", 29, 2)
instruction_set += Instruction("dc.l", 30, 2)

instruction_set += Instruction("section", 31, 1)
instruction_set += Instruction("label", 32, 0)
instruction_set += Instruction("end", 33, 0)
