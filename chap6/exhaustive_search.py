def combine(A, m, s):
    for key, a in enumerate(A):
        t = s + a
        if t == m:
            return True
        elif t > m:
            continue
        else:
            if combine(A[key+1:], m, t):
                return True
    return False


if __name__ == "__main__":
    n = input()
    A = [int(a) for a in input().split()]
    q_num = int(input())
    M = [int(q) for q in input().split()]

    total = 0
    chars = 'sum: '
    for m in M:
        print('yes' if combine(A[:], m, 0) else 'no')

