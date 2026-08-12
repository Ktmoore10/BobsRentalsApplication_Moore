# Maurice Toney
# Final Project Part 1: Bob's Ski & Snowboard Rentals

#-----------------------------------------------------------------------
# Class Definition: RentalEquipment
#-----------------------------------------------------------------------

class RentalEquipment:

    def __init__(self, name, hourly_rate, daily_rate, weekly_rate, quantity_available):
        self.name = name
        self.hourly_rate = hourly_rate
        self.daily_rate = daily_rate
        self.weekly_rate = weekly_rate
        self.quantity_available = quantity_available

    #-------------------------------------------------------------------
    # Properties
    #-------------------------------------------------------------------
    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value < 0:
            print("Hourly rate must be positive. Value given: " + str(value))
            value = 0
        self._hourly_rate = value

    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        if value < 0:
            print("Daily rate must be positive. Value given: " + str(value))
            value = 0
        self._daily_rate = value

    @property
    def weekly_rate(self):
        return self._weekly_rate

    @weekly_rate.setter
    def weekly_rate(self, value):
        if value < 0:
            print("Weekly rate must be positive. Value given: " + str(value))
            value = 0
        self._weekly_rate = value

    @property
    def quantity_available(self):
        return self._quantity_available

    @quantity_available.setter
    def quantity_available(self, value):
        if value < 0:
            print("Quantity must be positive. Value given: " + str(value))
            value = 0
        self._quantity_available = value

    #-------------------------------------------------------------------
    # Methods
    #-------------------------------------------------------------------
    def get_equipment_type(self):
        return "Equipment"

    def get_best_price(self, quantity, rental_period, units):
        if rental_period == "hourly":
            calculated_price = self.hourly_rate * units * quantity
            if self.daily_rate * quantity < calculated_price:
                calculated_price = self.daily_rate * quantity
        elif rental_period == "daily":
            calculated_price = self.daily_rate * units * quantity
            if self.weekly_rate * quantity < calculated_price:
                calculated_price = self.weekly_rate * quantity
        elif rental_period == "weekly":
            calculated_price = self.weekly_rate * units * quantity
        else:
            calculated_price = 0
        return calculated_price

    def reduce_inventory(self, quantity):
        if quantity > self.quantity_available:
            print("Not enough inventory available. Value given: " + str(quantity))
        else:
            self.quantity_available = self.quantity_available - quantity

    def restore_inventory(self, quantity):
        self.quantity_available = self.quantity_available + quantity

    def display_info(self, show_inventory=True):
        print("Equipment:", self.name)
        print("Hourly rate:", self.hourly_rate)
        print("Daily rate:", self.daily_rate)
        print("Weekly rate:", self.weekly_rate)
        if show_inventory:
            print("Available:", self.quantity_available)