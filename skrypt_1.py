import sys
class MyError(Exception):
    pass
def main():
    if len(sys.argv) != 2:
        raise MyError("Podaj dokladnie jeden argument")
    arg = sys.argv[1]
    if not arg.isdigit():
        raise MyError("Argument musi byc liczba calkowita")
    liczba = int(arg)
    print(f"Wprowadzona liczba to: {liczba}")
if __name__ == "__main__":
    main()