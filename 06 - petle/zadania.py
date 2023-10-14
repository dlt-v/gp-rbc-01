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

for wiersz in range(1, 11):
    linijka = ""

    for kolumna in range(1, 11):
        linijka += (str(wiersz * kolumna)).center(4)
    
    print(linijka)

"""
Użyj pętli for, aby wydrukować wszystkie liczby parzyste od 1 do 20.
"""

"""
Zadanie 1.
Utwórz grę w zgadywanie losowej liczby, użytkownik jest informowany czy zgadł niżej niż cel bądź wyżej. (1 do 100) i za każdym razem gdy zgadł program zamraża się na pół sekundy.
"""

"""
Zadanie 2.
Napisz program w Pythonie, który używa pętli for do rysowania kwadratu o zadanej wielkości w terminalu. Użytkownik powinien podać liczbę, która będzie określać długość boków kwadratu, a program powinien go narysować z gwiazdek lub innego znaku.

Przykład dla kwadratu o boku 5:
*****
*   *
*   *
*   *
*****



"""


"""
Zadanie 3.
Stwórz program, który przyjmuje od użytkownika liczbę całkowitą, a następnie używa pętli for do policzenia sumy wszystkich liczb parzystych od 1 do podanej liczby. Wynik powinien być wyświetlany na ekranie.

"""