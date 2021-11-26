Math = {}
while True:
    sth = input()
    if sth == '':
        break
    surname, name, mark = map(str, sth.split())
    Math[surname + ' ' + name] = mark
Inf = {}
while True:
    sth = input()
    if sth == '':
        break
    surname, name, mark = map(str, sth.split())
    Inf[surname + ' ' + name] = mark
Phizik = {}
while True:
    sth = input()
    if sth == '':
        break
    surname, name, mark = map(str, sth.split())
    Phizik[surname + ' ' + name] = mark
print(len(set(Math.keys()) - set(Inf.keys())))# + set(Phizik.keys())))