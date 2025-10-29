class User:
    def __init__(self, id: int | None, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User({self.id}, '{self.name}', '{self.email}')"
