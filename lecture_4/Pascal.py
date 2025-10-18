N = 9
P = []
 
for i in range(0, N):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]
 
    P.append(row)
last_row = ' '.join(f'{num:3}' for num in P[-1])
max_width = len(last_row)

for r in P:
    row_str = ' '.join(f'{num:3}' for num in r)  
    print(row_str.center(max_width))