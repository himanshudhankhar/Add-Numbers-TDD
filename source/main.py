import sys
from source.string_adder import add_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m src.main <input>")
        sys.exit(1)

    input = sys.argv[1]

    try:
        result = add_string(input)
        print(f"The result of adding is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
