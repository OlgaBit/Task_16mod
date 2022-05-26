class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f""'{self.name} {self.surname}".{self.city}. Баланс: {self.balance} руб."'

    def get_quest(self):
        return f'{self.name} {self.surname},г.{self.city}'

clients_1 = Clients('Иван', 'Петров', 'Москва', 50)
clients_2 = Clients('Петр', 'Иванов', 'Волгоград', 150)
clients_3 = Clients('Василий','Сидоров','Рязань', 200)
print(clients_1)

quest_list=[clients_1, clients_2, clients_3]
