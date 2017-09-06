
def count_pairs(words):
    num_pairs = 0
    counter = dict()
    for w in words:
        counter.setdefault(w, 0)
        if counter[w] == 2:
            num_pairs -= 1
        elif counter[w] == 1:
            num_pairs += 1
        counter[w] += 1
    return num_pairs


if __name__ == '__main__':
    s = ["hate", "love", "peace", "love", "peace", "hate", "love", "peace", "love", "peace"]
    print count_pairs(s)
    t = ["Om", "Om", "Shankar", "Tripathi", "Tom", "Jerry", "Jerry"]
    print count_pairs(t)