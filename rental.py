# rental.py

from ski import Ski
from snowboard import Snowboard

class Rental:
    def __init__(self, customer, rental_hours, is_family_rental, coupon_code):
        # One customer per rental
        self._customer = customer
        self._rental_hours = rental_hours  # total hours for the rental
        self._is_family_rental = is_family_rental
        self._coupon_code = coupon_code

        # Quantities of each equipment type
        self._ski_quantity = 0
        self._snowboard_quantity = 0

        # Stored cost values
        self._estimated_cost = 0.0
        self._final_cost = 0.0

        # Equipment objects (polymorphism)
        self._ski_equipment = Ski()
        self._snowboard_equipment = Snowboard()

    def add_skis(self, quantity):
        self._ski_quantity = self._ski_quantity + quantity

    def add_snowboards(self, quantity):
        self._snowboard_quantity = self._snowboard_quantity + quantity

    def get_total_items(self):
        return self._ski_quantity + self._snowboard_quantity

    def _calculate_base_cost(self, hours):
        # Best price per equipment type
        ski_cost = self._ski_equipment.calculate_best_price_for_hours(hours) * self._ski_quantity
        snowboard_cost = self._snowboard_equipment.calculate_best_price_for_hours(hours) * self._snowboard_quantity
        return ski_cost + snowboard_cost

    def _apply_family_discount(self, amount):
        total_items = self.get_total_items()
        if total_items >= 3 and total_items <= 5:
            # 25% discount
            discount = amount * 0.25
            amount = amount - discount
        return amount

    def _apply_coupon_discount(self, amount):
        # Coupon code ending in "BBP" gets 10% discount
        if self._coupon_code is not None and self._coupon_code.endswith("BBP"):
            discount = amount * 0.10
            amount = amount - discount
        return amount

    def calculate_estimate(self):
        base_cost = self._calculate_base_cost(self._rental_hours)

        # Apply discounts
        amount_after_family = self._apply_family_discount(base_cost)
        final_amount = self._apply_coupon_discount(amount_after_family)

        self._estimated_cost = final_amount
        return self._estimated_cost

    def calculate_final_bill(self, actual_hours):
        base_cost = self._calculate_base_cost(actual_hours)

        amount_after_family = self._apply_family_discount(base_cost)
        final_amount = self._apply_coupon_discount(amount_after_family)

        self._final_cost = final_amount
        return self._final_cost

    def get_estimated_cost(self):
        return self._estimated_cost

    def get_final_cost(self):
        return self._final_cost
