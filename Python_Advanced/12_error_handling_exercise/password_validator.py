class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


def check_for_identical_characters(some_pass: str, special: tuple) -> bool:
    return some_pass.isdigit() or some_pass.isalpha() or all([sym in special for sym in some_pass])


MIN_PASSWORD_LEN = 8
SPECIAL_CHAR = ("@", "*", "&", "%")

password = input()

while password != "Done":

    if len(password) < MIN_PASSWORD_LEN:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if check_for_identical_characters(password, SPECIAL_CHAR):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any([sym in SPECIAL_CHAR for sym in password]):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")

    password = input()
