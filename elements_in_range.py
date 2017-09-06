
def num_elements(elements, i, j):
    count = 0
    for elem in elements:
        if elem >= i and elem <= j:
            count += 1
    return count


if __name__ == '__main__':
    arr = [1, 3, 3, 9, 10, 4]
    print num_elements(arr, 1, 4)
    print num_elements(arr, 9, 12)
