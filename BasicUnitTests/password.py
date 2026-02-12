def validate_password(password: str) -> bool:
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    if len(password) < 8:
        return False

    has_uppercase = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    return has_uppercase and has_digit