ar = input().split()
ar = [float(i) for i in ar]
ar = sorted(ar)
n = []
m = []
c = 0
d = 0
res = 0
Me = 0
for i in ar:
    res += i
Sr = round((res/len(ar)),1)
print("Среднее: "+str(Sr))
if len(ar)%2 != 0:
    Me = round(ar[len(ar)//2],1)
    print("Медиана:",str(Me))
else:
    Me = round(((ar[int(len(ar)/2)])+(ar[int(len(ar)/2-1)]))/2,1)
    print("Медиана:",str(Me))    
for i in ar:
    if ar.count(i) >= c:
        c = ar.count(i)
        if i not in n:
            n.append(i)
        if ar.count(i) not in m:
            m.append(ar.count(i))
m = max(m)
mo = []
for i in n:
    if ar.count(i) == m:
        mo.append(i)
MOD = ""
if len(mo)==1:
    MOD += "Мода: "+str(int(mo[0]))
else:
    MOD = "Моды: "
    for i in mo:
        MOD += str(int(i))+" "
    MOD = MOD[:-1]
print(MOD)
ar_res = []
for i in mo:
    if i == Me:
        if "Мо=Ме" not in ar_res:
            ar_res.append("Мо=Ме")
    elif i < Me:
        if "Мо<Ме" not in ar_res:
            ar_res.append("Мо<Ме")
    elif i > Me:
        if "Мо>Ме" not in ar_res:
            ar_res.append("Мо>Ме")
    if i == Sr:
        if "Мо=Ср" not in ar_res:
            ar_res.append("Мо=Ср")
    elif i < Sr:
        if "Мо<Ср" not in ar_res:
            ar_res.append("Мо<Ср")
    elif i > Sr:
        if "Мо>Ср" not in ar_res:
            ar_res.append("Мо>Ср")
if Me==Sr:
    ar_res.append("Ме=Ср")
elif Me<Sr:
    ar_res.append("Ме<Ср")
elif Me>Sr:
    ar_res.append("Ме>Ср")
for i in ar_res:
    print(i)
