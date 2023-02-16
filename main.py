from module import Jatekos

jatekosok:list[Jatekos] = []

file = open(file='juve.txt', mode='r', encoding='utf-8')
for s in file: jatekosok.append(Jatekos(s))

print(f'igazolt jatekosok szama: {len(jatekosok)}')

m:int = 0
for i in range(1, len(jatekosok)):
    if jatekosok[i].szul > jatekosok[m].szul:
        m = i
print(f'legfiatalabb jatekos: {jatekosok[m].nev} ({2023-jatekosok[m].szul} eves)')

c:int = 0
for j in jatekosok:
    if j.nemzet != 'olasz': c += 1
print(f'osszesen {c} jatekos van, aki nem olasz')

d:dict[str, int] = {}
for j in jatekosok:
    if j.poszt not in d: d[j.poszt] = 1
    else: d[j.poszt] += 1
print('jatekosok szama posztonkent:')
for k, v in d.items():
    print(f'\t{k}: {v} fo')