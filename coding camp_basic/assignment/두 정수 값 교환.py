def exchange(a,b) :
    a, b = b, a
    return a, b

n, m = tuple(map(int,input().split()))
n, m = exchange(n,m)
print(n,m)