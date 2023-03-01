# EX 2 Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
#variabilă :
#- string
#- int
#- float
#- bool

nume1 = 'Andrei' # variabila string
numar = 3       # variabila int
numar2 = 3.5    # variabila float
x = True        # variabila bool

# EX 3 Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(nume1))
print(type(numar))
print(type(numar2))
print(type(x))

# EX 4 Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
#aceeași variabilă (suprascriere):
#- Verifică tipul acesteia.

numar_rotunjit = round(numar2) # rotunjire variabila de tip float
print(numar_rotunjit)
print(type(numar_rotunjit))

# EX 5 Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești

nume1 = 'Andrei'
nume2 = 'Alex'
numar = 3
numar2 = 3.5

print(f'{nume1} este nepotul meu')
print(f'El are varsta de {numar} ani')
print(f'{nume2} este fratele lui {nume1}')
print(f'{nume2} are varsta de {numar2} ani')

# EX 6 Citește de la tastatură:
#- numele;
#- prenumele.
#Afișează: 'Numele complet are x caractere'.

nume = input('Nume: ')
prenume = input('Prenume: ')

print(f'Numele complet are {len(nume) + len(prenume)} caractere')

# EX 7 Citește de la tastatură:
#- lungimea;
#- lățimea.
#Afișează: 'Aria dreptunghiului este x'.

lungimea =int(input('lungime: '))
latimea =int(input('latime: '))

print(f'Aria dreptunghiului este x= {lungimea * latimea} metri patrati')

# EX 8 Având stringul: 'Coral is either the stupidest animal or the smartest rock':
#- afișează de câte ori apare cuvântul 'the';

prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.count(' the '))

#  EX 9 Același string.
# Folosindu-te de string-ul de la exercițiul 8, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”) si afișează pe ecran rezultatul

prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.replace('the', 'THE'))

# EX 10 Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.

prop = 'Coral is either the stupidest animal or the smartest rock'
assert prop.isdigit() is True, 'Propozitia nu are numere'

# Exercitii optionale ##################################################################################

# EX 1
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.

cuvant = input('Tasteaza un cuvant cu dimensiune impara: ')
print(f'Caracterul din mijloc este {cuvant[(len(cuvant)//2)]}')

#Ex_2 Folosind assert, verifică dacă un string este palindrom.

cuvant = 'are'
assert cuvant == cuvant[::-1]

#Ex_3 - Citește un string de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.

prop = input('Tasteaza doua cuvinte: ')
x, y = prop.split(' ')
print(f'Primul cuvant este {x} si ultimul cuvant este {y}')






