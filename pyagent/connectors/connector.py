class Connector:

    def __init__(self, user):
        self.user = user

    def get_quote(self):
        raise NotImplementedError
