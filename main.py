class Penalty:
    def __init__(self, penalty_type, amount, city):
        self.penalty_type = penalty_type
        self.amount = amount
        self.city = city

    def __str__(self):
        return f"Тип: {self.penalty_type}, Сума: {self.amount}, Місто: {self.city}"

class Person:
    def __init__(self, personal_code, name, city):
        self.personal_code = personal_code
        self.name = name
        self.city = city
        self.penalties = []

    def add_penalty(self, penalty):
        self.penalties.append(penalty)

    def remove_penalty(self, penalty):
        self.penalties.remove(penalty)

    def update_info(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        penalties_info = "\n".join([str(penalty) for penalty in self.penalties])
        return f"Персональний код: {self.personal_code}\nІм'я: {self.name}\nМісто: {self.city}\nШтрафи:\n{penalties_info}"


