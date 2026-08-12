from ski import Ski
from snowboard import Snowboard
from customer import Customer
from rental_shop import RentalShop
from rental import Rental





def Validate_Ski_Inventory():

    blnVlaidated = bool(False)
    while blnVlaidated == False:
        intSk = input("Enter starting ski inventory: ")
        try:
            intSk = int(intSk)
            if intSk < 0:
                print("Inventory must be greater than or equal to zero.")
            else:
                blnVlaidated = True
        except :
             print("Inventory must be a number.")

    return intSk

def Validate_Snowboard_Inventory():

    blnVlaidated = bool(False)
    while blnVlaidated == False:
        intSB = input("Enter starting snowboard inventory: ")
        try:
            intSB = int(intSB)
            if intSB < 0:
                print("Inventory must be greater than or equal to zero.")
            else:
                blnVlaidated = True
        except :
             print("Inventory must be a number.")

    return intSB


def Validate_Menu_Selection():

    blnVlaidated = bool(False)
    while blnVlaidated == False:
        intMenuSelection = input("Please select an option (1-4): ")
        try:
            intMenuSelection = int(intMenuSelection)
            if intMenuSelection < 1 or intMenuSelection > 4:
                print("Menu selection must be between 1 and 4.")
            else:
                blnVlaidated = True
        except :
             print("Menu selection must be a number.")

    return intMenuSelection

def ValidateName():

    blnValidated = bool(False)
    while blnValidated == False:
        intName = input("Enter customer name: ")
        if intName == "":
            print("Please enter a name.")
        else:
            blnValidated = True
            return intName

def ValidateCustomerID():

    blnValidated = bool(False)
    while blnValidated == False:
        intID = input("Enter customer ID: ")
        if intID == "":
            print("Please enter a customer ID.")
        else:
            blnValidated = True
            return intID

def Validate_Ski_Rental():

    blnVlaidated = bool(False)
    while blnVlaidated == False:
        intSk = input("Enter number of skis to rent: ")
        try:
            intSk = int(intSk)
            if intSk < 0:
                print("Quantity must be greater or equal to than zero.")
            elif intSk > Rental_Shop_obj.ski_inventory.quantity_available:
                print(f"Only {Rental_Shop_obj.ski_inventory.quantity_available} skis are available.")
            else:
                blnVlaidated = True
                return intSk
        except :
             print("Quantity must be a number.")



def Validate_Snowboard_Rental():
    
    blnVlaidated = bool(False)
    while blnVlaidated == False:
        intSB = input("Enter number of snowboards to rent: ")
        try:
            intSB = int(intSB)
            if intSB < 0:
                print("Quantity must be greater or equal to than zero.")
            elif intSB > Rental_Shop_obj.snowboard_inventory.quantity_available:
                print(f"Only {Rental_Shop_obj.snowboard_inventory.quantity_available} snowboards are available.")
            else:
                blnVlaidated = True
                return intSB
        except :
             print("Quantity must be a number.")

def Validate_Rental_Period():

    blnVlaidated = bool(False)

    while blnVlaidated == False:
        strRentalPeriod = input("Enter rental period (hourly/daily/weekly): ").lower()
        if strRentalPeriod not in ["hourly", "daily", "weekly"]:
            print("Rental period must be 'hourly', 'daily', or 'weekly'.")
        else:
            blnVlaidated = True
            return strRentalPeriod

def Validate_Length(strHoursDaysWeeks):

    blnVlaidated = bool(False)
    while blnVlaidated == False:
        intLength = input(f"How many {strHoursDaysWeeks}?: ")
        try:
            intLength = int(intLength)
            if intLength < 1:
                print("Quantity must be greater than zero.")
            else:
                blnVlaidated = True
                return intLength
        except :
             print("Quantity must be a number.")


def New_Customer_Rental():

    print("")
    print("-----New Customer Rental-----")
    print("")

    strCustomerName = ValidateName()
    strCustomerID = ValidateCustomerID()
    intSkiQuantity = Validate_Ski_Rental()
    intSBQuantity = Validate_Snowboard_Rental()

    if intSkiQuantity == 0 and intSBQuantity == 0:
        print("No equipment selected for rental. Returning to main menu.")
        return

    strRentalPeriod = Validate_Rental_Period()

    if strRentalPeriod == "hourly":
        strHoursDaysWeeks = "hour(s)"
    elif strRentalPeriod == "daily":
        strHoursDaysWeeks = "day(s)"
    else:
        strHoursDaysWeeks = "week(s)"

    intLength = Validate_Length(strHoursDaysWeeks)

    coupon_code = input("Enter coupon code (if any): ")

    customer = Customer(strCustomerName, strCustomerID)
    rental = Rental(customer, strRentalPeriod, intLength, coupon_code)
    rental.add_skis(intSkiQuantity)
    rental.add_snowboards(intSBQuantity)
    dblEstimate = rental.calculate_estimate(Rental_Shop_obj)

    print("")
    print("-------Rental Estimate------")
    print("")
    print(f"Customer Name: {strCustomerName}")
    print(f"Rental Length: {intLength} {strHoursDaysWeeks}")
    print(f"Skis Rented: {intSkiQuantity}")
    print(f"Snowboards Rented: {intSBQuantity}")
    print(f"Estimated Cost: ", "${:,.2f}".format(dblEstimate))
    print("")
    strComplete = input("Would the customer like to complete the rental? (yes/no): ").lower()
    if strComplete == 'yes':
        Rental_Shop_obj.rent_skis(intSkiQuantity)
        Rental_Shop_obj.rent_snowboards(intSBQuantity)
        Rental_Shop_obj.add_daily_totals(intSkiQuantity, intSBQuantity, 0)
        lstActiveRentals.append(rental)
        print("Rental completed.")
    elif strComplete == 'no':
        print("Returning to main menu.")
        return
    else:
        print("Please enter 'yes' or 'no'.")

def Rental_Return():
    
    print("")
    print("-----Rental Return-----")
    print("")
    strCustomerID = ValidateCustomerID()
    Found = None

    def Loop_Active_Rentals(strcustomer_id):

        for rental in lstActiveRentals:
            if rental.customer.id_number == strCustomerID:
                return rental
                    
        return None
                

    Found =  Loop_Active_Rentals(strCustomerID)

    while Found == None:
            YesNo = input("Rental cannot be found. Would you like to try another customer ID? (yes/no): ").lower()
            if YesNo == "no":
                print("Returning to main menu.")
                return
            elif YesNo == 'yes':
                strCustomerID = ValidateCustomerID()
                Found = Loop_Active_Rentals(strCustomerID)
            else:
                print("Please enter 'yes' or 'no'.")

    print("Customer: ", Found.customer.name)

    if Found.rental_period == "hourly":
        strHoursDaysWeeks = "hour(s)"
    elif Found.rental_period == "daily":
        strHoursDaysWeeks = "day(s)"
    else:
        strHoursDaysWeeks = "week(s)"

    intActualLength = Validate_Length(strHoursDaysWeeks)
    
    dblFinalPrice = Found.calculate_final_bill(Rental_Shop_obj, intActualLength)

    intTotalItems = Found.get_total_items()
    dblSubtotal = Rental_Shop_obj.ski_inventory.get_best_price(Found.ski_quantity, Found.rental_period, intActualLength) + Rental_Shop_obj.snowboard_inventory.get_best_price(Found.snowboard_quantity, Found.rental_period, intActualLength)
    dblAfterFam = Rental_Shop_obj.calculate_family_discount(dblSubtotal, intTotalItems)
    dblFamDiscount = dblSubtotal - dblAfterFam
    dblAfterCoupon = Rental_Shop_obj.calculate_coupon_discount(dblAfterFam, Found.coupon_code)
    dblCouponDiscount = dblAfterFam - dblAfterCoupon


    print("")
    print("-------Final Price------")
    print("")
    print(f"Customer Name: {Found.customer.name}")
    print(f"Customer ID: {Found.customer.id_number}")
    print(f"Skis Rented: {Found.ski_quantity}")
    print(f"Snowboards Rented: {Found.snowboard_quantity}")
    print(f"Rental Period: {Found.rental_period}")
    print(f"Actual Rental Length: {intActualLength} {strHoursDaysWeeks}")
    print("")
    print(f"Price before discounts: ", "${:,.2f}".format(dblSubtotal))
    print(f"Family Discount: ", "${:,.2f}".format(dblFamDiscount))
    print(f"Coupon Discount: ", "${:,.2f}".format(dblCouponDiscount))
    print(f"Final Price: ", "${:,.2f}".format(dblFinalPrice))
    print("")
    
    YesNo = input("Are your ready to finalize the return?(yes/no): ")

    if YesNo == "no":
        print("Returning to main menu.")
        return
    elif YesNo == "yes":
        Rental_Shop_obj.return_skis(Found.ski_quantity)
        Rental_Shop_obj.return_snowboards(Found.snowboard_quantity)
        lstActiveRentals.remove(Found)
        Rental_Shop_obj.add_daily_totals(0, 0, dblFinalPrice)
        print("Return completed.")
    else:
        print("Please enter 'yes' or 'no'.")
        return

def Show_Inventory():

    print("")
    print("------Current Inventory------")
    print("Ski Inventory:", Rental_Shop_obj.ski_inventory.quantity_available)
    print("Snowboard Inventory:", Rental_Shop_obj.snowboard_inventory.quantity_available)
    print("-----------------------------")

def End_Of_Day():

    print("")
    print("------End of Day Report------")
    print("Total Skis Rented:", Rental_Shop_obj.daily_skis_rented)
    print("Total Snowboards Rented:", Rental_Shop_obj.daily_snowboards_rented)
    print("Total Revenue: ", "${:,.2f}".format(Rental_Shop_obj.daily_revenue))
    print("-----------------------------")
    global blnEndOfDay
    blnEndOfDay = True

def Main_Menu():

    print("")
    print("      Bob's Ski & Snowboard Rentals      ")
    print("")
    print("               Main Menu:                ")
    print("")
    print(" 1. New Customer Rental ")
    print(" 2. Rental Return ")
    print(" 3. Show Inventory ")
    print(" 4. End of Day ")
    print("")

    intMenuSelection = Validate_Menu_Selection()

    return intMenuSelection






#-------------------------------------------------------------------
# Main
#-------------------------------------------------------------------

lstActiveRentals = []

starting_ski_inventory = Validate_Ski_Inventory()
starting_snowboard_inventory = Validate_Snowboard_Inventory()

Rental_Shop_obj = RentalShop(starting_ski_inventory, starting_snowboard_inventory)

blnEndOfDay = bool(False)

while blnEndOfDay == False:

    intMenuSelection = Main_Menu()

    if intMenuSelection == 1:
        New_Customer_Rental()
    elif intMenuSelection == 2:
        Rental_Return()
    elif intMenuSelection == 3:
        Show_Inventory()
    else:
        End_Of_Day()
  
