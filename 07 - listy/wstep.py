"""
lista - jak sama nazwa wskazuje jest strukturą danych, w której mamy sekwencje pewnych danych

przykładowo:
lista uczniów
1. Tomek
2. Adam
3. Bartek
...

lista ocen
4.5
3
6
2

lista wyników meczy

lista zakupów

Techniczne:
Lista w Pythonie może się zmniejszać bądź zwiększać - jej rozmiar jest dynamiczny.
Lista w Pythonie ma możliwość posiada w tej samej liście dane o różnych typach:
1. "Tomek"
2. "Bartek"
3. 43
4. True
5. 1. "Bartek"
   2. "Ania"

I choć jest to legalne - program na was nie będzie krzyczał - to jest to uważane za złą praktykę.
Najlepiej żeby lista była jednego typu.

Jak ogólnie zadeklarować listę:
nazwa_zmiennej = [a, b, c, d, e]
"""
lista_uczniow = ["Ania", "Bartek", "Czesław"]

for element in lista_uczniow:
    print(element)