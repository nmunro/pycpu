class Instruction:
    def __init__(self, name: str, opcode: int, operands: int) -> None:
        self.name = name
        self.opcode = opcode
        self.operands = operands

    def __str__(self) -> str:
        return f"{self.name} ({self.opcode})"

    def __repl__(self) -> str:
        return f"<Instruction: {str(self)}>"


HLT = Instruction("HLT", 0, 0)
NOP = Instruction("NOP", 1, 0)

ADD = Instruction("ADD", 101, 3)
SUB = Instruction("SUB", 102, 3)
MUL = Instruction("MUL", 103, 3)
DIV = Instruction("DIV", 104, 3)
MOD = Instruction("MOD", 105, 3)
INC = Instruction("INC", 106, 1)
DEC = Instruction("DEC", 107, 1)

JMP = Instruction("JMP", 201, 1)
JIF = Instruction("JIF", 202, 3)

EQL = Instruction("EQL", 301, 3)
GT = Instruction("GT", 302, 3)
GTE = Instruction("GTE", 303, 3)
LT = Instruction("LT", 304, 3)
LTE = Instruction("LTE", 305, 3)
AND = Instruction("AND", 306, 3)
OR = Instruction("OR", 307, 3)
NOT = Instruction("NOT", 308, 3)
MOV = Instruction("MOV", 309, 2)
