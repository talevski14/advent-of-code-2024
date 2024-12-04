def find_xmas(text):
    counter = 0
    for i in range(len(text)):
        for j in range(len(text[i])):
            current = text[i][j]
            if current == 'X':
                if j + 3 < len(text[i]) and text[i][j + 1] == 'M' and text[i][j + 2] == 'A' and text[i][j + 3] == 'S':
                    counter += 1
                if j - 3 >= 0 and text[i][j - 1] == 'M' and text[i][j - 2] == 'A' and text[i][j - 3] == 'S':
                    counter += 1

                if i + 3 < len(text) and text[i + 1][j] == 'M' and text[i + 2][j] == 'A' and text[i + 3][j] == 'S':
                    counter += 1
                if i - 3 >= 0 and text[i - 1][j] == 'M' and text[i - 2][j] == 'A' and text[i - 3][j] == 'S':
                    counter += 1

                if j + 3 < len(text[i]) and i - 3 >= 0 and text[i - 1][j + 1] == 'M' and text[i - 2][j + 2] == 'A' and \
                        text[i - 3][j + 3] == 'S':
                    counter += 1
                if j + 3 < len(text[i]) and i + 3 < len(text) and text[i + 1][j + 1] == 'M' and text[i + 2][
                    j + 2] == 'A' and text[i + 3][j + 3] == 'S':
                    counter += 1

                if j - 3 >= 0 and i - 3 >= 0 and text[i - 1][j - 1] == 'M' and text[i - 2][j - 2] == 'A' and \
                        text[i - 3][j - 3] == 'S':
                    counter += 1
                if j - 3 >= 0 and i + 3 < len(text) and text[i + 1][j - 1] == 'M' and text[i + 2][j - 2] == 'A' and \
                        text[i + 3][j - 3] == 'S':
                    counter += 1
    return counter


if __name__ == "__main__":
    text = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        text.append(line)

    result = find_xmas(text)
    print(result)
