"""
Zadanie 1:

Utwórz kalkulator, gdzie użytkownik wpisuje nazwę operacji oraz dwie liczby.
Wydrukuj najpierw dostępne operacjie, np:
"+ dodawanie"
"- odejmowanie"
...


Według symbolu operacji zostanie obliczony wynik.

========================================
Pojedyncze operacje zawrzyj w ich oddzielnych funkcjach.

dodaj(a, b)
odejmij(a, b)
...
========================================

Pamiętaj, że dzielenie nie może być prowadzone przez 0.

Na koniec wyświetl wynik w takim formacie:

"Wynik dodawania liczb 5 i 3 to: 8"
"Wynik odejmowania liczb 5 i 3 to: 2"

"""
# def suma(x, y):
#     return x + y

# def dzielenie(x, y):
#     if y == 0:
#         print("Nie można dzielić przez zero.")
#         return -1
#     else:
#         return x / y

# print("+ dodawanie")
# print("- odejmowanie")
# print("* mnożenie")
# print("/ dzielenie")

# operacja = input("Podaj znak operacji: ")
# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))

# if operacja == "+":
#     wynik = suma(a, b)
#     print(f"Wynik dodawania liczb {a} i {b} to: {wynik}")

# if operacja == "/":
#     wynik = dzielenie(a, b)
#     print(f"Wynik dzielenie liczb {a} i {b} to: {wynik}")


"""

Zadanie 2:

Utwórz funkcje, która po przyjęciu potrzebnych argumentów jak podstawa i wysokość obliczy pole trójkąta i wyświetli wynik.

"""
def pole_trojkata(a, b):
    print(f"Pole trójkąta wynosi: {a * b / 2}") 


podstawa = int(input("Podaj p: "))
wysokosc = int(input("Podaj h: "))

pole_trojkata(podstawa, wysokosc)

