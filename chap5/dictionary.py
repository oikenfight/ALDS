n = int(input())
statements = [input().split() for i in range(n)]
inserts = []

for data in statements:
    if data[0] == 'insert':
        inserts.append(data[1])
        continue
    print('yes' if data[1] in inserts else 'no')
