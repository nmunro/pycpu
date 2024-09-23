from pathlib import Path
import curses
import tomllib

from cpu import CPU, Register
from display import Display
from machine import Machine
from vm import VM


def main(screen):
    with Path("cpu_conf.toml").open("rb") as conf:
        data = tomllib.load(conf)

    registers = []

    for k, v in data["cpu"]["registers"].items():
        for num in range(int(v.get("count"))):
            if v.get("protected"):
                registers.append(Register(f"{k}", v.get("protected")))

            else:
                registers.append(Register(f"{v.get('prefix')}{num}", v.get("protected")))

    cpu = CPU(
        registers=registers,
        clock_speed=data["cpu"]["speed"],  # clock speed
        clock_freq=data["cpu"]["freq"],  # clock magnitude (hz, khz, mhz, etc)
        word_length=data["vm"]["word_length"],  # size of registers
    )

    memory = VM(
        word_length=data["vm"]["word_length"],
        total_size=data["vm"]["total_size"],
    )

    display = Display(screen, width=80, address="0x00000000")

    machine = Machine(cpu=cpu, memory=memory, display=display)

    machine.display.write_byte("H")
    machine.display.write_byte("e")
    machine.display.close()

    print(machine.cpu)
    print(machine.cpu.registers)
    print(machine.memory)
    print(machine.display)

    print(machine.memory.read_memory_location("0x07"))
    machine.memory.write_memory_location("0x07", "ff")
    print(machine.memory.read_memory_location("0x07"))

    print(machine.memory.read_memory_location("1x07"))
    machine.memory.write_memory_location("1x07", "0c")
    print(machine.memory.read_memory_location("1x07"))
    print(machine.memory.read_memory_location("7x00"))

    machine.load("programs/1.asm")


if __name__ == "__main__":
    curses.wrapper(main)
