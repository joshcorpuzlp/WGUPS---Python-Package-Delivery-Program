from turtle import update
import datetime


class Package():
    def __init__(self):
        self.id = None
        self.address = ""
        self.city = ""
        self.state = ""
        self.zip = ""
        self.delivery_deadline = ""
        self.mass_kg = 0
        self.status = ""
        self.notes = ""
        self.miles_travelled = 0.00
        self.time_elapsed = 0.00
        self.datetime_delivered = datetime.datetime(
            2022, 2, 21, hour=8, minute=0, second=0)

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip, self.delivery_deadline, self.mass_kg, self.status, self.notes)

    def printPackageDetails(self):
        print(f'Id: {self.package_id} - Address: {self.package_address} {self.package_city}, {self.package_state} {self.package_zip}')

    def set_address(self, updated_address):
        self.address = updated_address

    def set_city(self, updated_city):
        self.city = updated_city

    def set_zip(self, updated_zip):
        self.zip = updated_zip
