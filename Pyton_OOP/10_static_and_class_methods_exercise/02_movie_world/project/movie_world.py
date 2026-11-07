from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def find_customer_and_dvd(self, some_customer_id, some_dvd_id):
        searched_customer = next((c for c in self.customers if c.id == some_customer_id), None)
        searched_dvd = next((d for d in self.dvds if d.id == some_dvd_id), None)
        return searched_customer, searched_dvd

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str | None:
        found_customer, found_dvd = self.find_customer_and_dvd(customer_id, dvd_id)

        if found_customer and found_dvd:
            if found_dvd in found_customer.rented_dvds:
                return f"{found_customer.name} has already rented {found_dvd.name}"
            if found_dvd.is_rented:
                return "DVD is already rented"
            if found_customer.age < found_dvd.age_restriction:
                return (f"{found_customer.name} should be at least"
                        f" {found_dvd.age_restriction} to rent this movie")

            found_dvd.is_rented = True
            found_customer.rented_dvds.append(found_dvd)
            return f"{found_customer.name} has successfully rented {found_dvd.name}"

    def return_dvd(self, customer_id, dvd_id) -> str:
        found_customer, _ = self.find_customer_and_dvd(customer_id, dvd_id)
        searched_dvd = next((d for d in found_customer.rented_dvds if d.id == dvd_id), None)
        if searched_dvd is None:
            return f"{found_customer.name} does not have that DVD"

        searched_dvd.is_rented = False
        found_customer.rented_dvds.remove(searched_dvd)
        return f"{found_customer.name} has successfully returned {searched_dvd.name}"

    def __repr__(self) -> str:
        output = []
        output.extend(repr(c) for c in self.customers)
        output.extend(repr(d) for d in self.dvds)

        return '\n'.join(output)
