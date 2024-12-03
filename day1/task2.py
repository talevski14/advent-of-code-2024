if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    list1 = []
    list2 = []

    for line in lines:
        tmp = line.split(" ")
        list1.append(int(tmp[0]))
        list2.append(int(tmp[-1].replace("\n", "")))

    similarity_score = 0
    for element in list1:
        similarity_score += element * list2.count(element)

    print(similarity_score)