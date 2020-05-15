"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password,):

        self.first_name  = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self): 

        return (f'Customer: { first_name },{ last_name },{ email }')  


def get_customers_from_file(filename):
    """create a global dictionary to store Customer with email as the key"""
    customers = {}

    with open(filename) as file:
        for line in file:
            first_name, last_name, email, password = line.strip().split("|")

            
            customers[email] = Customer(first_name,
                                        last_name,
                                        email,
                                        password)
    return customers

def get_by_email(email):
    """get and return a Customer for given email"""

    return customers[email]

customers = get_customers_from_file("customers.txt")