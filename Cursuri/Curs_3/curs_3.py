# Structuri de date
# Structura alternativa if

# # if fara identare
# a = 5
# b = 10
# # if a>b #
# #     print('a este mai mare decat b')
# #if else
# if a<b:
#     print('b este mai mare decat a')
# else:
#     print('Nu este mai mare')
#
# #if,elif,else
# if a<b:
#     print('b este mai mare decat a')
# elif a == b:
#     print('a egal cu b')
# else:
#     print('Nu este mai mare')
#
# # if cu operatori logici
# if a < b or a == b :
#     print('mesaj 1')
# else:
#     print('mesaj 2')

###############
# #Exercitiul 4
# RO: Daca un client are peste 65 de ani, atunci va beneficia de o reducere de 15%.
# Altfel, daca clientul nu are varsta de peste 65 de ani si calatoreste cu cel putin un copil,
# atunci acesta va beneficia de o reducere de 10%.
# Pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta sub 65 de ani) se va aplica
# o reducere de 10% daca acestia calatoresc iarna.
# De asemenea, pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (v

# varsta = int(input('Va rugam introduceti varsta: '))
# anotimp = str(input('Va rugam sa introduceti anotimpul in care calatoriti: '))
# clasa = int(input('Introduceti clasa: '))
# pretBilet = int(input('Introduceti pretul biletullui: '))
#
# if varsta > 65:
#     discount = 0.15
# else:
#     nrCopii = int(input('Introduceti numaul de copii care va insotesc: '))
#     if nrCopii >=1:
#         discount = 0.1
# if anotimp == 'iarna':
#     discount += 0.1
# if clasa == 1:
#     taxa = 0.03
# else:
#     taxa = 0.01
# pretBilet = pretBilet - pretBilet * discount + pretBilet * taxa
# print(discount, taxa, pretBilet)

'''
1. Lista
se defineste cu paranteze []
colectie de date ORDONATE, cu tipuri de date diferite sau de acelasi fel
are proprietatea de a fi mutabila
Actiuni asupra unei liste:
- adaugam elemente
- sterg elemente
- modificam un element de la un anumit index
- sa mutam un element la un anumit index
'''
# 1. declararea si initializarea unei liste goale
a = []
# 2  declararea si initializarea unei liste populate
a_prezenti = ['raul', 'simona', 'alex', 'dan', 'ramona1']
a_absenti = ['silviu', 'carmen', 'iulia','ramona,']
string_a = 'Ana are mere si este fericita'
a_split = string_a.split()
print(a_split)
# 3. accesarea elementelor din lista
print(f'Primul element din lista este: {a_prezenti[0]}')
print(f'Primul element din lista este: {a_absenti[0]}')
# accesarea ultimului element din lista
print(f'Ultimul element: {a_prezenti[len(a_prezenti)-1]}')
print(f'Ultimul element: {a_prezenti[-1]}')
# functia append (adauga la sfarsitul listei)
a_prezenti.append('adela')
print(a_prezenti)
# functia insert adauga pe pozitia denumita
a_absenti.insert(2, 'adela')
print(a_absenti)
# functia index returneaza pozitia unui index
print(a_absenti.index('iulia'))
# functia remove sterge un element
print(a_prezenti.remove('dan'))
print(a_prezenti)
# functia pop sterge un element pe baza pozitiei lui
print(a_absenti.pop(-1))
print(a_absenti)
# functia count numara de cate ori apare un element in lista
print(a_prezenti.count('simona'))

print(a_prezenti.extend(a_absenti))
print(a_prezenti)

# functia clear goleste continutul listei
# liste neomogene = tipuri de date diferite
liasta_neomogena = ['maria', 12, True, 15.3]

#*******************************************************************************

# 2. Seturi
# - structuri/colectii de date, NEORDONATE, imutabile (nu putem modoifica valorile lor)
# - definirea: cu o pereche de {}
# - operatii: accesa elementele, adauga elementele, sterge elementele

# 1. definirea unui set gol
set_col = set()
print(type(set_col))

# 2. definirea unui set populat
set_populat = {'caine', 'pisica', 'hamster', 'papagal'}
# accesarea unui element din set
# varianta cu operatorul IN
print('hamster' in set_populat)
assert 'hamster' in set_populat, 'Error: hamster nu este in set_populat'
# assert 'gaina' in set_populat, 'Error: hamster nu este in set_populat'

# functia add()
set_populat.add('gaina')
print(set_populat)
# # functia pop() = sterge un element la intamplare
# set_populat.pop()
# print(set_populat)
# functia remove() = sterge ce anume vrem noi si se executa daca elementul nu exista
# set_populat.remove('hamster')
# print(set_populat)

# functia discard() = executa fara eroare
set_populat.discard('broasca')
print(set_populat)

# functia update(); union(); clear()
#set_populat.update()

