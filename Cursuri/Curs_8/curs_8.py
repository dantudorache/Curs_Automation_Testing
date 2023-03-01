# MOSTENIREA
# EX 1
# class Chef ():
#     cutite = None
#     linguri = None
#     def __init__(self, nr_cutite):
#         self.cutite = nr_cutite
#     def make_salad (self):
#         print('salad')
#     def make_fries(self):
#         print('fries')
#
# class Chef2 ():
#     sort = 2
#
# class JapaneseChef (Chef):
#     def __init__(self, cantitate_alge, cutite):
#         self.alge = cantitate_alge
#         self.cutite = cutite
#     def make_sushi (self):
#         print('sushi')
#
# class ItalianChef (Chef, Chef2):
#     tava = 1
#     def make_pizza (self):
#         print('pizza')

# new_chef = Chef (4)
# new_chef.make_fries()
#
# japan_chef = JapaneseChef(10, 5)
# japan_chef.linguri = 6
# print(japan_chef.linguri)
# japan_chef.make_sushi()
# japan_chef.make_salad()
#
# mario_chef = ItalianChef(3)
# print(mario_chef.tava)
# print(mario_chef.sort)
# print(mario_chef.linguri)
# mario_chef.linguri = 15
# print(mario_chef.linguri)

# class Tokyo_Chef (JapaneseChef):
#     alge = 300

# san_chef = Tokyo_Chef(150, 7)
# san_chef.make_salad()

# EXEMPLU 2

# class Animale():
#     sunet = None
#     culoare = None
#     specie = None
#     varsta = 0
#     sunet_somn_mancare = None
#     def dormi(self):
#         print(f'Acum dorm {self.sunet_somn_mancare}')
#
#     def imbatranire(self):
#         self.varsta = varsta + 1
#         print(f'Acum am varsta de {self.varsta}')
#
# class Pisica (Animale):
#     toarce = 'DA'
#     vaneaza_soareci = None
#     def toarce_sa_ceri_mancare(self):
#         if self.toarce == 'DA':
#             self.sunet_somn_mancare = 'MIAU'
#             print(self.sunet_somn_mancare)
#
# pisica = Animale()
# pisica_mostenitoare = Pisica()
#
# pisica.sunet = 'Miau Miau'
# print(pisica.sunet)
# print(pisica_mostenitoare.sunet)
#
# pisica.dormi()
# pisica_mostenitoare.dormi()
# pisica.imbatranire()
# pisica_mostenitoare.imbatranire()
#
#################################################################################

# POLIMORFISM
# Polimorfism cu functii cu un numar indefinit de argumente

# print(len('abc'))
# print(len([1, 2, 3, 4]))

def suma_nr (*args):
    suma = 0
    for element in args:
        suma = suma + element
    return suma

# print(suma_nr(2,4))
# print(suma_nr(4,6,9))
# print(suma_nr(5,6,7,8))

def add (x, y=0, z=0):
    return x+y+z
# print(add(5,7,1))
# print(add(5,6))
# print(add(6))

# Polimorfism prin implementarea a

class America:
    limba = None
    imn = 'Imnul americii'
    drapel = 'drapel american'
    def printeaza_limba(self):
        print(f'limba care se vorbeste in a va fi {self.limba}')

class Romania:
    limba = 'romana'
    imn = 'Imnul romaniei'
    drapel = 'tricolor'
    def printeaza_limba(self):
        print(f'limba care se vorbeste in romania va fi {self.limba}')

# america = America()
# romania = Romania()
#
# america.printeaza_limba()
# romania.printeaza_limba()

# Polimorfism prin

class Pasare:
    def describe(self):
        print('sunt o pasare')
    def zboara(self):
        print('sunt o pasare deci zbor')

class Papagal(Pasare):
    def vorbeste(self):
        print(f'sunt o pasare si vorbesc deci sunt un papagal')

class Pinguin(Pasare):
    def zboara(self):
        print('nu pot zbura dar sunt frumos')

pasare_1 = Pasare()
pasare_1.describe()
pasare_1.zboara()
print('*******************************')
papagal_1 = Papagal()
papagal_1.describe()
papagal_1.zboara()
papagal_1.vorbeste()
print('************')
pinguin_1 = Pinguin()
pinguin_1.describe()
pinguin_1.zboara()













