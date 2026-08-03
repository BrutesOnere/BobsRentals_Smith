# rental_shop.py

class RentalShop:
    def __init__(self):
        # Starting inventory
        self._starting_ski_inventory = 0
        self._starting_snowboard_inventory = 0

        # Current available inventory
        self._available_skis = 0
        self._available_snowboards = 0

        # Daily totals
        self._total_skis_rented_today = 0
        self._total_snowboards_rented_today = 0
        self._total_revenue_today = 0.0

    def set_starting_inventory(self, ski_count, snowboard_count):
        self._starting_ski_inventory = ski_count
        self._starting_snowboard_inventory = snowboard_count

        self._available_skis = ski_count
        self._available_snowboards = snowboard_count

    def get_available_skis(self):
        return self._available_skis

    def get_available_snowboards(self):
        return self._available_snowboards

    def can_rent_skis(self, quantity):
        return quantity <= self._available_skis

    def can_rent_snowboards(self, quantity):
        return quantity <= self._available_snowboards

    def rent_items(self, ski_quantity, snowboard_quantity, rental_amount):
        # Reduce inventory
        self._available_skis = self._available_skis - ski_quantity
        self._available_snowboards = self._available_snowboards - snowboard_quantity

        # Update daily totals
        self._total_skis_rented_today = self._total_skis_rented_today + ski_quantity
        self._total_snowboards_rented_today = self._total_snowboards_rented_today + snowboard_quantity
        self._total_revenue_today = self._total_revenue_today + rental_amount

    def return_items(self, ski_quantity, snowboard_quantity):
        # Restore inventory
        self._available_skis = self._available_skis + ski_quantity
        self._available_snowboards = self._available_snowboards + snowboard_quantity

    def get_total_skis_rented_today(self):
        return self._total_skis_rented_today

    def get_total_snowboards_rented_today(self):
        return self._total_snowboards_rented_today

    def get_total_revenue_today(self):
        return self._total_revenue_today
