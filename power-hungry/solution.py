def solution(xs):
    if len(xs) == 1:
        return str(xs[0])
    l = [i for i in xs if i != 0]
    if len(l) == 0:
        return str(0)
    r = 1
    for i in l:
        r *= i
    if r < 0:
        l.remove(max([i for i in l if i < 0]))
        r = solution(l)
    return str(r)