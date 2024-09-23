from pathlib import Path

from instruction_set import instruction_set


class InvalidOperandType(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class Operator:
    def __init__(self, operator: str) -> None:
        if operator[0].isalpha() and operator[-1] == ":":
            self.instruction = instruction_set["label"]

        elif operator.startswith("section"):
            self.instruction = instruction_set["section"]

        else:
            self.instruction = instruction_set[operator]

    def __str__(self) -> str:
        return f"{self.instruction}"

    def __repr__(self) -> str:
        return f"<Operator: {str(self)}>"


class Operand:
    MEMORY = {"name": "MEMORY", "prefix": "$#"}
    NUMERIC = {"name": "NUMERIC", "prefix": "#"}
    REGISTER = {"name": "REGISTER"}

    def __init__(self, operand: str) -> None:
        self.operand = operand

    def determine_type(self, operand: str) -> str:
        if operand.startswith(self.MEMORY["prefix"]):
            return self.MEMORY["name"]

        elif operand.startswith(self.NUMERIC["prefix"]):
            return self.NUMERIC["name"]

        else:
            return self.REGISTER["name"]

        raise InvalidOperandType(operand)

    def __str__(self) -> str:
        return f"{self.operand} ({self.determine_type(self.operand)})"

    def __repr__(self) -> str:
        return f"<Operand: {str(self)}>"


def peek_operator(line: str) -> Operator:
    line = line.split(";")[0]

    try:
        operator, line = line.split(" ", maxsplit=1)

        return Operator(operator.strip()), line.strip()

    except ValueError:
        return Operator(line.strip()), ""


def translate_line(line: str) -> str:
    """
    Translate english op-codes
    """

    operator, line = peek_operator(line)

    if operator.instruction.opcode == 28:
        line, term = [s.strip() for s in line.rsplit(",", maxsplit=1)]
        return operator, *[]

    elif operator.instruction.name == "halt" or operator.instruction.name == "end":
        return operator, 0

    else:
        try:
            operands = line.split(" ", maxsplit=1)
            return operator, *[Operand(op) for op in operands]

        except ValueError:
            raise ValueError(f"Unable to parse line: {line}")


def generate_byte_code(line: str) -> tuple:
    operator, *operands = translate_line(line)
    return operator, *operands


def compile_file(input_path: Path, output_path: Path | None = None) -> None:
    if not output_path:
        output_path = Path(input_path.parent / f"{input_path.stem}.bin")

    print(f"{ input_path = } -> { output_path = }")

    data = [generate_byte_code(line.strip()) for line in input_path.open("r").readlines() if line != "\n"]

    for d in data:
        print(d[0].instruction.name, d[1:])


compile_file(Path("programs/1.asm"))
