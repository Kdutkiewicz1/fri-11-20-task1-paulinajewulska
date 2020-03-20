class Client:
    def __init__(self, name: str, surname: str, cash: float):
        self.name = name
        self.surname = surname
        self.cash = cash


class Bank:
    def __init__(self):
        self.clients: list = [Client("Jan", "Kowalski", 1000)]

    def add_client(self, name: str, surname: str, cash: float):
        self.clients.append(Client(name, surname, cash))

    def add_cash(self, name: str, surname: str, cash: float, added_cash: float):
        for client in self.clients:
            if client.name is name and client.surname is surname and client.cash is cash:
                client.cash += added_cash

    def remove_cash(self, name: str, surname: str, cash: float, removed_cash: float):
        for client in self.clients:
            if client.name is name and client.surname is surname and client.cash == cash:
                if client.cash >= removed_cash:
                    client.cash -= removed_cash
                elif client.cash < removed_cash:
                    print("Not enough money")

    def transfer_money(self, client_1_name: str, client_1_surname: str, client_1_cash: float, client_2_name: str,
                       client_2_surname: str, client_2_cash: float, transfered_cash: float):
        for client in self.clients:
            if client.name is client_1_name and client.surname is client_1_surname and client.cash == client_1_cash:
                for another_client in self.clients:
                    if client.name is client_2_name and client.surname is client_2_surname and client.cash == client_2_cash:
                        if client.cash >= transfered_cash:
                            another_client.cash += transfered_cash
                            client.cash -= another_client
                        else:
                            print("Not enough money")


if __name__ == '__main__':
    bank = Bank()
    bank.add_client("Marek", "Nowak", 2000)
    bank.add_client("Weronika", "Kowalska", 1200)
    bank.add_client("Agnieszka", "Kowalska", 3000)
    bank.add_cash("Agnieszka", "Kowalska", 3000, 100)
    bank.remove_cash("Agnieszka", "Kowalska", 3100, 1000)
    bank.remove_cash("Agnieszka", "Kowalska", 2100, 4000)
    bank.transfer_money("Marek", "Nowak", 2000, "Weronika", "Kowalska", 1200, 100)
    for client in bank.clients:
        print("{}, {}, {}".format(client.name, client.surname, client.cash))
