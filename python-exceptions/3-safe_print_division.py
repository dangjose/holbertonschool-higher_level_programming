#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ValueError, IndexError, ZeroDivisionError) as e:
        print(e)
    finally:
        print("Inside result: {:.1f}".format(result))
        return result
