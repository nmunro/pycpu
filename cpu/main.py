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
        size=data["vm"]["size"],
    )

    display = Display(screen, width=80, height=24)
    machine = Machine(cpu=cpu, memory=memory, display=display)

    # Test display memory
    for y in range(24):
        for x in range(80):
            machine.display.write_byte(y, x, str(0))

    machine.display.write_byte(10, 10, "H")
    machine.display.write_byte(10, 11, "e")
    machine.display.write_byte(10, 12, "l")
    machine.display.write_byte(10, 13, "l")
    machine.display.write_byte(10, 14, "o")

    machine.display.close()

    print(f"Window dimensions: {screen.getmaxyx()}")

    print(machine.cpu)
    print(machine.cpu.registers)
    print(machine.memory)
    # print(machine.display)

    # print(machine.memory.read_memory_location("0x07"))
    # machine.memory.write_memory_location("0x07", "ff")
    # print(machine.memory.read_memory_location("0x07"))

    print(machine.memory.read_memory_location("1x07"))
    machine.memory.write_memory_location("1x07", "0c")
    print(machine.memory.read_memory_location("1x07"))
    print(machine.memory.read_memory_location("7x00"))

    machine.load("programs/1.bin")
    machine.boot()


if __name__ == "__main__":
    curses.wrapper(main)
