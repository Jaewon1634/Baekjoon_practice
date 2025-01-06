# 내가 쓴 답안(시간초과)
import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers_B = sorted(set(numbers))
changed = []

for i in numbers:
    count = 0
    for j in range(len(numbers_B)):
        if numbers_B[j] < i:
            count += 1
    changed.append(count)

for i in changed:
    print(i, end=' ')


# 모범답안
import sys

N = int(input())
inputList = list(map(int,sys.stdin.readline().rstrip().split()))

sortedList = sorted(list(set(inputList)))
dictList = dict(zip(sortedList,list(range(len(sortedList)))))

for x in inputList:
    print(dictList[x])





