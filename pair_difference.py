def merge(s, t):
    result = []
    i = 0
    j = 0
    while len(s) > i and len(t) > j:
        if s[i] <= t[j]:
            result.append(s[i])
            i += 1
        else:
            result.append(t[j])
            j += 1

    while len(s) > i:
        result.append(s[i])
        i += 1

    while len(t) > j:
        result.append(t[j])
        j += 1

    return result


def merge_sort(x):
    if len(x) <= 1:
        return x

    q = len(x)/2
    s = merge_sort(x[0:q])
    t = merge_sort(x[q:len(x)])
    return merge(s, t)


def minimum_difference(s):
    a = merge_sort(s)
    min = 10000000
    i = 0
    for j in range(1,len(a)):
        if (a[j] - a[i]) < min:
            min = a[j] - a[i]
        i += 1
    return min

def minimum_pair_difference(s, t):
    s = merge_sort(s)
    t = merge_sort(t)

    labels = []
    sorted_list = []
    i = 0
    j = 0
    while len(s) > i and len(t) > j:
        if s[i] <= t[j]:
            sorted_list.append(s[i])
            labels.append(0)
            i += 1
        else:
            sorted_list.append(t[j])
            labels.append(1)
            j += 1
    while len(s) > i:
        sorted_list.append(s[i])
        labels.append(0)
        i += 1

    while len(t) > j:
        sorted_list.append(t[j])
        labels.append(1)
        j += 1

    print sorted_list
    print labels
    i = 0
    min = 1000000
    pair = None
    for j in range(1, len(sorted_list)):
        if sorted_list[j] - sorted_list[i] < min and labels[i] != labels[j]:
            min = sorted_list[j] - sorted_list[i]
            pair = (sorted_list[i], sorted_list[j])
        i += 1
    return pair

if __name__ == '__main__':
    a = [5, 3, 19, 18, 25, 99]
    #print minimum_difference(a)
    b = [9, 1, 31, 38, 25, 100]
    #print minimum_difference(b)
    print minimum_pair_difference(a, b)