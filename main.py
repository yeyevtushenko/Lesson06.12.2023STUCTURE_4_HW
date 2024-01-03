class Penalty:
    def __init__(self, penalty_type, amount, city):
        self.penalty_type = penalty_type
        self.amount = amount
        self.city = city

    def __str__(self):
        return f"Тип: {self.penalty_type}, Сума: {self.amount}, Місто: {self.city}"

