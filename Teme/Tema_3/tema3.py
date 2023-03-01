# # 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# # Afiseaz-o
# # Inversează ordinea folosind slicing si suprascrie aceasta lista
# # Printeaza varianta actuala (inversata)
# # Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii inverseze ordinea.
#             # (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face asta automat)
# # Printeaza varianta actuala a listei. Practic ai ajuns înapoi la varianta inițială
# # Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o listă nouă.
#                 # Metoda gasita de tine face suprascrierea automat și permanentizeaza aceste modificări.
#                 # Ambele variante își găsesc utilitatea în funcție de ce ne dorim in acel moment.
#
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
#
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
#
# note_muzicale.reverse()
# print(note_muzicale)
#
#
# #2 Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
#
# print(note_muzicale.count('do'))

# #3 Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
# #
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
#
# lista_intreaga = list1 + list2
# print(lista_intreaga)
#
# list1.extend(list2)
# print(list1)
#
# #4 Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista folosind o functie si apoi afiseaza din nou lista
#
# lista_intreaga.sort()
# print(lista_intreaga)
# lista_intreaga.remove(0)
# print(lista_intreaga)
#
# #5 Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
# # Lista este goala (IF)
# # Lista nu este goala (ELSE)
#
# if len(lista_intreaga) >= 1:
#     print(f'lista nu este goala')
# else:
#     print(f'lista este goala')
#
# #6 Foloseste o functie care sa goleasca lista de la exercitiul 3
#
# lista_intreaga.clear()
# print(lista_intreaga)
#
# #7 Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala
#
# if len(lista_intreaga) >= 1:
#     print(f'lista nu este goala')
# else:
#     print(f'lista este goala')

# #8 Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa afisezi Elevii (cheile)
#
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())
#
# #9 Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
# # Ex: ‘Ana a luat nota {x}’.
# # Doar nota o vei lua folosindu-te de cheie
#
# print(f'Ana a luat nota {dict1["Ana"]}')
# print(f'Gigel a luat nota {dict1["Gigel"]}')
# print(f'Dorel a luat nota {dict1["Dorel"]}')
#
# # 10. Dorel a făcut contestație și a primit 6
# #  Modifică nota lui Dorel în 6
# #  Printează nota după modificare
#
# dict1['Dorel'] = 6
# print(dict1.get('Dorel'))
#
# #11 Imagineaza-ti ca Gigel se transfera din clasa.
# # Cauta o functie care sa il stearga
# # Vine un coleg nou.
# # Adaugati-l in lista pe Ionica, cu nota 9
# # Printati dictionarul cu noii elevi
#
# dict1.pop('Gigel')
# print(dict1)
#
# dict1['Ionica'] = 9
# print(dict1)

#12 Ai urmatoarele seturi:
#              zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
#              weekend = {'sambata', 'duminica'}
#  Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
#  Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(zile_sapt)

#13 Foloseste un if si verifica daca:
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt

if weekend.issubset(zile_sapt):
    print('weekend este un subset al zilelor sapt')
else:
    print('weekend nu este un subset al zilelor sapt')

#14. Afișează diferențele dintre aceste 2 seturi.

diferenta1 = zile_sapt.difference(weekend)
diferenta2 = weekend.difference(zile_sapt)
print(f'Diferenta intre zilele saptamanii si weekend este: {diferenta1}')
print(f'Diferenta intre weekend si zilele saptamanii este: {diferenta1}')

#15. Afișază intersecția elementelor din aceste 2 seturi.

intersectia = zile_sapt.intersection(weekend)
print(f'intersectia elementelor este {intersectia}')
















