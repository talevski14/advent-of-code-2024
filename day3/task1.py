import re


def find_mul(line):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return re.findall(pattern, line)


def calculate(mul):
    sum_of_mul = 0
    for x, y in mul:
        sum_of_mul += int(x) * int(y)
    return sum_of_mul


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    mul = []
    for line in lines:
        mul_in_line = find_mul(line)
        mul.extend(mul_in_line)

    solution = calculate(mul)
    print(solution)
