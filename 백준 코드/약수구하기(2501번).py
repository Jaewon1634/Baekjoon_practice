N,K = map(int, input().split())
group = []


for i in range(1, N+1):
    if N % i == 0:
        group.append(i)

if len(group) < K:
    print(0)
else : 
    print(group[K-1])