# test_bobs_rentals.py

from customer import Customer
from rental import Rental
from rental_shop import RentalShop

def main():
    # Create the shop and set starting inventory
    shop = RentalShop()
    shop.set_starting_inventory(10, 8)

    print("Starting skis:", shop.get_available_skis())
    print("Starting snowboards:", shop.get_available_snowboards())

    # Create a customer
    customer = Customer("Alice Smith", "CUST1001")

    # Create a rental: 4 hours, family rental, coupon code
    rental = Rental(customer, 4, True, "SAVE10BBP")

    # Add equipment to the rental
    rental.add_skis(2)
    rental.add_snowboards(2)

    print("Total items for rent:", rental.get_total_items())
   
    # Check inventory before renting
    if shop.can_rent_skis(2) and shop.can_rent_snowboards(2):
        # Get estimated cost before renting
        estimated_cost = rental.calculate_estimate()
        print("Estimated cost:", estimated_cost)

        # Rent the items and update shop totals
        shop.rent_items(2, 2, estimated_cost)

        print("Available skis:", shop.get_available_skis())
        print("Available snowboards:", shop.get_available_snowboards())
        print("Total skis rented today:", shop.get_total_skis_rented_today())
        print("Total snowboards rented today:", shop.get_total_snowboards_rented_today())
        print("Total revenue today:", shop.get_total_revenue_today())

        # Calculate final bill
        final_bill = rental.calculate_final_bill(5)
        print("Final bill:", final_bill)

        # Return items to the shop inventory
        shop.return_items(2, 2)
        print("Available skis after returns:", shop.get_available_skis())
        print("Available snowboards after returns:", shop.get_available_snowboards())
    else:
        print("Not enough inventory for this rental.")

if __name__ == "__main__":
    main()
