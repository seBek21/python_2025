import sys
class MyError(Exception):
    pass
def main():
    if len(sys.argv) != 2:
        raise MyError("Podaj dokladnie jeden argument")
    liczby_str = sys.argv[1].split(',')
    suma = 0
    for num_str in liczby_str:
        try:
            num = float(num_str)
            suma += num
        except ValueError:
            raise MyError(f"Nieprawidlowy argument: {num_str}")
    print(f"Suma: {suma}")