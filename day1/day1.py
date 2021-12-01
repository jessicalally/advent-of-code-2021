def read_file(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        return [int(line.rstrip()) for line in lines]


def num_increases(data):
    count = 0

    for i, v in enumerate(data):
        if (i != 0 and v > data[i - 1]):
            count += 1
    
    return count 


def sliding_window(data):
    count = 0
    curr_sum = data[0] + data[1] + data[2]
    prev_sum = 0

    for i, v in enumerate(data):
        if (i != 0 and i < len(data) - 2):
            curr_sum -= data[i - 1]
            curr_sum += data[i + 2]

            if (curr_sum > prev_sum):
                count += 1

            prev_sum = curr_sum

    return count


def main():
    data = read_file("day1.txt")
    print(num_increases(data))
    print(sliding_window(data))


if __name__ == "__main__":
    main()