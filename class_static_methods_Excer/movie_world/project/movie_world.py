from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self,customer:Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd:DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
         for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer.name} has already rented {dvd.name}"
                for d in self.dvds:
                    if d.id == dvd_id and d.is_rented:
                        return "DVD is already rented"
                    elif d.id == dvd_id and not d.is_rented:
                        if customer.age < d.age_restriction:
                            return f"{customer.name} should be at least {d.age_restriction} to rent this movie"
                        else:
                            d.is_rented = True
                            customer.rented_dvds.append(d)
                            return f"{customer.name} has successfully rented {d.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for d in customer.rented_dvds:
                    if dvd_id == d.id:
                        d.is_rented = False
                        customer.rented_dvds.remove(d)
                        return f"{customer.name} has successfully returned {d.name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customer_repr = ""
        for customer in self.customers:
            customer_repr += f"{customer}\n"
        dvd_repr = ""
        for dvd in self.dvds:
            dvd_repr += f"{dvd}\n"
        return f"{customer_repr}{dvd_repr}"









