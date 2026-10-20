class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_NAME_LEN = 4

while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split('@')

    if len(username) <= MIN_NAME_LEN:
        raise NameTooShortError("Name must be more than 4 characters")

    _, tld = domain.split('.')

    if tld not in ("com", "bg", "net", "org"):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
