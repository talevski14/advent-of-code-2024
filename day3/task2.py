import re


def find_mul(line):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return re.findall(pattern, line)


def calculate(mul):
    sum_of_mul = 0
    for x, y in mul:
        sum_of_mul += int(x) * int(y)
    return sum_of_mul


def split_text(text):
    all_valid = []
    do_texts = text.split("do()")
    for do_text in do_texts:
        valid_text = do_text.split("don't()")[0]
        all_valid.append(valid_text)
    return all_valid


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    text = ""
    for line in lines:
        text += line.replace("\n", "")

    text = split_text(text)

    mul = []
    for line in text:
        mul_in_line = find_mul(line)
        mul.extend(mul_in_line)

    solution = calculate(mul)
    print(solution)
