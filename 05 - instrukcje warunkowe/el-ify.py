"""
if warunek:

    fragment_kodu

else:

    fragment_kodu


"""

"""
if warunek:         - główny warunek
    fragment_kodu1
elif warunek:       - jeżeli warunek główny jest fałszywy, to ten warunek zostanie         
                        sprawdzony
    fragment_kodu2
elif warunek:       - jeżeli warunek nad tym jest fałszywy, to ...
    fragment_kodu3
else:
    fragment_kodu4 - else musi być na samym końcu "drabiny"

"""

# liczba = 55

# if liczba > 100:
#     print("Liczba jest większa od 100.")
# elif liczba > 50:
#     print("Liczba jest większa od 50.")
# elif liczba > 10:
#     print("Liczba jest większa od 10.")
# else:
#     print("Liczba jest mniejsza bądź równa 10.")

# pieniadze = int(input("Ile masz gotówki? "))
# wiek = int(input("Ile masz lat? "))

# if pieniadze > 10 and wiek >= 16:
#     print("Możesz wejść do kina.")
# elif pieniadze <= 10 and wiek >= 16:
#     print("Nie masz wystarczająco dużo pieniędzy")
# elif pieniadze > 10 and wiek < 16:
#     print("Nie masz wymaganego wieku.")
# else:
#     print("Nie masz wymaganego wieku oraz nie masz wystarczająco dużo pieniędzy")

"""
Zadanie:
Prosty kalkulator. Program wyświetli znaki działań, które można wykonywać:
- ‘+’ dla dodawania,
- ‘-’ dla odejmowania,
- itd (4 w sumie operacje)
Po wybraniu odpowiedniej opcji program zapyta o liczby potrzebne do wykonania
działania, a następnie wyświetli wynik.
Do 12:10

"""
# print("+ dodawanie")
# print("- odejmowanie")
# print("* mnożenie")
# print("/ dzielenie")
# opcja = input("Podaj znak operacji: ")
# a = float(input("Podaj liczbę a: "))
# b = float(input("Podaj liczbę b: "))

# if opcja == "+":
#     print(f"{a} + {b} = {a + b}")
# elif opcja == "-":
#     ...
# elif opcja == "*":
#     ...
# else:
#     if b != 0:
#         print(f"{a} / {b} = {a / b}")
#     else:
#         print("Nie można dzielić przez zero.")

"""
Zadanie 1:
Napisz program, który przyjmuje dwie liczby od użytkownika i wypisuje większą z nich oraz czy są równe.

Zadanie 2:
Stwórz program, który przyjmuje rok urodzenia użytkownika i oblicza jego wiek. Następnie wypisuje odpowiedni komunikat, np. "Jesteś pełnoletni" lub "Nie jesteś jeszcze pełnoletni".

Zadanie 3:
Napisz program, który oblicza cenę końcową produktu po uwzględnieniu podatku VAT. Poproś użytkownika o podanie ceny produktu i stawki VAT (23% lub 8%). Użyj instrukcji warunkowych, aby odpowiednio obliczyć cenę po opodatkowaniu.
"""
# Przerwa do 14:00

# a = int(input("a: "))
# b = int(input("b: "))

# if a == b:
#     print("a i b są równe.")
# else:
#     print(f"Większa wartość to: {max(a, b)}")

# cena = float(input("Podaj cenę netto produktu: "))
# stawka = int(input("Podaj stawkę VAT w %: "))

# if stawka == 8:
#     print(f"Cena z podatkiem VAT 8% to: {cena + cena * (stawka / 100)} PLN")
# elif stawka == 23:
#     print(f"Cena z podatkiem VAT 23% to: {cena + cena * (stawka / 100)} PLN")
# else:
#     print("Niepoprawna stawka VAT.")

"""
Napisz program, który wczyta od użytkownika oceny końcowe z pięciu przedmiotów:
matematyka, polski, angielski, wos, wf. Następnie wyliczy średnią ocen i wyświetli
komunikat czy otrzymamy pasek na świadectwie (pasek >= 4.75 średniej).
Do 14:20

Funkcje konwersji jawnej:
int() - próbuje przekonwertować wartość na liczbę całkowitą - Integer
str() - próbuje przekonwertować wartość na napis, String
float() - próbuje przekonwertować wartość na liczbę zmiennoprzecinkową - Float
bool() - próbuje przekonwertować wartość na wartość Prawda Fałsz (True, False)
"""

mat = float(input("Podaj ocenę z przedmiotu matematyka: "))
pol = float(input("Podaj ocenę z przedmiotu polski: "))
ang = float(input("Podaj ocenę z przedmiotu angielski: "))
wos = float(input("Podaj ocenę z przedmiotu wos: "))
wf = float(input("Podaj ocenę z przedmiotu wf: "))

srednia = (mat + pol + ang + wos + wf) / 5

print(f"Twoja średnia ocen to: {srednia}")
if srednia >= 4.75:
    print("Gratulacje! Uzyskałeś czerwony pasek.")
else:
    print("Przykro mi, nie masz czerwonego paska.")