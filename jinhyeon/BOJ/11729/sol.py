def hanoitop(start_rod, helper_rod ,end_rod, idx):
    if idx == 1:
        ans.append((start_rod, end_rod))
        rod[end_rod].append(rod[start_rod].pop())
    else:
        hanoitop(start_rod, end_rod, helper_rod, idx - 1)
        ans.append((start_rod, end_rod))
        rod[end_rod].append(rod[start_rod].pop())
        hanoitop(helper_rod, start_rod, end_rod, idx - 1)

k = int(input())
ans = []
rod = [[] for _ in range(4)]
rod[1] = list(range(k, 0, -1))

hanoitop(1, 2, 3, k)

print(len(ans))
for i in ans:
    print(' '.join(map(str,i)))