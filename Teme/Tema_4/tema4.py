# Ex 1
# Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
    print(f'Masina mea preferata este: {masini[i]}')

# for each
for masina in masini:
    print(f'Masina mea preferata este: {masina}')

# while
i = 0
while i < len(masini):
    print(f'Masina mea preferata este: {masini[i]}')
    i = i + 1

# Ex 2
# Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

for masina in range(1, len(masini)-1):
    masini[masina] = masini[masina].upper()
else:
    print(masini)

# Ex 3
# Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

for masina in masini:
    if masina == 'Mercedes':
        print(f'Am gasit masina dorita de dvs {masina}')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')


# Ex 4
# Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

for masina in masini:
    if masina == "Trabant" or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

# Ex 5
# Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.

masini_vechi = []

for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
        i = masini.index(masina)
        masini[i] = 'Tesla'
print('Modele vechi:', masini_vechi)
print('Modele noi:', masini)




























































