
ALPHA = "abcdefghijklmnopqrstuvwxyz"

def number_needed(a, b):
    counter_a = [0]*len(ALPHA)
    counter_b = [0]*len(ALPHA)
    for c in a:
        counter_a[ALPHA.index(c)] += 1
    for c in b:
        counter_b[ALPHA.index(c)] += 1

    deletions = 0
    for i in range(len(ALPHA)):
        deletions += abs(counter_a[i]-counter_b[i])

    return deletions

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
