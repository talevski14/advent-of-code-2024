if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    list1 = []
    list2 = []

    for line in lines:
        tmp = line.split(" ")
        list1.append(int(tmp[0]))
        list2.append(int(tmp[-1].replace("\n", "")))

    list1.sort()
    list2.sort()

    distance_sum = 0
    for a,b in zip(list1,list2):
        distance_sum += abs(a-b)

    print(distance_sum)