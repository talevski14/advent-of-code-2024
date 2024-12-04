def find_mas(text):
    counter = 0
    for i in range(len(text)):
        for j in range(len(text[i])):
            current = text[i][j]
            if current == 'A' and 0 < i < len(text) - 1 and 0 < j < len(text[i]) - 1:
                if text[i - 1][j - 1] == 'M' and text[i + 1][j + 1] == 'S' or text[i - 1][j - 1] == 'S' and text[i + 1][
                    j + 1] == 'M':
                    if text[i + 1][j - 1] == 'M' and text[i - 1][j + 1] == 'S' or text[i + 1][j - 1] == 'S' and \
                            text[i - 1][j + 1] == 'M':
                        counter += 1
    return counter


if __name__ == "__main__":
    text = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        text.append(line)

    result = find_mas(text)
    print(result)
