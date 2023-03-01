# #3. Tupluri
# # definire tuplu gol
# t = ()
# print(type (t))
# # definire tuplu populat
# t = ('mere', 'pere', 'nectarine', 'gutui','pere')
# print(t)
#
# # functii care se pot folosi cu tuplu
# # functia index
# print(t.index('nectarine'))
#
# # functia count
# print(t.count('pere'))
# print(t.remove('gutui')) # nu putem folosi remove pe un tuplu


# 4. Dictionare
# Elementele sunt de tip cheie-valoare
# cheile trebuie sa fie unice
# cheile servesc drept inlocuitori pt index
# sunt ordonate

## definirea unui dictionar gol
# d = {}
# print(type(d))

##3 definire unui dictionar populat
d = {
    'marca': 'audi',
    'model': 'tt',
    'an_fabricatie': 2010,
    'norma_euro': 'euro4',
    'combustibil': 'benzina',
}
print(d)

# functii
# accesarea elementelor dintr-un dictionar
print(f'numele masinii este {d["marca"]}')
print(f'modelul masinii este {d.get("model")}')

# adaugam elemente in dictionar
d['numar_de_locuri'] = 5
d.update({'numar_roti': 4})
updates = {'numar_roti': 4}
print(d)

ramona = {'centuri': True,}
d.update(ramona)
print(d)

# stergerea unui element din dictionar
# functia pop.
d.pop('norma_euro')
print(d)

# accesarea cheilor din dictionar
print(f'valorile proprietatilor masinii mele sunt:{d.values()}')
print(f'proprietatilor masinii mele sunt:{d.keys()}')

# accesarea perechilor cheie-valoare
print(f'dictionarul este format din urmatoarele elemente: {d.items()}')

# dictionar imdricat = dictionar in dictionar
apa_plata = {
    "borsec": {
        "nume": "borsec",
        "producator": "borsec",
        "cantitate_vanzare": "500ml",
        "impachetare": "baxuri"
    },
    "aqua carpatica": {
        "nume": "aqua carpatica",
        "cantitate_vanzare": "2l",
        "impachetare": "sticla"
    },
    "dorna":
        {
            "nume": "dorna",
            "producator": "dorna",
            "impachetare": "bax",
            "promovare": {"reclama": "Hai gata cu fotosinteza, la culcare toata lumea"},
            "televiziune promovare": ["tvr1", "tvr2", "acasa tv", "antena1"]
        }
}

print(apa_plata['aqua carpatica']['impachetare'])
print(apa_plata['dorna']['promovare']['reclama'])

# structuri repetitive:
# 1. structura while
# executam o serie de instructiuni atata timp cat o conditie este adevarata
# elementul sau variabila de control se declara in afara while-ului
# ex1: printati toate numerele de la 1 la 10
i = 1
while i <= 10:
    print(f'numarul curent este {i}')
    i+=1

# ex2: printam 101 dalmatieni
i = 1
while i <= 101:
    print(f'dalmatianul curent are numarul{i}')
    i+=1

# ex3. printati suma numerelor de la 1 la 10
i = 0
suma = 0
while i<=10:
    suma = suma + i
    i = i + 1
    print(suma)

# ex4: parcurgeti o lista si printati fiecare element
l1 = ['ramona', 'dan', 'alex', 'iulia', 'carmen', 'raul', 'ramona2', 'simona', 'silviu']
i = 0
while i < len(l1):
    print(l1[i])
    i += 1
print(len(l1))

# ex5 inlocuim silviu cu andreea
i = 0
while i < len(l1):
    if l1[i] == 'silviu':
        l1[i] = 'andreea'
    i += 1
    print(l1)

# ex6: inlocuim alex cu adela
i = 0
while i < len(l1):
    if l1[i] == 'alex':
        l1[i] = 'adela'
        break
    i += 1
print(l1)

# structura FOR
# este utilizata atunti cand vrem sa parcurgem o lista cu scopul de a modifica sau printa elementele
# - o mai utilizam atunci cand vrem sa executam un set de istructiuni de un numar de operatori
#
# structura unui FOR LOOP
# parcurgeti numerele de la 0 la 10 si printati-le pe cele pare

for i in range(0,11):

    if i % 2 == 0:
        print(i)
    else:
        print('nu este par')
















