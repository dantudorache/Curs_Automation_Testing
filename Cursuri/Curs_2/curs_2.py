


poezie = 'Ana are mere si, este vesela pentru ca este miercuri'
# Extrage toate caracterele de la inceput pana la sfarsit cu specificarea pozitiei de start si de stop!

print(poezie[0:len(poezie)])# Pozitia de stop len(poezie) reprezinta defapt lungimea stringului poezie

print(poezie[:])# extragem toate caracterele de la incepot pana la sfarsit cu pozitie de start si de stop implicita sau default

print(poezie[::]) # extragem toate caracterele de la incepot pana la sfarsit cu pozitie de start si de stop si pas implicite sau default

# Extragem toate caracterele de la inceput pana la sfarsit
print(poezie[0:len(poezie):2])

print(poezie[::2])

# Extragem toate caracterele de la pozitia 5 pana la 13 inclusiv
print(poezie[5:14])

print(poezie[len(poezie)-3:len(poezie)])
# sau
print(poezie[-3:])

# printam stringul in ordine iversa
print(poezie[::-1])

# Metoda split = se returneaza o lista de elemente iar splitul se va face la fiecare cuvant
print(poezie.split(sep=','))
print(poezie.split(sep='L'))
print(poezie.split(sep=' '))

# Metoda replace inlocuim A cu m
print(poezie.replace('A','m'))
print(poezie.replace('Ana','Maria'))

# Metoda upper()
print(poezie.upper())
print(poezie.upper().replace('A','m'))

# Metoda index() si metoda find()
print(poezie.index('a'))
print(poezie.index('A'))

print(poezie.find('a'))

'''diferenta intre find si index este ca find returneaza -1
in cazul in care nu este gasit iar index ne returneaza o eroare '''

poezie = 'Ana are mere si, este vesela pentru ca este miercuri'

print(poezie.find('x'))
print(poezie.index('x'))

# metoda isnumeric(), metoda count() ss capitalize()
numeric='1234'
print(poezie.insnumeric())
print(numeric.insnumeric())

print(poezie.count('A'))
print(poezie.count('A'))

print(poezie.capitalize())

