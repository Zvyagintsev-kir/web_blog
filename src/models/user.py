from src.common.database import Database


class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        # Check wheter a user's email matches the password they sent us
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is None:
            new_user = User(email, password)
            new_user.save_to_mongo()
            return True
        else:
            # User exists
            return False

    def login(self):
        pass

    def get_blogs(self):
        pass
