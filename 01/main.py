# # Struktura danych

# imie = "Tomek" # Napis / String

# # Typy Danych (Prymitywne)

# wiek = 23 # Liczba Całkowita / Integer / Int
# wzrost = 1.80 # Liczba Zmiennoprzecinkowa / Floating Point Number / Float
# bool = True # False / Bool

# Wprowadzanie danych za pomocą terminala

# print("Jak masz na imię? ") # Drukowanie do terminala
# imie = input() # Pobieranie informacji z terminala

# print("Cześć " + imie)

# Instrukcja input przechowuje wartości w postacji String

# wiek = input("Jaki masz wiek: ")
# wiek = wiek + 5
# print("Za 5 lat będziesz miał " + wiek + " lat.")

# Konwersja z jednego typu danych na drugi:

# napis_na_liczbe = int("23")
# liczba_na_napis = str(20)

# print(napis_na_liczbe + 20)
# print(liczba_na_napis + "abc")

# wiek = input("Jaki masz wiek: ")
# print("Zmienna wiek ma typ: ", type(wiek)) # str - string
# wiek = int(wiek) # konwertujemy na liczbę
# wiek = wiek + 5
# # print("Za 5 lat będziesz miał",wiek ,"lat.")

# print("Zmienna wiek ma typ: ", type(wiek)) # int - integer - liczba całkowita

# Zadanie:
# Pobierz od użytkownika imię, wiek i klasę. Wydrukuj potem te dane w jednej linijce.
# 5 min - 11:05.

imie = input("Podaj swoje imię: ")
wiek = input("Podaj swój wiek: ") # UWAGA - to będzie napis
klasa = input("Podaj swoją klasę: ")

print("Masz na imię ", imie, "Twój wiek to ", wiek, "Jesteś w klasie", klasa)

# f-string - lepszy sposób na formatowanie tekstu.
# Połączenie tesktu z wartościami ze zmiennych nazywany INTERPOLACJĄ.

print(f"Masz na imię {imie}. Twój wiek to {wiek} i jesteś w klasie {klasa}.")
