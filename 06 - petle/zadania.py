import random
import time

"""
Napisz program, który wypisze ile lat miałeś/aś w kolejnych latach kalendarzowych odTwojego roku urodzenia. Program powinien wykorzystać zmienną wiek oraz pętle for z instrukcją range.
"""

# rok_urodzenia = int(input("Podaj swój rok urodzenia: "))

# wiek = 0

# for rok in range(rok_urodzenia, 2024):
#     print(f"W roku {rok} miałeś {wiek} lat.")
#     wiek += 1


"""
Zrób tabliczkę mnożenia.
"""

# for wiersz in range(1, 11):
#     linijka = ""

#     for kolumna in range(1, 11):
#         linijka += (str(wiersz * kolumna)).center(4)
    
#     print(linijka)

"""
Użyj pętli for, aby wydrukować wszystkie liczby parzyste od 1 do 20.
"""


"""
Zadanie 1.
Utwórz grę w zgadywanie losowej liczby, użytkownik jest informowany czy zgadł niżej niż cel bądź wyżej. (1 do 100) i za każdym razem gdy zgadł program zamraża się na pół sekundy.
"""

# losowa_liczba = random.randint(1, 100)

# while True:
#     odp = int(input("Podaj twoją odpowiedź: "))

#     if odp == losowa_liczba:
#         print("Zgadłeś!")
#         break
#     elif odp > losowa_liczba:
#         print("Nie zgadłeś, spróbuj niżej.")
#     else: 
#         print("Nie zgadłeś, spróbuj wyżej.")
    
#     time.sleep(0.5)


"""
Zadanie 2.
Napisz program w Pythonie, który używa pętli for do rysowania kwadratu o zadanej wielkości w terminalu. 

Użytkownik powinien podać liczbę, która będzie określać długość boków kwadratu, a program powinien go narysować z gwiazdek lub innego znaku.

Przykład dla kwadratu o boku 5:
*****
*   *
*   *
*   *
*****
"""

# dl_bok = int(input("Podaj długość boku: "))

# for i in range(dl_bok):
#     linia = ""
#     for j in range(dl_bok):
#         if i == 0 or i == dl_bok - 1:
#             linia += "*"
#         elif j == 0 or j == dl_bok -1:
#             linia += "*"
#         else:
#             linia += " "

#     print(linia)

# Divide and conquer - Dziel i zwyciężaj

# Przyjmij długość boku

# Rozpocznij pierwszą pętle i iteruj po wierszach
    # Utwórz nową zmienną z pustym tekstem

    # Utwórz drugą pętle i iteruj po kolumach


#Wydrukuj linijkę

"""
Zadanie 3.
Stwórz program, który przyjmuje od użytkownika liczbę całkowitą, a następnie używa pętli for do policzenia sumy wszystkich liczb parzystych od 1 do podanej liczby. Wynik powinien być wyświetlany na ekranie.
"""

liczba_koncowa = int(input("Podaj liczbę: "))
suma = 0
for liczba in range(0, liczba_koncowa + 1, 2):
    suma += liczba

print(f"Suma liczb parzystych od 0 do {liczba_koncowa} wynosi {suma}.")