class Client:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __hash__(self):
        return hash((self.name, self.surname))

    def __eq__(self, other):
        return (self.name, self.surname) == (other.name, other.surname)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Account:
    def __init__(self, cash: float):
        self.cash = cash


class Bank:
    def __init__(self):
        self.clients: dict = {}

    def add_client(self, new_client: Client, cash: float):
        self.clients[new_client] = Account(cash)

    def add_cash(self, client: Client, cash_to_add: float):
        self.clients[client].cash += cash_to_add

    def remove_cash(self, client: Client, cash_to_remove: float):
        if self.clients[client].cash < cash_to_remove:
            print("Not enough cash to remove\n")
        else:
            self.clients[client].cash -= cash_to_remove

    def transfer_money(self, client_from, client_to, cash_to_transfer):
        if self.clients[client_from].cash < cash_to_transfer:
            print("Not enough cash to transfer\n")
        else:
            self.clients[client_from].cash -= cash_to_transfer
            self.clients[client_to].cash += cash_to_transfer

    def __str__(self):
        result = ""
        for client, account in self.clients.items():
            result += ("{} {}: {}\n".format(client.surname, client.name, account.cash))
        return result


if __name__ == '__main__':

    bank = Bank()
    marek_nowak = Client("Marek", "Nowak")
    weronika_kowalska = Client("Weronika", "Kowalska")
    agnieszka_kowalska = Client("Agnieszka", "Kowalska")

    bank.add_client(marek_nowak, cash=2000)
    bank.add_client(weronika_kowalska, cash=2000)
    bank.add_client(agnieszka_kowalska, cash=2000)
    bank.add_cash(marek_nowak, cash_to_add=1000)
    bank.remove_cash(weronika_kowalska, cash_to_remove=100)
    bank.transfer_money(client_from=agnieszka_kowalska, client_to=marek_nowak, cash_to_transfer=500)

    print(bank)

    bank_2 = Bank()
    anna_nowak = Client("Anna", "Nowak")
    bank_2.add_client(anna_nowak, cash=2000)
    print(bank_2)
