import re

sample = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]

def read_file(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]


# Solution to part 1
def calculate_pos_and_depth(commands):
    pos = 0
    depth = 0

    for command in commands:
        command = command.split()
        direction = command[0]
        distance = int(command[1])

        if re.match("forward", direction):
            pos += distance
        elif re.match("down", direction):
            depth += distance
        elif re.match("up", direction):
            depth -= distance

    return pos * depth 


# Solution to part 2
def calculate_pos_depth_and_aim(commands):
    pos = 0
    depth = 0
    aim = 0

    for command in commands:
        command = command.split()
        direction = command[0]
        distance = int(command[1])

        if re.match("forward", direction):
            pos += distance
            depth += aim * distance
        elif re.match("down", direction):
            aim += distance
        elif re.match("up", direction):
            aim -= distance

    return pos * depth   


def main():
    commands = read_file("day2.txt")
    print(calculate_pos_and_depth(commands))
    print(calculate_pos_depth_and_aim(commands))


if __name__ == "__main__":
    main()