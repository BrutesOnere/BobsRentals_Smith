# snowboard.py

from rental_equipment import RentalEquipment

class Snowboard(RentalEquipment):
    def __init__(self):
        # Snowboard rates:
        # Hourly: $10, Daily: $40, Weekly: $160
        RentalEquipment.__init__(self, "Snowboard", "snowboard", 10, 40, 160)
