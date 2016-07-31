from src.common.database import Database


class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_by_email():
        data = Database.find_one("users", {"email": self.email})
        if data is not None:
            return cls(**data)

    def get_by_id(self):
        pass

    def login_valid(self):
        # Check wheter a user's email matches the password they sent us
        pass

    def register(self):
        pass

    def login(self):
        pass

    def get_blogs(self):
        pass
