N = int(input())
list = list(map(int, input().split()))
new = []
for i in list:
    i = i/max(list)*100
    new.append(i)

print(sum(new)/len(new))

