from app.calculator import Operations
import re

def repl():
    """
    Simple command-line calculator using the Operations class.
    Supports addition, subtraction, multiplication, and division.
    Type 'exit' to quit the program.
    """
    print("Simple Calculator")
    print("You can perform: addition (+), subtraction (-), multiplication (*), division (/)")
    print("Type 'exit' to quit.\n")

    operations_map = {
        '+': Operations.addition,
        '-': Operations.subtraction,
        '*': Operations.multiplication,
        '/': Operations.division,
    }

    while True:
        expr = input("Enter expression (e.g. 2 + 3): ").strip()
        if expr.lower() == "exit":
            print("Goodbye!")
            break

        try:
            match = re.fullmatch(r'\s*([-+]?\d*\.?\d+)\s*([+\-*/])\s*([-+]?\d*\.?\d+)\s*', expr)
            if not match:
                raise ValueError("Invalid format. Use: number operator number (e.g. 2 + 3)")

            a_str, op, b_str = match.groups()
            a, b = float(a_str), float(b_str)

            if op in operations_map:
                result = operations_map[op](a, b)
            else:
                raise ValueError("Invalid operator. Use +, -, *, or /.")

            print("Result:", result)

        except ValueError as ve:
            print("Error:", ve)
        except Exception:
            print("Error: Something went wrong. Please enter a valid expression like '2 + 3'.")

if __name__ == "__main__":
    repl()
