from instruction_set import instruction_set


class InvalidOperandType(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class Operator:
    def __init__(self, operator: str) -> None:
        print(instruction_set[operator])
        self.operator = operator

    def __str__(self) -> str:
        return f"{self.operator}"

    def __repr__(self) -> str:
        return f"<Operator: {str(self)}>"


class Operand:
    MEMORY = {"name": "MEMORY", "prefix": "$#"}
    NUMERIC = {"name": "NUMERIC", "prefix": "#"}
    REGISTER = {"name": "REGISTER", "prefix": "r"}

    def __init__(self, operand: str) -> None:
        self.operand = operand

    def determine_type(self, operand: str) -> str:
        if operand.startswith(self.MEMORY["prefix"]):
            return self.MEMORY["name"]

        elif operand.startswith(self.NUMERIC["prefix"]):
            return self.NUMERIC["name"]

        elif operand.startswith(self.REGISTER["prefix"]):
            return self.REGISTER["name"]

        raise InvalidOperandType(operand)

    def __str__(self) -> str:
        return f"{self.operand} ({self.determine_type(self.operand)})"

    def __repr__(self) -> str:
        return f"<Operand: {str(self)}>"


def translate_line(line: str) -> str:
    """
    Translate english op-codes to integer ones
    """

    # Split the operator
    operator, operands = line.split(" ", maxsplit=1)
    operator = Operator(operator)
    operands = [Operand(op) for op in operands.split(",")]

    print(f"{ operator = }, { operands = }")

    return line

print(translate_line("MOV #1,r0"))
print(translate_line("MOV #2,r1"))
print(translate_line("ADD r0,r1"))
