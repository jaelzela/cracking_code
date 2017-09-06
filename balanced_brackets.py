def is_matched(expression):
    brackets = []
    for c in expression:
        if c in "([{":
            brackets.append(c)
        else:
            try:
                close = brackets.pop()
                if (c == ")" and close == "(") or (c == "]" and close == "[") or (c == "}" and close == "{"):
                    continue
                else:
                    return False
            except IndexError:
                return False
    if len(brackets) > 0:
        return False
    return True


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"