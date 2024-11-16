def combination(initial, remaining, l):
    if len(remaining) == 1:
        l.append(initial + remaining)
        return 
    for i in range(len(remaining)):
        combination(remaining[i] + initial,remaining[:i] + remaining[i+1:], l)
    return l

l = combination('', '()()()()()', [])
s = list(set(l))
s.sort()

for i in s:
    n = 0
    for j in i:
        if j == '(':
            n += 1
        if j == ')' and n == 0:
            n = -1
            break
        if j == ')':
            n -= 1
    if n == -1 or i[-1] == '(':
        continue
    else:
        print(i)