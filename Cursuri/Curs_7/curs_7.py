# from import1 import TestCase1, TestCase2, TestCase3
# import math # se cauta dupa modulul built-in (buit-in => in interiorul python) math apelandu-se functia import() <=>  __import__() si daca nu se gaseste, vom avea o eroare
# # modul python = un fisier care contine definitii si statements python, adica, functii, clase, variabile
#
# # from math import *
# # print(pi)
# # print(factorial(6))
#
# # from math import pi
# # print(pi)
#
#
# pie = math.pi
# print("The value of pi is : ",pie)
#
# child1 = TestCase1()
# child2 = TestCase2()
# child3 = TestCase3('test_case_nr_0003', 'the test case validate the design and functionality of [OK] button')
# child1.test_exe()
# child2.test_exe()
# print(child3.get_name())
# print(child3.get_summary())
# child3.test_exe()
# child3.runTwice()

#######################################################

class Masina:
    #definirea atributelor
    model = None
    culoare = 'Orange'
    marca = None
    vitez_max = 0
    an_fabricatie = 0
    capacitate_motor = 0
    serie_sasiu = None
    tip_combustibil = 'motorina'
    cutie_viteze = 'automata'
    viteza_curenta = 0

    # metodele
    # 1 constructor
    def __init__(self, marca1, model1, culoare1):
        self.marca = marca1
        self.model = model1
        if culoare1 == 'orange':
            self.culoare = 'portocaliu'
        #self.culoare = culoare

    # metode
    def paint(self, colour):
        self.culoare = colour

    def start_masina(self):
        self.viteza_curenta = self.viteza_curenta + 5
        print('masina s-a pus in miscare')
        return self.viteza_curenta

bmw = Masina('bmw', '1280', 'rosu')
print(bmw.culoare)
bmw.paint('verde')
print(bmw.culoare)
print(bmw.start_masina())

# cum accesez un atribut din interiorul unei clase? self.
# cum pot sa accesez atributele si metodele din afara clasei? bmw = Masina






























































































