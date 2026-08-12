# Maurice Toney
# Final Project - Part 1: Bob's Ski & Snowboard Rentals

#-----------------------------------------------------------------------
# Class definition: Rental
#-----------------------------------------------------------------------
class Rental:

    def __init__(self, customer, rental_period, units, coupon_code=""):
        self.customer = customer
        self.rental_period = rental_period
        self.units = units
        self.coupon_code = coupon_code
        self.ski_quantity = 0
        self.snowboard_quantity = 0

    #-------------------------------------------------------------------
    # Methods
    #-------------------------------------------------------------------
    def add_skis(self, quantity):
        self.ski_quantity = self.ski_quantity + quantity

    def add_snowboards(self, quantity):
        self.snowboard_quantity = self.snowboard_quantity + quantity

    def get_total_items(self):
        return self.ski_quantity + self.snowboard_quantity

    def calculate_estimate(self, rental_shop):
        ski_price = rental_shop.ski_inventory.get_best_price(self.ski_quantity, self.rental_period, self.units)
        snowboard_price = rental_shop.snowboard_inventory.get_best_price(self.snowboard_quantity, self.rental_period, self.units)
        subtotal = ski_price + snowboard_price
        final_price = rental_shop.calculate_final_price(subtotal, self.get_total_items(), self.coupon_code)
        return final_price

    def calculate_final_bill(self, rental_shop, actual_units):
        self.units = actual_units
        return self.calculate_estimate(rental_shop)