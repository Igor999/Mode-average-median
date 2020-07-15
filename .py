ar = input().split()
ar = [int(i) for i in ar]
ar = sorted(ar)
n = []
m = []
c = 0
d = 0
for i in ar:
    if ar.count(i) >= c:
        c = ar.count(i)
        if i not in n:
            n.append(i)
        if ar.count(i) not in m:
            m.append(ar.count(i))
m = max(m)
for i in n:
    if ar.count(i) == m:
        print(str(i), end=" ")
print("\n")
res = 0
for i in ar:
    res += i
print("Среднее"+str(res/len(ar)))
if len(ar)%2 != 0:
    print("Медиана:",str(round(ar[len(ar)//2],1)))
else:
    print("Медиана:",str(round((ar[int(len(ar)/2)])+(ar[int(len(ar)/2-1)])/2,1)))  
