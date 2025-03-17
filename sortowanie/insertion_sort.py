def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            if (int(numbers[j]) < int(numbers[j - 1])):
                pom1 = numbers[j - 1]
                numbers[j - 1] = numbers[j]
                numbers[j] = pom1
    return numbers