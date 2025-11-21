'''
Zadanie 1.
Napisz skrypt, który przymuje od użytkownika 3 liczby całkowiite a,b,c
i oblicza wyrażenie kwadratowe ax^2 + bx + c i zwraca jego pierwiastki.
Pamietaj o obsłudze wyjątków:
- ValueError - gdy użytkownik poda coś innego niż liczbe całkowitą
- ZeroDivisionError - gdy a = 0 (wtedy to nie jest wyrażenie kwadratowe)
- Inne wyjątki, które mogą się pojawić podczas działania programu
'''

'''
Zadanie 2.
Utworz skrypt ktory jako argumenty przyjmuje sciezke do 
folderu gdzie znajduja sie pliki z sekwencjami DNA w formacie FASTA.
Skrypt powinien zczytac kazdy plik i obliczyc dla kazdej sekwencji 
jej dlugosc oraz zawartosc poszczegolnych nukleotydow (A, T, C, G).
Wyniki powinny zostac zapisane do pliku o nazwie sekwencji w nowo utworzonym folderze "wyniki".
Pamietaj o obsludze wyjatkow:
- FileNotFoundError - gdy podany folder nie istnieje
- ValueError - gdy plik nie jest w formacie FASTA
- Inne wyjatki, ktore moga sie pojawic podczas dzialania programu
'''

'''
Zadanie 3.
Napisz funkcje, która dostaje listę wydarzeń w formacie:
[('Spotkanie',"2025-12-01 19:00),('Impreza', "2026-01-31 20:00")...]
następnie z takiej listy parsuje daty, sortuje je rosnąco i zwraca użytkownikowi, dla każdego
wydarzenia nazwę, datę, ile dni pozostało. Dodatkowo można uwzględnić jakiś komunikat, jeśli data już mineła.
Oczekiwany output:
Spotkanie pon 1 grudnia 2025 19:00 (za 12 dni)
'''