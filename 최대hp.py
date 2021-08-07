H, T = list(map(int, input().split()))
ah = []
c_hp = 0

for i in range(T):
    ah.append(list(map(int, input().split())))

    a = ah[i][0]
    h = ah[i][1]

    if i == 0:
        c_hp = H

    if a == 1:
        c_hp -= h
    elif a == 2:
        c_hp += h
    elif a == 3:
        c_hp += h

print(c_hp)

'''
10 3 
2 20
1 10
3 40
'''