from Interp import Interp
import sys

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        i = Interp(file)
    except Exception as e:
        print(f"AOOOWGA!\n{e}\nCRASHING OUT!!!")
        exit(1)