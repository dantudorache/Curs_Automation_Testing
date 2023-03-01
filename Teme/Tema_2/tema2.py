# Ex:1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

# daca conditie = True, se executa acest cod
# altfel, se executa acest cod

# Ex:2 - Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)

# x = 4
# if x >= 0:
#     print(f'x este numar intreg')
# else:
#     print(f'x nu este numar intreg')
#
# # Ex:3 - Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
#
# x = 4
# if x > 0:
#     print(f'x este numar pozitiv')
# elif x < 0:
#     print(f'x este numar negativ')
# else:
#     print(f'x este numar neutru')
#
# # Ex:4 - Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval)
#
# x = 4
# if x >= -2 and x <= 13:
#     print(f'x este in intervalul dorit')
# else:
#     print(f'x nu este in intervalul dorit')
#
# # Ex:5 - Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
#
# x = 14
# y = 10
# if x - y < 5:
#     print(f'diferenta este mai mica de 5')
# else:
#     print(f'diferenta nu este mai mica de 5')

# # Ex:6 - Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
#
# x = 4
# if not 5 <= x <= 27:
#     print(f'x NU este in intervalul 5 si 27')
# else:
#     print(f'x este in intervalul 5 si 27')
#
# # Ex:7 - Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare
#
# x = 6
# y = 4
#
# if x == y:
#     print(f'x si y sunt egale')
# elif x > y:
#     print(f'valoarea lui x este {x} si este mai mare decat valoarea lui y care este {y}')
# else:
#     print(f'valoarea lui x este {x} si este mai mic decat valoarea lui y care este {y}')

# # Ex:8 - Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi,
# # afiseaza daca triunghiul este isoscel (doua laturi sunt egale),
# # echilateral (toate laturile sunt egale)
# # sau oarecare (nicio latura nu e egala).
#
# x = 4
# y = 5
# z = 6
#
# if x == y or y == z or x == z:
#     print(f'Triunghiul este isoscel')
# elif x == y == z:
#     print(f'Triunghiul este echilateral')
# else:
#     print(f'Triunghiul este oarecare')
#
# # Ex:9 - Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu
#
# litera = input('tasteaza o vocala: ')
# litera = litera.lower()
# if litera.isdigit():
#     print(f'nu ai introdus o litera')
# elif litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
#     print(f'litera introdusa este o vocala')
# else:
#     print(f'litera introdusa este o consoana')

# # Ex:10 Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# # Peste 9 => A
# # Peste 8 => B
# # Peste 7 => C
# # Peste 6 => D
# # Peste 4 => E
# # 4 sau sub => F
#
# nota = float(input('Introduceti nota:'))
# if 9 < nota <= 10:
#     nota = 'A'
#     print(f'nota introdusa este nota {nota} in sistemul american')
# elif nota == 8:
#     nota = 'B'
#     print(f'nota introdusa este nota {nota} in sistemul american')
# elif nota == 7:
#     nota = 'C'
#     print(f'nota introdusa este nota {nota} in sistemul american')
# elif nota == 6:
#     nota = 'D'
#     print(f'nota introdusa este nota {nota} in sistemul american')
# elif nota == 4:
#     nota = 'E'
#     print(f'nota introdusa este nota {nota} in sistemul american')
# elif nota <= 4:
#     nota = 'F'
#     print(f'nota introdusa este nota {nota} in sistemul american')


#########   Exerciții Opționale


# # Ex:1 - Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#
# x = 1234
# if len(str(x)) == 4:
#     print('x are 4 cifre')
# else:
#     print('x nu are 4 cifre')
#
# # Ex:2 - Verifica daca x are exact 6 cifre
#
# x = 123456
# if len(str(x)) == 6:
#     print('x are 6 cifre')
# else:
#     print('x nu are 6 cifre')

# Ex:3 - Verifica daca x este numar par sau impar

x = 3
if x % 2 == 0:
    print(f'x este numar par')
else:
    print(f'x nu este impar')

# Ex:4 x, y, z (int).Afiseaza care este cel mai mare din ele.

x = 3
y = 4
z = 5

if x >= y and x >= z:
    print(f'{x} este cel mai mare')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare')
else:
    print(f'{z} este cel mai mare')




