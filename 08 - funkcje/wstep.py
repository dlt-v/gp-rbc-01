"""
Funkcje pozwalają nam na powtórzenie pewnego fragmentu kodu z różnymi parametrami.

Funkcje tworzymy w taki sposób:

def nazwa_funkcji(argumenty):
    
    ciało funkcji

Wykonanie funkcji wygląda tak:

nazwa_funkcji(a, b)

"""

def dodaj_dwie_liczby(a, b):

    print(f"Suma a i b to: {a + b}")


dodaj_dwie_liczby(2, 3)
dodaj_dwie_liczby(3, 5)

"""
Funkcje mogą również zwracać wartości.

random.randInt(0, 10) <- ta funkcja zwraca liczbę

Zwracanie wartości robimy za pomocą słowa kluczowego "return"

def nazwa_funkcji(a, b):

    ...

    return x
"""

def suma(a, b): # Funkcja musi być wcześniej zadeklarowana zanim będziemy mogli jej używać.

    wynik = a + b
    return wynik


moj_wynik = suma(3, 5)

print(moj_wynik)

