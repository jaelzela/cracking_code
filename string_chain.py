chars = 'abcdefghijklmnopqrstuvwxyz'

def build_chain(words, index):
    result = ''
    try:
        next_words = words[chars[index]]
    except KeyError:
        return result

    w = next_words.pop()
    c = w[-1]
    result += w + ' ' + build_chain(words, chars.index(c))
    return result


def string_chain(strings):
    words = dict()
    counts = [0]*26
    for s in strings:
        counts[chars.index(s[0])] += 1
        counts[chars.index(s[-1])] += 1
        if s[0] not in words.keys():
            words[s[0]] = []
        words[s[0]].append(s)

    print counts
    print words
    odd = 0
    start_index = []
    for i in range(len(counts)):
        if counts[i] % 2 != 0:
            odd += 1
            start_index.append(i)

    for i in start_index:
        chain = build_chain(words, i)
        print chain

    if odd == 2:
        return True

    return False


if __name__ == '__main__':
    a = ['aabb', 'bbcc', 'gcdd', 'ddee']
    print string_chain(a)