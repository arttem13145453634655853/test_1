def sozd():
    ff = {}
    while True:
        sth = input()
        if sth == '':
            break
        surname, name, mark = map(str, sth.split())
        ff[surname + ' ' + name] = mark
    return(ff)


n = int(input('Введите количество олимпиад:'))
Olimps = [0] * n
for i in range(n):
    Olimps[i] = sozd()

f = set
for i in range(n):
    f = f.union(set(Olimps[i].keys()))
print(len(f))

DiktPoNum ={}
i = 1
for n in f:
    DiktPoNum[str(i) + '_' + n[0] + '_' + n.split()[1][0]] = n
    i += 1
print(DiktPoNum)

SpisVsOlimp = set
for i in range(len(Olimps)):
    if i == 1:
        SpisVsOlimp = set(Olimps[i].keys())
    else:
        SpisVsOlimp = SpisVsOlimp.intersection_update(set(Olimps[i].keys()))
print(SpisVsOlimp)

for i in SpisVsOlimp:
    sumB = 0
    for i in Olimps:

