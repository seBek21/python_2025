'''
Zadanie 1.
Napisz funkcje, ktora wylicza wartosc wyrazenia:
(x^2 -4) / (x-2) 
wykorzystaj try/except do obslugi wyjatkow.
'''

'''
Zadanie 2.
Napisz funkcje, ktora przyjmuje dowolna liczbe argumentow i jako
wynik zwraca ich srednia:
a) arytmetyczna
b) geometryczna
Wywolanie funkcji averages(*args) powinno zwrocic liste postac:
[średnia_arytmetyczna, średnia_geometryczna]
'''

'''Zadanie 3.
Zmodyfikuj funkcję z zadania 2. tak, aby użytkownik ręcznie podawał liczby. 
Uwaga proces musi się kiedyś zakończyć. 
'''

'''Zadanie 4.
Z pliku 1E7A.fasta wczytaj do zmiennej hsa_seq sekwencję albuminy ludzkiej.
'''

'''Zadanie 5.
Ze zmiennej 1E7A.fasta utwórz słownik hsa_dict, gdzie klucze to odpowiednie oznaczenia aminokwasów, 
a wartości im odpowiadające to ilość ich wystąpień w sekwencji.
'''

'''Zadanie 6.
zapisz do nowego pliku hsa_freq częstość wystąpięń aminokwasów w HSA. Plik powinien mieć postać:
M    4
A    5
G    1
...'''

'''Zadanie 7.
Napisz funkcję, która przyjmuje jako argument x i zwraca wynik wyrażenia:
f(x) = (sin(π x) + cos(x²)) / (x! + √|x| - e^(-x))
'''

'''
Zadanie 8.
Napisz minutnik, która przyjmuje od użytkownika czas podany w formacie [X,Y,Z]
X=liczba h, Y=liczba minut, Z=liczba sekund'''

''''
Zadanie 9 – Mini ruletka
Napisz funkcję `mini_ruletka()`, która symuluje prostą grę w ruletkę:
1. Funkcja losuje liczbę całkowitą z przedziału 0–36 (kolory ruletki: czerwony/ czarny/ zielony).  
   - 0 jest zawsze **zielone**.  
   - Liczby parzyste > 0 to **czarne**, nieparzyste > 0 to **czerwone**.
2. Użytkownik typuje liczbę i zakład:
    - Liczba: `0–36`   
    - Zakład: dowolna dodatnia liczba całkowita
3. Funkcja zwraca:
    - Wylosowaną liczbę i jej kolor.
    - Typ użytkownika (liczba i kolor).
    - Informację, czy użytkownik wygrał (trafienie liczby lub koloru).
4. Dodatkowo oblicza wygraną:
    - Trafienie liczby: 35 * zakład
    - Trafienie koloru: 2 * zakład
    - Nietrafiony: 0
'''