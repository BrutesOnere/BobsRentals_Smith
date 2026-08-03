# Bob's Ski & Snowboard Rentals – Class Library

Name: Michael Smith  
Assignment: Final Part 1

Project description

My repository contains a reusable Python class library for Bob's Ski & Snowboard Rentals. I focuses on classes, properties, and methods needed to manage customers, equipment, pricing, best pricing, discounts, inventory, and daily totals.

# Classes

- RentalEquipment: Parent class for rental equipment with shared rates and best price logic.
- Ski: Inherits from 'RentalEquipment', uses ski rental rates.
- Snowboard: Inherits from 'RentalEquipmen', uses snowboard rental rates.
- Customer: Stores customer names and ID.
- Rental: Represents a single rental for one customer, including quantity, rental period, discount, and price calculations.
- RentalShop: Manages starting inventory, available inventory, and daily total for rental and revenue.

# Important properties and methods

- RentalEquipment
  - 'calculate_best_price_for_hours(total_hours)': Returns lowest price using hourly, daily, or weekly rate.
- Ski / Snowboard
  - Inherits all methods from 'RentalEquipment' but use different rate.
- Customer
  - 'get_name()', 'get_customer_id()': Access customer information.
- Rental
  - 'add_ski(quantity)', 'add_snowboard(quantity)': Set quantity for the rental.
  - 'calculate_estimate()': Estimate cost using best price and discounts.
  - 'calculate_final_bill(actual_hours)': Final bill based on rental length.
- RentalShop
  - 'set_starting_inventory(ski_count, snowboard_count)': Initialize inventory.
  - 'can_rent_skis(quantity)', 'can_rent_snowboards(quantity)': Validate availability.
  - 'rent_items(ski_quantity, snowboard_quantity, rental_amount)': Update inventory and daily totals.
  - 'return_items(ski_quantity, snowboard_quantity)': Restore inventory.
  - 'get_total_skis_rented_today()', 'get_total_snowboards_rented_today()', 'get_total_revenue_today()': Daily totals.

# Object-oriented concepts

- Encapsulation: Attributes are stored as '_private_' fields and accessed through methods (e.g. 'get_name')

- Inheritance: 'Ski/Snowboard' inherit from 'RentalEquipment', sharing common behavior and structure.

- Polymorphism: Both 'Ski/Snowboard' use 'calculate_best_price_for_hours, but with different rates, allowing the same method to behave differently depending on the object type.

- Abstraction: 'RentalEquipment' represents general rental equipment; concrete types ('Ski', 'Snowboard') provide specific details while using the same interface.

# how to test

1. Clone BobsRentals_Smith repository.
2. Make sure all .py files are in the same folder.
3. Run the testing file by executing: python test_bobs_rentals.py
