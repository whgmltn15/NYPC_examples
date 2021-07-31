import sys

Ti = []
for i in range(3):
    Ti.append(sys.stdin.readline())

N = int(input())

N1 = []
for i in range(N):
    N1.append(sys.stdin.readline())

for i in range(N):
    if N1[i] <= Ti[2]:
        print('***')
    elif N1[i] <= Ti[1]:
        print('**')
    if Ti[1] < N1[i] <= Ti[0]:
        print('*')
    elif N1[i] > Ti[0]:
        print(':(')

'''
01:00:00
00:50:00
00:40:00
6
01:00:00
00:49:99
00:30:00
00:45:00
00:55:00
01:00:01
'''