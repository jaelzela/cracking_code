def index_first_uno(l):
    low = 0
    high = len(l) - 1

    while low <= high:
        print 'low:', low, 'high:', high
        mid = (low + high)/2
        print 'mid:', mid, 'val:', l[mid], l[mid-1]
        if l[mid] == 1 and (mid == 0 or l[mid-1] == 0):
            return mid

        if l[mid] == 0:
            low = mid + 1

        if l[mid] == 1:
            high = mid - 1

    return -1


if __name__ == '__main__':
    s = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    print index_first_uno(s)
    t = [0, 0, 0, 0]
    print index_first_uno(t)
    u = [1]
    print index_first_uno(u)