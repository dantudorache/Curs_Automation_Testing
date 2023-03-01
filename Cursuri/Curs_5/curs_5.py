# Functii
# # ex 1 for in for parcurgerea unei matrici
# my_list = [
# 		[1,"test1"],
# 		[2,"test2", 3, "test3"],
# 		[34,"test4"],
# 		[5]
# ]
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(f'valoarea curenta a elementului din lista de pe pozitia[{i}][{j}] este: {my_list[i][j]}')


# # EX 2: parcurgeti o lista de elemente, printati elementele pe ecran, daca intalniti stringul gutui inlocuitil cu caise
#
# list_2 = ['gutui', 'prune', 'mere', 'pere']
# for i in range(len(list_2)):
# 	print(list_2[i])
# 	if list_2[i] == 'gutui':
# 		list_2[i] = 'caise'
# print(list_2)

# # Ex 3: Avem o lista de culori. Si vrem sa vindem haine in culorile respective
# # 			# cand vine un cumparator vrem sa ii prezentam haine in culorile alese de el
# # 			# adica, daca cumparatorul ne spune ca nu ii place culoarea x, ii vom exclude de la prezentare hainele in culoarea respectiva
#
# culori_disponibile = ['rosu', 'roz', 'verde', 'galben', 'violet', 'magenta', 'maro', 'albastru']
# culori_nepotrivite = ['galben', 'albastru', 'maro']
#
# for culoare in range(len(culori_disponibile)):
#     if culori_disponibile[culoare] in culori_nepotrivite:
#         break
#     print(f'va recomandam haine in culoarea {culori_disponibile[culoare]}')

# # FUNCTIA FOR EACH
# # parcurge lista si daca intalnesti soarece, sterge-l
# animale = ['cal', 'pisica', 'caine', 'magar', 'soarece', 'oaie', 'vaca']
#
# for animal in range(len(animale)-1):
#     if animale[animal] == 'soarece':
#         animale.pop(animal)
# print(animale)
#
# # for each
# # nu putem folosi .pop pentru ca ia ca si parametru indexul
# # folosim .remove
# for animal in animale:
#     if animale == 'soarece':
#         animale.remove(animal)
# print(animale)

# # for else
# # printati toate nr pana la 5
#
# for i in range(6):
#     print(i)
# else:
#     print('am terminat')
#
# # WHILE
# # else este optional si se executa o singura data la final
# i = 0
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print('am terminat')

# FUNCTII

# # ex 1 functii simple
#
# def print_noapte_buna():
#     print('Noapte buna')
#     print('Este ora 8')
#
# # print_noapte_buna()
# #
# # print_noapte_buna()
# #
# # print_noapte_buna()
#
# x = print_noapte_buna()
# print(x)
#
# def print_noapte_buna1():
#     print('Noapte buna')
#     print('Este ora 8')
#     msg = 'sunt obosit'
#     return msg
# y = print_noapte_buna1()
# print(y)

# # ex: suma a doua numere
# # calculeaza_suma() #functia nu se poate apela inainte de a fi definita
# def calculeaza_suma():
#     a = 3
#     b = 4
#     suma = a + b
#     print(f'Suma celor doua numere este {suma}')
#     return suma
#
# # calculeaza_suma()
# x = calculeaza_suma()
# print(x)

# # functii cu parametrii
#
# def suma(a, b):
#     sum = a + b
#     print(f'suma celor doua numere este: {sum}')
#     return sum
#
# x = suma(2, 4)
# print(x)
#
# suma(2, 1)

# ex 2
# functii cu un numar indefinit de parametrii
def calculeaza_pretul(*nr):
    pret = 0
    for element in nr:
        pret = pret + element
    return pret


print(calculeaza_pretul(2, 6, 7))
print(calculeaza_pretul(1, 3))
print(calculeaza_pretul(1, 3, 9, 8, 6))




































































































































