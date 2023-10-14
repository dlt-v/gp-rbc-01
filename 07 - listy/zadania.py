"""
Zadanie 1:
Utwórz listę imion, zapełnij ją 5 imionami,

Za pomocą pętli for, wyświelt pojedyncze imiona oraz ich długość.
Użyj funkcji len() by otrzymać długość napisu.

["Paweł", "Ania"]

Paweł - 5
Ania - 4
...

Zadanie 2:

Utwórz listę zakupów, przynajmniej 5 elementów.
Wydrukuj te elementy wraz z ich indeksem.
0. Jabłka
1. Banany
2. Chleb
...

Potem zmień trzeciemu elementowi (indeks 2) na coś innego.

Wydrukuj drugi raz te elementy by zaobserwować zmianę.
0. Jabłka
1. Banany
2. Bułki
...
Czas do 11:15
"""

# lista_zakupow = ["Jabłka", "Banany", "Chleb", "Szynka", "Dżem"]

# i = 0
# for element in lista_zakupow:
#     print(f"{i}. {element}")
#     i += 1

# lista_zakupow[2] = "Bułki"

# i = 0
# for element in lista_zakupow:
#     print(f"{i}. {element}")
#     i += 1

"""
Zadanie 3
Użytkownik na żywo wpisuje elementy listy.
Natomiast jeżeli wpisze stop to kończymy wpisywanie do listy i ją wyświetlamy.

"""
lista = []

while True: # Wpisywanie elementów do listy.
    odp = input("Podaj następny element listy: ")

    if odp != "stop":
        lista.append(odp)
    else:
        print("Koniec wpisywania.")
        break

print() # Drukowanie listy.
print("Elementy listy: ")
i = 0
for element in lista:
    print(f"{i}. {element}")
    i += 1

