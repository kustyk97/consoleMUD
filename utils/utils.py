import re


def is_int(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def try_get_int_value() -> float:
    value = input()
    if is_int(value) is True:
        value = int(value)
        return value
    else:
        print("This is not int value")
        return None
