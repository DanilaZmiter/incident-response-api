import re


def validate_password_complexity(v: str) -> str:
    if len(v) < 8:  # check for lenght
        raise ValueError("Пароль должен быть не менее 8 символов в длину")

    if not re.search(r"[a-zа-я]", v):  # check for at least one little letter
        raise ValueError("Пароль должен содержать хотя бы одну строчную букву")

    if not re.search(r"[A-ZА-Я]", v):  # check for at least one big letter
        raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")

    if not re.search(r"[0-9]", v):  # at leats one number
        raise ValueError("Пароль должен содержать хотя бы одну цифру")

    if not re.search(r"[@$!%*?&._-]", v):  # at least one special symbol
        raise ValueError("Пароль должен содержать хотя бы один спецсимвол (@$!%*?&._-)")

    return v
