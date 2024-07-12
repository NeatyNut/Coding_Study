import sys
data = input().split("\n")
# input = sys.stdin.read
# data = input().split()
print(sorted(data[1].split(" "))[:int(data[0])])