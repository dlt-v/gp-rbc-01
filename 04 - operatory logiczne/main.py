"""
> - większy od
< - mniejszy od

>= - większy bądź równy
<= - mniejszy bądź równy

== - równy 
!= - nierówny

and - i
or  - lub
not - zaprzeczenie


Tworzenie zapytań/kwarend

a > 10 - "czy a jest większe od 10?" - True albo False

Wartość boolowska jest wynikiem tego zapytania.

and, or, not - pozwalają nam na tworzenie złożonych zapytań logicznych.

"""

pieniadze = 10
wiek = 14

# Czy mamy więcej niż 7zł? Oraz czy mamy 16 bądź więcej lat.
wynik = pieniadze >= 7 and wiek >= 16
#          True      and      False

# AND - zwraca True jeżeli wszystkie zapytania są prawdziwe. 
# Jeżeli przynajmniej jeden z nich jest nieprawdziwy to zwraca False.
# np. TRUE and TRUE and TRUE and FALSE => FALSE

# OR - zwraca True jeżeli przynajmniej jeden warunek jest prawdziwy.
# np. TRUE or FALSE or FALSE or FALSE => TRUE

# NOT - zaprzeczenie albo po prostu odwrotność wyrażenia
# np. not True => False | not False => True


# print(f"Czy możemy wejść do kina na horror? {wynik}")

# print(f'False and True: {False and True}')
# print(f'False or True: {False or True}')
# print(f'not True: {not True}')
# print(f'not False: {not False}')

# # Najpierw wykonywany jest operator NOT, potem operator AND a na końcu OR.

# # AND i OR w Pythonie działają trochę specyficznie:

# True and False and True
# False and True and True

# True or False or True or False or False or False
# False or True or False

# a = 0
# wynik = a != 0 and 100 / a > 5

