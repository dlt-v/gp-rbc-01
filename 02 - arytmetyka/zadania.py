"""
    Zadanie 1:
    Pobierz od użytkownika (input) boki prostokąta i oblicz pole i obwód i wyświetl w terminalu.
    Pamiętaj że input zwraca napis, czyli trzeba go przekonwertować.
    Do 12:20.

    bok_a = input("Podaj bok a:" )
    bok_a = int(bok_a)

    Zadanie 2:
    Poproś użytkownika o podanie temperatury w stopniach Celsjusza i przelicz ją na stopnie Fahrenheita za pomocą wzoru: F = (C * 9/5) + 32 oraz wyświetl wynik w terminalu.
    Do 12:25.

    Zadanie 3:
    Poproś użytkownika o podanie trzech ocen szkolnych i oblicz ich średnią arytmetyczną. Wyświetl wynik.
    Do 12:35.
"""

# # Zadanie 1

# bok_a = float(input("Podaj bok a: "))
# bok_b = float(input("Podaj bok b: "))

# pole = bok_a * bok_b
# obwod = (bok_a + bok_b) * 2

# print(f"Obwód prostokąta to: {obwod}. Pole prostokąta to: {pole}.")


# Zadanie 2

#F = (C * 9/5) + 32

# temp_c = float(input("Podaj temperature w C: "))
# temp_f = (temp_c * 9 / 5) + 32

# print(f"{temp_c} C = {temp_f} F.")

# # Zadanie 3

# ocena_1 = float(input("Podaj ocenę 1: "))
# ocena_2 = float(input("Podaj ocenę 2: "))
# ocena_3 = float(input("Podaj ocenę 3: "))

# print(f"Twoja średnia z ocen to: {(ocena_1 + ocena_2 + ocena_3) / 3}")