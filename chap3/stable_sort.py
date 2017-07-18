import re


def bubble_sort(C, N):
    for i in range(N):
        for j in reversed(range(1, N)):
            if C[j][1] < C[j - 1][1]:
                C[j], C[j - 1] = C[j - 1], C[j]
    return C


def selection_sort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C


def is_stable(C, sorted):
    c_container = []
    s_container = []
    for i in range(len(C)):
        for j in range(len(C)):
            if C[i][1] == C[j][1]:
                c_container.append(C[j][0])
        if len(c_container) >= 2:
            for k in range(len(sorted)):
                if sorted[k][1] == C[i][1]:
                    s_container.append(sorted[k][0])
            if c_container != s_container:
                return False
        c_container = []
        s_container = []
    return True


if __name__ == '__main__':
    N = int(input())
    cards = input().split()
    C = [[] for i in range(N)]
    for i in range(N):
        symbol_and_num = re.findall(r'(\d+|\D+)', cards[i])
        C[i] = [symbol_and_num[0], int(symbol_and_num[1])]

    bubble_sorted = bubble_sort(C.copy(), N)
    bubble_sorted_cards = [val[0] + str(val[1]) for val in bubble_sorted]
    print(' '.join(bubble_sorted_cards))
    print('Stable' if is_stable(C, bubble_sorted) else 'Not stable')

    selection_sorted = selection_sort(C.copy(), N)
    selection_sorted_cards = [val[0] + str(val[1]) for val in selection_sorted]
    print(' '.join(selection_sorted_cards))
    print('Stable' if is_stable(C, selection_sorted) else 'Not stable')
