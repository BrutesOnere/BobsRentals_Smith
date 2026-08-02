# rental_equipment.py

class RentalEquipment:
    def __init__(self, name, equipment_type, hourly_rate, daily_rate, weekly_rate):
        # Encapsulated attributes
        self._name = name
        self._equipment_type = equipment_type
        self._hourly_rate = hourly_rate
        self._daily_rate = daily_rate
        self._weekly_rate = weekly_rate

    def get_name(self):
        return self._name

    def get_equipment_type(self):
        return self._equipment_type

    def get_hourly_rate(self):
        return self._hourly_rate

    def get_daily_rate(self):
        return self._daily_rate

    def get_weekly_rate(self):
        return self._weekly_rate

    # Best price based on total hours
    def calculate_best_price_for_hours(self, total_hours):
        # Hourly cost
        hourly_cost = total_hours * self._hourly_rate

        # Daily cost (rounding up to the nearest full day)
        days = total_hours // 24
        if total_hours % 24 != 0:
            days = days + 1
        daily_cost = days * self._daily_rate

        # Weekly cost (rounding up to the nearest full week)
        weeks = total_hours // (24 * 7)
        if total_hours % (24 * 7) != 0:
            weeks = weeks + 1
        weekly_cost = weeks * self._weekly_rate

        # Return the lowest cost
        best_cost = hourly_cost
        if daily_cost < best_cost:
            best_cost = daily_cost
        if weekly_cost < best_cost:
            best_cost = weekly_cost

        return best_cost
