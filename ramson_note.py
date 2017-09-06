def ransom_note(magazine, ransom):
    if len(ransom) > len(magazine):
        return False

    magazine_words = dict()
    for w in magazine:
        if w in magazine_words.keys():
            magazine_words[w] += 1
        else:
            magazine_words[w] = 1

    for w in ransom:
        try:
            if magazine_words[w] <= 0:
                return False
            magazine_words[w] -= 1
        except KeyError:
            return False

    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"