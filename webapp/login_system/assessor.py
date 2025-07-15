class Assessor:

    def __init__(self, email, password):
        self.email = email
        self.passowrd = password

    def __str__(self):
        return self.email

    def to_dict(self):
        return {
            'email': self.email,
            'password': self.passowrd
        }
