# customer.py

class Customer:
    def __init__(self, name, customer_id):
        self._name = name
        self._customer_id = customer_id

    def get_name(self):
        return self._name

    def get_customer_id(self):
        return self._customer_id
