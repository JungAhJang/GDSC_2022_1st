n, k = tuple(map(int,input().split()))
arr = [0] * (n+1)

for _ in range(k) :
    Ai, Bi = tuple(map(int,input().split()))
    for i in range(Ai,Bi+1):
        arr[i] += 1

max_val = arr[0]
for elem in arr[1:] :
    if max_val < elem :
        max_val = elem
print(max_val)