# 1.Funcție care să calculeze și să returneze suma a două numere

x = 5
y = 7

def suma_numere(x, y):
    suma = x + y
    return (f'Suma celor doau numere este: {suma}')
print(suma_numere(x, y))

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

n = 5
if n % 2 == 0:
    print("True")
else:
    print("False")

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
prenume = 'dan'
nume = 'tudorache'
def dan_tudorache(prenume, nume):
    return len(prenume + nume)
print(dan_tudorache(prenume, nume))

# 4. Funcție care returnează aria dreptunghiului
lungime = 8
latime = 5
def aria_dreptunghi(lungime, latime):
    aria = lungime * latime
    return aria

print(f'Aria dreptunghiului este: {aria_dreptunghi(lungime, latime)}')

# 5. Funcție care returnează aria cercului
raza = 4
def aria_cerc(raza):
    aria = raza * raza * 3.14
    return aria
print(f'Aria dreptunghiului este: {aria_cerc(raza)}')

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
string = 'casa'
litera = 'd'
def caracter(string, litera):
    if litera in string:
        return True
    else:
        return False
print(caracter(string, litera))

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def nr_caractere(string):
    a = 0
    b = 0
    for x in string:
        if x == x.upper():
            a = a+1
        else :
            b = b+1
    print('Numarul de caractere lower case este: ', b)
    print('Numarul de caractere upper case este: ', a)

nr_caractere('StraDa')

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

lista = [-15, -10, -5, 0, 5, 10, 15]


def numere_pozitive(numere):
    lista_numere_pozitive = []
    for numar in numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive


print(numere_pozitive(lista))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

x = 5
y = 12
def numere(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    elif y > x:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print(f'Numerele sunt egale')
print(numere(x, y))












































