"""
a
41 | 1(% 2 = ) 1
20 | 0
10 | 0
5 |  1 ( 5 - 1 = 4 ; 4 : 2 = 2)
2 |  0
1 |  1 (od dołu)

41 (D) - 101001 (B)
"""

def convert_to_binary(a):

    wynik = ""

    while a > 0:
        m = a % 2
        a = a // 2
        wynik = str(m) + wynik
    
    return wynik

"""

1   0   1   0   0   1
2^5 2^4 2^3 2^2 2^1 2^0

2^5     + 2^3     + 2^0

32      + 8       + 1

41

"""

def convert_to_decimal(a):
    a = int(a)
    wynik = 0

    i = 0
    while a > 0:
        mod = a % 10
        a = a // 10
        wynik += mod * (2**i)
        i += 1

    return wynik



# liczba = int(input("Podaj liczbę: "))

# wynik = convert_to_binary(liczba)

# print(f"{liczba} w systemie binarnym wynosi: {wynik}")

# wynik_binarny = convert_to_decimal(wynik)

# print(f"{wynik} w systemie dziesiętnym wynosi: {wynik_binarny}")


"""
Zadanie 2:
Liczba pierwsza - liczba naturalna większa, od 1, której jedynymi naturalnymi dzielnikami jest liczba 1 i ona sama.

Waszym zadaniem jest napisać funkcję, która zwróci informacje prawda/fałsz czy podana liczba jest liczbą pierwszą.

def is_prime(a):

    ...

    return True/False

    Do 14:20
"""

def is_prime(a):

    if a <= 1:
        return False
    
    for i in range(2, a):
        if a % i == 0:
            return False
        
    return True

# print(is_prime(2))
# print(is_prime(5))
# print(is_prime(15))
# print(is_prime(23))

"""
Zadanie 3:
Napisz drugą funkcję, która ma wyświetlić wszystkie liczby pierwsze z podanego przedziału (możesz wykorzystać do tego funkcję, którą już napisałeś)

def check_range(a)
    ...
    print(...)

========================================================================

Zadanie 4:
Palindromy to bardzo ciekawe zagadnienie w świecie programowania. Palindromy są to
takie wyrażenia, liczby, ciągi znaków, które czytane od przodu jak i od tyłu brzmią tak
samo (często spacje są pomijane). Przykłady Palindromów:
oko, sedes, zakopane na pokaz, elf układał kufle, 4554

Napisz funkcję, która jako argument otrzymuje tekst i sprawdzi czy jest on palindromem
wyświetlając: „{podane słowo} jest palindromem” lub „{podane słowo} nie jest
palindromem”

========================================================================

Zadanie 5:
Anagramy to słowa, które składają się z tej samej ilości oraz z dokładnie tych samych liter. Przykład
bark – krab, adam – dama.

Napisz funkcję, która sprawdzi czy dwa podane wyrazy są anagramami

Przerwa do 15:30
"""