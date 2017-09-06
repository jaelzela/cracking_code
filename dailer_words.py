characters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


def words(numbers, index, word, n):
    if index == n:
        print word
        return

    for c in characters[numbers[index]]:
        word += c
        words(numbers, index + 1, word, n)
        word = word[:len(word)-1]


def suggest_words(numbers, n):
    words(numbers, 0, '', n)


if __name__ == '__main__':
    suggest_words([2, 3, 4, 5], 4)