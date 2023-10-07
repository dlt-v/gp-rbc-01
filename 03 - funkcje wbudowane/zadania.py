"""
    Zadanie 1:
    Napisz program, który pozwala użytkownikowi przeliczać kwoty między różnymi walutami. Wykorzystaj jawne konwersje danych oraz funkcje input() do wprowadzania kursów wymiany walut.
    Czas do 13:30

    Zadanie 2:
    Napisz program, który znajduje najmniejszą liczbę z podanych przez użytkownika liczb całkowitych. Wykorzystaj funkcje input(), min().
    Czas do 13:35

    Zadanie 3:
    Napisz program, który zamienia wartości dwóch zmiennych. Wykorzystaj jawne konwersje danych.
    Czas do 13:40

    Zadanie 4:
    Napisz program, który pobiera od użytkownika 4 słowa i oblicza średnią długość słów i wyświetla wynik. Wykorzystaj funkcje input(), len().
    Czas do 13:50

    Zadanie 5:
    Napisz program, który pobiera od użytkownika rok jego urodzenia i oblicza jego wiek w latach oraz dniach. Wykorzystaj funkcje input(), int(), str(), len().
    Czas do 14:00

    Zadanie 6:
    Napisz program, który pobiera od użytkownika długość podstawy i wysokość trójkąta oraz oblicza jego pole powierzchni. Wykorzystaj funkcje input() i obliczenia matematyczne.
    Czas do 14:05


"""

# ilosc = float(input("Podaj ilość gotówki: "))
# kurs = float(input("Podaj kurs waluty: "))

# print(f"Waluta po zastosowaniu kursu wynosi: {ilosc * kurs}")

# a = int(input("Podaj liczbę 1: "))
# b = int(input("Podaj liczbę 2: "))
# c = int(input("Podaj liczbę 3: "))

# print(f"Najmniejsza podana liczba to: {min(a, b, c)}")

# a = 7 # a = 7
# b = "ala" # b = "ala"

# # a = "ala" b = 7
# print(a, b)

# temp = a
# a = b
# b = temp

# print(a, b)

# a = input("Podaj 1 słowo: ")
# b = input("Podaj 2 słowo: ")
# c = input("Podaj 3 słowo: ")

# srednia = (len(a) + len(b) + len(c)) / 3

# print(f"Średnia długość słów to: {srednia}")

# rok_urodzenia = int(input("Podaj rok urodzenia: "))
# wiek = 2023 - rok_urodzenia

# print(f"Masz {wiek} lat. W dniach to {wiek * 365} dni.")

podstawa = float(input("Podaj długość podstawy: "))
wysokosc = float(input("Podaj wysokość: "))

print(f"Pole trójkąta to {(podstawa * wysokosc) / 2}")