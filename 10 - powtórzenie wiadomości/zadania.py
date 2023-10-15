"""
1. Utwórz trzy zmienne, do których wpisz wartość 3 jako odpowiedni typ:
- x_int - jako liczba całkowita
- x_float - jako liczba z przecinkiem
- x_str - jako napis

"""
x_int = 43
x_float = 0.5
x_str = "Tomek"

"""
======================================================================

2. Utwórz zmienną napis_liczba, która przechowuje wartość "290".
Utwórz zmienną x. Użyj konwersji z typu str na typ int, aby zmienna x
przechowywała to co napis_liczba, ale jako typ liczby całkowitej

======================================================================

3. Utwórz 3 zmienne:
- pole_trojkata
- podstawa_trojkata
- wysokosc_trojkata
Do podstawa_trojkata oraz wysokosc_trojkata powinny trafić wartości odczytane z
konsoli (od użytkownika).
Oblicz pole takiego trójkąta i zapisz wynik w zmiennej pole_trojkata
Wyświetl wynik jako komunikat:

Pole trójkąta o podstawie XX oraz wysokości XX wynosi XX

Zamiast XX powinny pojawić się wartości liczbowe

======================================================================

4. Zapytaj użytkownika o jego wiek i na tej podstawie wyświetla w konsoli jeden z
komunikatów:
- Jesteś pełnoletni/a
- Nie jesteś jeszcze pełnoletni/a. Brakuje Ci XX lat do 18 roku życia
Zamiast XX powinna pojawić się wartość liczbowa

======================================================================

5. Cena atrakcji turystycznej zależy od miesiąca. Napisz program, który zapyta
użytkownika o liczbę biletów oraz miesiąc, w którym chce odwiedzić park
rozrywki i na tej podstawie obliczy koszt transakcji.
Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):
- 1 -> 50 zł
- 2 -> 50 zł
- 3 -> 100 zł
- 4 -> 100 zł
- 5 -> 200 zł
- 6 -> 200 zł
- 7 -> 250 zł
- 8 -> 200 zł

- 9 -> 200 zł
- 10 -> 100 zł
- 11 -> 100 zł
- 12 -> 50 zł

Wyświetl komunikat:
"Cena biletów: XX zł"
XX to wartość liczbowa

Jeśli wprowadzono niepoprawny numer miesiąc program powinien wyświetlić
informację:
"Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie"

======================================================================

6. Napisz program, który zapyta użytkownika o liczbę, a następnie wypisze na
ekranie tyle wyników z rzutu kością sześcienną.
Rzut kością sześcienną to wynik z losowania liczby od 1 do 6 (włącznie).

======================================================================

7. Napisz funkcję, która przyjmuje 2 argumenty:
- tekst, typu str
- n, typu int
a zwraca nowy napis, który powstaje poprzez połączenie text n razy.

Szablon funkcji:
def laczenie_slow(???) -> ???:
    nowy_tekst = ""
    ???
    ???
    return ???

Zastąp wszystkie znaki zapytania odpowiednimi wyrazami/instrukcjami/itd

======================================================================

8. Przygotuj funkcję, która otrzymuje jeden argument: n - liczbę elementów.
Funkcja ma zwrócić listę n - losowych elementów od 0 do 100
Wywołaj ją kilka razy, aby sprawdzić, czy za każdym razem zwraca różne wartości

======================================================================

9. Napisz program aplikacji graficznej, która co 3 sekundy zmienia kolor tła. Nowy
kolor tła powinien być losowany.
Pamiętaj o wykorzystaniu liczby klatek do wykrycia kiedy mijają kolejne 3 sekundy
Pamiętaj o budowaniu koloru RGB:
RGB składa się z trzech kolorów, każdy może przyjąć wartość od 0 do 255 (włącznie)
RGB = [R, G, B] możesz przechowywać to jako listę

======================================================================

10.Dodaj do swojego wykrywanie naciśnięcia klawisza 'b'.
Jeśli taki klawisz zostanie naciśnięty kolor tła powinien zmienić się na czarny - po
puszczeniu klawisza kolor:
- powinien zostać na nowo wylosowany - wersja podstawowa
- powinien wrócić poprzedni kolor - wersja rozszerzona

"""