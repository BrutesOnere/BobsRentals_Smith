# ski.py

from rental_equipment import RentalEquipment

class Ski(RentalEquipment):
    def __init__(self):
        # Ski rates:
        # Hourly: $15, Daily: $50, Weekly: $200
        RentalEquipment.__init__(self, "Ski", "ski", 15, 50, 200)
