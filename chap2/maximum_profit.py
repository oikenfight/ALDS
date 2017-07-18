N = int(input())
R = [int(input()) for i in range(N)]

maxv = -20000000000
minv = R[0]

for i in range(1, N):
    maxv = max(R[i] - minv, maxv)
    minv = min(R[i], minv)

print(maxv)