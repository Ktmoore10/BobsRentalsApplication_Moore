#-----------------------------------------------------------------------
# Class Definition: Customer
#-----------------------------------------------------------------------
class Customer:

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    #-------------------------------------------------------------------
    # Properties
    #-------------------------------------------------------------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            print("Customer name cannot be blank.")
            value = "Unknown"
        self._name = value

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        if value == "":
            print("Customer ID cannot be blank.")
            value = "Unknown"
        self._id_number = value