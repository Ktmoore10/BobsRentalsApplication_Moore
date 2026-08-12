# Maurice Toney
# Final Project - Part 1: Bob's Ski & Snowboard Rentals

from rental_equipment import RentalEquipment

#-----------------------------------------------------------------------
# Class Definition: Ski
#-----------------------------------------------------------------------
class Ski(RentalEquipment):

    def __init__(self, quantity_available):
        super().__init__("Ski", 15, 50, 200, quantity_available)

    #-------------------------------------------------------------------
    # Methods
    #-------------------------------------------------------------------
    def get_equipment_type(self):
        return "Ski"