class GroupException(Exception):
    def __init__(self):
        self.message="This group can have a maximum of 10 people."
    def __str__(self):
        return self.message