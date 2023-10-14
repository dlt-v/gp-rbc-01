"""
Funkcje pozwalają nam na powtórzenie pewnego fragmentu kodu z różnymi parametrami.

Funkcje tworzymy w taki sposób:

def nazwa_funkcji(argumenty):
    
    ciało funkcji

Wykonanie funkcji wygląda tak:

nazwa_funkcji(a, b)

"""

# def dodaj_dwie_liczby(a, b):

#     print(f"Suma a i b to: {a + b}")


# dodaj_dwie_liczby(2, 3)
# dodaj_dwie_liczby(3, 5)

"""
Funkcje mogą również zwracać wartości.

random.randInt(0, 10) <- ta funkcja zwraca liczbę

Zwracanie wartości robimy za pomocą słowa kluczowego "return"

def nazwa_funkcji(a, b):

    ...

    return x
"""

# def suma(a, b): # Funkcja musi być wcześniej zadeklarowana zanim będziemy mogli jej używać.

#     wynik = a + b
#     return wynik


# moj_wynik = suma(3, 5)

# print(moj_wynik)


"""
Funkcje mogą mieć domyślne wartości.
Czyli w sytuacji gdy użytkownik wywoła funkcje bez podania argumentu, który jest oczekiwany. Możliwe jest, że funkcja użyje wartości domyślnej.

Domyślne wartości muszą być zadeklarowane od prawej strony.
def przedstaw_sie(imie, nazwisko, wiek = "x"):  -> Poprawnie!

def przedstaw_sie(imie = "Adam", nazwisko, wiek):  -> Błąd!

Nie możemy deklarować niedomyślych argumentów za domyślnymi argumentami.



"""

# def powitaj(imie = "kolego"):
#     print(f"Cześć {imie}!")


# powitaj("Tomek")
# powitaj("Michał")
# powitaj()

def przedstaw_sie(imie = "Ala", nazwisko = "Malarz", wiek = 18):
    print(f"Nazywam się {imie} {nazwisko} i mam {wiek} lat.")

przedstaw_sie("Adam", "Nowak", 18)
przedstaw_sie("Paweł", "Kowalski", 16)
przedstaw_sie("Paweł", "Kowalski")
przedstaw_sie()
