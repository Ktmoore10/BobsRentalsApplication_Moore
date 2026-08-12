# Maurice Toney
# Final Project - Part 1: Bob's Ski & Snowboard Rentals

from rental_equipment import RentalEquipment

#-----------------------------------------------------------------------
# Class Definition: Snowboard
#-----------------------------------------------------------------------
class Snowboard(RentalEquipment):

    def __init__(self, quantity_available):
        super().__init__("Snowboard", 10, 40, 160, quantity_available)

    #-------------------------------------------------------------------
    # Methods
    #-------------------------------------------------------------------
    def get_equipment_type(self):
        return "Snowboard"