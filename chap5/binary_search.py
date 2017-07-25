def binary_search(S, key):
    left = 0
    right = len(S)
    while left < right:
        mid = int((left + right) / 2)
        # 見つかったらその位置を return
        if S[mid] == key:
            return 'Found'
        # 真ん中の値より小さければ、先頭から真ん中に範囲を更新
        elif S[mid] > key:
            right = mid
        # 真ん中の値より大きければ、真ん中 + 1 から最後までに範囲を更新
        elif S[mid] < key:
            left = mid + 1
    return False

if __name__ == '__main__':
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    cnt = 0
    for key in T:
        if binary_search(S, key):
            cnt += 1

    print(cnt)
