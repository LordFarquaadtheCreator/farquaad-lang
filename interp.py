import Interp
import sys

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        i = Interp(file)
    except Exception as e:
        print(f"AOOOWGA! Error spotted on line {e}. CRASHING OUT!!!")