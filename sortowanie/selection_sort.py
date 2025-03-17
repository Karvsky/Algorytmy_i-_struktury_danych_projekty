def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        pom1 = i
        for j in range(i + 1, len(numbers)):
            if (numbers[pom1] > numbers[j]):
                pom1 = j
        pom2 = numbers[pom1]
        numbers[pom1] = numbers[i]
        numbers[i] = pom2
    return numbers
