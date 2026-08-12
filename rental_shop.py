# Maurice Toney
# Final Project - Part 1: Bob's Ski & Snowboard Rentals

from ski import Ski
from snowboard import Snowboard

#-----------------------------------------------------------------------
# Class Definition: RentalShop
#-----------------------------------------------------------------------
class RentalShop:

    def __init__(self, starting_ski_inventory, starting_snowboard_inventory):
        self.starting_ski_count = starting_ski_inventory
        self.starting_snowboard_count = starting_snowboard_inventory
        self.ski_inventory = Ski(starting_ski_inventory)
        self.snowboard_inventory = Snowboard(starting_snowboard_inventory)
        self.daily_skis_rented = 0
        self.daily_snowboards_rented = 0
        self.daily_revenue = 0

    #-------------------------------------------------------------------
    # Inventory management methods
    #-------------------------------------------------------------------
    def rent_skis(self, quantity):
        self.ski_inventory.reduce_inventory(quantity)

    def rent_snowboards(self, quantity):
        self.snowboard_inventory.reduce_inventory(quantity)

    def return_skis(self, quantity):
        self.ski_inventory.restore_inventory(quantity)

    def return_snowboards(self, quantity):
        self.snowboard_inventory.restore_inventory(quantity)

    #-------------------------------------------------------------------
    # Discount methods
    #-------------------------------------------------------------------
    def calculate_family_discount(self, subtotal, total_items):
        if total_items >= 3 and total_items <= 5:
            subtotal = subtotal * 0.75
        return subtotal

    def calculate_coupon_discount(self, subtotal, coupon_code):
        if coupon_code.endswith("BBP"):
            subtotal = subtotal * 0.90
        return subtotal

    def calculate_final_price(self, subtotal, total_items, coupon_code):
        subtotal = self.calculate_family_discount(subtotal, total_items)
        subtotal = self.calculate_coupon_discount(subtotal, coupon_code)
        return subtotal

    #-------------------------------------------------------------------
    # Daily total methods
    #-------------------------------------------------------------------
    def add_daily_totals(self, ski_quantity, snowboard_quantity, revenue):
        self.daily_skis_rented = self.daily_skis_rented + ski_quantity
        self.daily_snowboards_rented = self.daily_snowboards_rented + snowboard_quantity
        self.daily_revenue = self.daily_revenue + revenue