def solution(n, lost, reserve):
    real_reserve = [r for r in reserve if r not in lost]
    
    real_lost = [l for l in lost if l not in reserve]
    
    for r in real_reserve:
        p = r - 1
        m = r + 1

        if p in real_lost:
            real_lost.remove(p)
        elif m in real_lost:
            real_lost.remove(m)
    return n - len(real_lost)
