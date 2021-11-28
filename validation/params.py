from re import fullmatch


def email_validation(email: str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    isValid = fullmatch(regex, email)

    if isValid:
        return True

    return False
