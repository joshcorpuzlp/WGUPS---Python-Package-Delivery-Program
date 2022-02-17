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

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip, self.delivery_deadline, self.mass_kg, self.status, self.notes)

    def printPackageDetails(self):
        print(f'Id: {self.package_id} - Address: {self.package_address} {self.package_city}, {self.package_state} {self.package_zip}')
