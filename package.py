# -- INFO ---------------
# First Name: Joshua
# Last Name: Corpuz
# Student id#: 001196484
# -- INFO ---------------

# NOTES
# Package class used to represent a package and store its details
# Package class also contain methods that allow for its properties to be accessed.

class Package():
    def __init__(self):
        self.id = None
        self.address = ""
        self.city = ""
        self.state = ""
        self.zip = ""
        self.delivery_deadline = ""
        self.mass_kg = 0
        self.notes = ""
        self.status = ""
        self.miles_traveled = 0.00
        self.time_elapsed = 0.00
        self.datetime_delivered = None
        self.end_time = None

    def __repr__(self):
        return "ID: %s, Address: %s %s, %s %s, Deadline: %s, Mass (Kg): %s, Status: %s, Notes: %s" % (self.id, self.address, self.city, self.state, self.zip, self.delivery_deadline, self.mass_kg, self.status, self.notes)

    def printPackageDetails(self):
        print(f'Id: {self.package_id} - Address: {self.package_address} {self.package_city}, {self.package_state} {self.package_zip}')

    def set_address(self, updated_address):
        self.address = updated_address

    def get_address(self):
        return self.address

    def set_city(self, updated_city):
        self.city = updated_city

    def get_city(self):
        return self.city

    def set_zip(self, updated_zip):
        self.zip = updated_zip

    def get_zip(self):
        return self.zip

    def get_full_address(self):
        return f'{self.address} {self.city}, {self.state} {self.zip}'

    def set_delivery_deadline(self, delivery_deadline):
        self.delivery_deadline = delivery_deadline

    def get_delivery_deadline(self):
        return self.delivery_deadline

    def set_mass_kg(self, mass_kg):
        self.mass_kg = mass_kg

    def get_mass_kg(self):
        return self.mass_kg

    def set_notes(self, notes):
        self.notes = notes

    def get_notes(self):
        return self.notes

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
