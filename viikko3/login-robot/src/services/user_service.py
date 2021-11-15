from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        username_checker = re.compile("^[a-z]+$")
        password_checker = re.compile("^[a-z]+$")
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise UserInputError("Username must be 3 or above characters")
        
        if not bool(re.match(username_checker, username)):
            raise UserInputError("Username must contain only lowercase letters")
        
        if len(password) < 8:
            raise UserInputError("Password must be 8 or above characters")

        if bool(re.match(password_checker, password)):
            raise UserInputError("Password must characters other than letters")