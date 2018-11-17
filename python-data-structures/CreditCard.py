# Creating the Credit Card class
class CreditCard:
    # Defining the constructor with default parameters
    def __init__(self, name='John Doe', limit=0.0, balance=0.0):
        self._name = name
        self._limit = limit
        self._balance = balance

    def get_name(self):
        return self._name

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

