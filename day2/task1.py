def is_safe(numbers):
    for i in range(len(numbers) - 1):
        diff = numbers[i] - numbers[i + 1]
        if not (1 <= abs(diff) <= 3) or not (
                (numbers[0] < numbers[1] and diff < 0) or (not numbers[0] < numbers[1] and diff > 0)):
            return False
    return True


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    safe_lines = 0

    for line in lines:
        numbers = [int(item) for item in line.replace('\n', '').split(' ')]
        if is_safe(numbers):
            safe_lines += 1

    print(safe_lines)
