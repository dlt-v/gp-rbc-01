"""
lista - jak sama nazwa wskazuje jest strukturą danych, w której mamy sekwencje pewnych danych

przykładowo:
lista uczniów
1. Tomek
2. Adam
3. Bartek
...

lista ocen
4.5
3
6
2

lista wyników meczy

lista zakupów

Techniczne:
Lista w Pythonie może się zmniejszać bądź zwiększać - jej rozmiar jest dynamiczny.
Lista w Pythonie ma możliwość posiada w tej samej liście dane o różnych typach:
1. "Tomek"
2. "Bartek"
3. 43
4. True
5. 1. "Bartek"
   2. "Ania"

I choć jest to legalne - program na was nie będzie krzyczał - to jest to uważane za złą praktykę.
Najlepiej żeby lista była jednego typu.

Jak ogólnie zadeklarować listę:
nazwa_zmiennej = [a, b, c, d, e]
"""


"""
Elementy listy mają swój indeks - miejsce w liście.
Tak jak uczniowie mają swój numerek, tak samo element w liście ma swoją pozycję.

Tylko w przeciwieństwie do większość przypadków w realnym życiu, tutaj liczymy od 0.


lista_zakupow = ["jablka", "banany", "chleb", "bulki"]
ideksy            0         1         2        3

Za pomocą tych indeksów możliwe jest odczynie pojedynczych elementów.

"""

# lista_uczniow = ["Ania", "Bartek", "Czesław"]

# for element in lista_uczniow: # Drukowanie całej listy.
#     print(element)
   
# lista_uczniow[2] # Drukowanie trzeciego elementu w liście

# print(f"Drugi element w liście to: {lista_uczniow[1]}")

# lista_uczniow[1] = "Mieczysław" # Modyfikowanie elementów w liście

# print(f"Drugi element w liście to: {lista_uczniow[1]}")

# # UWAGA! Program może wyrzucić błąd jeżeli wyjdziemy poza indeks.

# print(lista_uczniow[5])

"""
Lista może się rozszerzać oraz zmniejszać dynamiczne.
"""

lista_imion = ["Ania", "Bartek", "Czesław"]
print(lista_imion)
print(f"Ilość imion: {len(lista_imion)}")

print()

lista_imion.append("Dominik") # Dodanie elementu do końca listy.
print(lista_imion)
print(f"Ilość imion: {len(lista_imion)}")

print()

lista_imion.pop(2) # Usuwanie elementu o N indeksie w liście.
print(lista_imion)
print(f"Ilość imion: {len(lista_imion)}")

print()

lista_imion.pop(-1) # Usuwanie elementu ostatniego w liście.
print(lista_imion)
print(f"Ilość imion: {len(lista_imion)}")

print()

lista_imion.insert(1, "Anielina") # "Wepchanie" elementu na N indeks.
print(lista_imion)
print(f"Ilość imion: {len(lista_imion)}")

print()

lista_imion.clear() # Czyszczenie listy
print(lista_imion)
print(f"Ilość imion: {len(lista_imion)}")

