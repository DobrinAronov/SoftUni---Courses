class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str) -> None:
        if not isinstance(value, str) or \
                not (5 <= len(value) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        is_length = len(value) >= 8
        has_upper_letter = any(char for char in value if char.isupper())
        has_digit = any(char for char in value if char.isdigit())

        if not all([is_length, has_upper_letter, has_digit]):
            raise ValueError("The password must be 8 or more characters "
                             "with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self) -> str:
        return (f'You have a profile with username: "{self.username}"'
                f' and password: {"*" * len(self.__password)}')


profile_with_invalid_password = Profile('My_username', 'My-password')
