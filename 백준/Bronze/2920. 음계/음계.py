A = list(map(int, input().split()))

code = None
if A[0] < A[1]:
    code = 'ascending'
else:
    code = 'descending'

for i in range(1, 7):
    if A[i] < A[i + 1] and code == 'descending':
        code = 'mixed'
        break
    if A[i] > A[i + 1] and code == 'ascending':
        code = 'mixed'
        break

print(code)
