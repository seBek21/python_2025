'''zadanie 1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

zmodifikuj powyższą funkcję tak, aby sortowała listę w porządku malejącym.
'''

'''zadanie 2
ykorzystując moduł time sprawdź, które podejście iteracyjne czy rekurencyjne zwróci 
szybciej wartość dla 50 elementu ciągu fibbonaciego.
'''

'''zadanie 3
zdefiniuj funkcje ktora wylicza silnie podejscie iteracyjne i rekurencyjne.
Następnie wykorzystaj moduł time aby sprawdzić, które podejście jest szybsze dla np. 1000!
'''

'''zadanie 4
nested_list = [1, [2, [3, 4], 5], 6]

def find_recursive(lst, target):
    for item in lst
        if type(item) == list
            result = find_recursive(item, target)
            if result != None
                return result
        elif item = target
            return item
    return None

print(find_recursive(nested_list 4))

jakie błędy występują w powyższym kodzie? Popraw je.
'''

'''zadanie 5
dla danej listy sekwencji zwróć listę zawierającą liczbę tymin 
dla każdej sekwencji (rozwiązanie 1/2 linijkowe). Przykładowo dla: ["ATTGC", "AGGC", "TTTGC"]
 powinieneś otrzymać [2,0,3]. Wykonaj to zadanie na 2 różne sposoby (map lub filter/lista składana)
'''

'''zadanie 6
list(map((lambda x: x**x, [1,2,3,4,5,6])))
przepisz powyższy kod na listę składana.
'''

'''zadanie 7
Dany jest string, w którym znajdują się sekwencje nukleotydowe
. W 2 linijkach kodu, zapisz każdą sekwencję jako kolejny element listy i 
posortuj je wg liczby uracyli (od sekwencji zawierającej najwięcej, do tej najmniej).
s = "UGAGGUAGUAGGUUUUUUUUUU, UGAGGUAGUAGGUUGAUUUUUU, UGAGGUAGUAGGUUGUUUUUUU, UGAGGUAGUAGGUUGUGAUUUU, UGAGGUAGUAGGUUGUAUGGUU"
'''
