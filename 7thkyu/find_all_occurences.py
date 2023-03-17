def find_all(array, n):
    occurences = []
    for i in range(len(array)):
        if array[i] == n:
            occurences.append(i)
    return occurences