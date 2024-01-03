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

class TaxInspectDB:
    def __init__(self):
        self.people = {}

    def add_person(self, person):
        self.people[person.personal_code] = person

    def remove_person(self, personal_code):
        if personal_code in self.people:
            del self.people[personal_code]

    def add_penalty(self, personal_code, penalty):
        if personal_code in self.people:
            person = self.people[personal_code]
            person.add_penalty(penalty)

    def remove_penalty(self, personal_code, penalty):
        if personal_code in self.people:
            person = self.people[personal_code]
            person.remove_penalty(penalty)

    def update_person_info(self, personal_code, name, city):
        if personal_code in self.people:
            person = self.people[personal_code]
            person.update_info(name, city)

    def print_db(self):
        for personal_code, person in self.people.items():
            print(f"Особа з персональним кодом {personal_code}:\n{person}\n")

    def print_by_code(self, personal_code):
        if personal_code in self.people:
            person = self.people[personal_code]
            print(f"Особа з персональним кодом {personal_code}:\n{person}\n")
        else:
            print(f"Особу не знайдено за таким персональним кодом {personal_code}")

    def print_by_penalty_type(self, penalty_type):
        for personal_code, person in self.people.items():
            penalties = [penalty for penalty in person.penalties if penalty.penalty_type == penalty_type]
            if penalties:
                print(f"Особа з персональним кодом {personal_code} має штраф за  {penalty_type}:\n")
                for penalty in penalties:
                    print(penalty)
                print("\n")

    def print_by_city(self, city):
        for personal_code, person in self.people.items():
            if person.city == city:
                print(f"Особа з персональним кодом{personal_code} живе в  {city}:\n{person}\n")

if __name__ == "__main__":
    db = TaxInspectDB()

    while True:
        print("\nМеню:")
        print("1. Додати особу")
        print("2. Видалити особу")
        print("3. Додати штраф")
        print("4. Видалити штраф")
        print("5. Оновити інформацію про особу")
        print("6. Вивести базу даних")
        print("7. Вивести за персональним кодом")
        print("8. Вивести за типом штрафу")
        print("9. Вивести за містом")
        print("0. Вийти")

        choice = input("Введіть свій вибір: ")

        if choice == "1":
            personal_code = input("Введіть персональний код: ")
            name = input("Введіть ім'я: ")
            city = input("Введіть місто: ")
            person = Person(personal_code, name, city)
            db.add_person(person)

        elif choice == "2":
            personal_code = input("Введіть персональний код для видалення: ")
            db.remove_person(personal_code)

        elif choice == "3":
            personal_code = input("Введіть персональний код: ")
            penalty_type = input("Введіть тип штрафу: ")
            amount = float(input("Введіть суму штрафу: "))
            city = input("Введіть місто: ")
            penalty = Penalty(penalty_type, amount, city)
            db.add_penalty(personal_code, penalty)

        elif choice == "4":
            personal_code = input("Введіть персональний код: ")
            penalty_type = input("Введіть тип штрафу для видалення: ")
            penalties = [penalty for penalty in db.people[personal_code].penalties if penalty.penalty_type == penalty_type]
            if penalties:
                db.remove_penalty(personal_code, penalties[0])
            else:
                print(f"Штрафів з типом {penalty_type} не знайдено")

        elif choice == "5":
            personal_code = input("Введіть персональний код: ")
            name = input("Введіть нове ім'я: ")
            city = input("Введіть нове місто: ")
            db.update_person_info(personal_code, name, city)

        elif choice == "6":
            db.print_db()

        elif choice == "7":
            personal_code = input("Введіть персональний код для виведення: ")
            db.print_by_code(personal_code)

        elif choice == "8":
            penalty_type = input("Введіть тип штрафу для виведення: ")
            db.print_by_penalty_type(penalty_type)

        elif choice == "9":
            city = input("Введіть місто для виведення: ")
            db.print_by_city(city)

        elif choice == "0":
            break

        else:
            print("Невірний вибір. Будь ласка, введіть дійсну опцію.")
