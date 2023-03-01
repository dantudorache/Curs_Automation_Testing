# # functii cu un numar indefinit de parametrii
# def calculeaza_pretul(*pret):
#     total = 0
#     for element in pret:
#         total = total + element
#     return total
#
#
# print(calculeaza_pretul(2, 6, 7))
# print(calculeaza_pretul(1, 3))
# print(calculeaza_pretul(1, 3, 9, 8, 6))

# functii cu kwargs <=> ** nume_argument
# sunt folosite pentru a parcurge dictionare si pt a opera cu ele
apa = {
    'borsec': {
        'nume': 'borsec',
        'producator': 'borsec',
        'imbuteliere': 'sticla'
    },
    'dorna':{
        'nume': 'dorna',
        'producator': 'dorna',
        'imbuteliere': 'peturi'
    }
}
def accesare_elemente_dictionar (**kwargs):
    for key,values in kwargs.items():
        print(f'detalii despre apa: {key}')
        for key_int,values_int in values.items():
            print(f'apa {key} are {key_int} : {kwargs[key][key_int]}')

accesare_elemente_dictionar(**apa)































































































































