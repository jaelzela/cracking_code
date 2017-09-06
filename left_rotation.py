def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a % b)


def array_left_rotation(a, n, k):
    cd = gcd(k, n)
    for i in range(cd):
        temp = a[i]
        j = i
        while True:
            l = j + k
            if l >= n:
                l = l % n
            if l == i:
                break
            a[j] = a[l]
            j = l
        a[j] = temp
    return a

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))