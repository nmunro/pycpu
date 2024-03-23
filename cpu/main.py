from pathlib import Path
import tomllib

from cpu import CPU
from vm import VM
import instruction_set


def main():
    data = tomllib.load(Path("cpu_conf.toml").open("rb"))

    cpu = CPU(
        reg_count=data["cpu"]["registers"]["standard"]["count"],  # Number of registers
        reg_prefix=data["cpu"]["registers"]["standard"]["prefix"],  # Prefix of registers
        clock_speed=data["cpu"]["speed"],
        clock_freq=data["cpu"]["freq"],
    )
    cpu.memory = VM(
        word_length=data["vm"]["word_length"],
        total_size=data["vm"]["total_size"],
    )

    print(cpu)
    print(cpu.memory)

    print(cpu.memory.read_memory_location("0x07"))
    cpu.memory.write_memory_location("0x07", "ff")
    print(cpu.memory.read_memory_location("0x07"))

    print(cpu.memory.read_memory_location("1x07"))
    cpu.memory.write_memory_location("1x07", "0c")
    print(cpu.memory.read_memory_location("1x07"))

    print(cpu.memory.read_memory_location("7x00"))

    print(instruction_set.AND)


if __name__ == "__main__":
    main()
