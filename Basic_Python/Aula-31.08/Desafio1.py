class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depósito de R${amount:.2f} realizado. Novo saldo: R${self.balance:.2f}")
        else:
            print("Valor inválido para depósito.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Saque de R${amount:.2f} realizado. Novo saldo: R${self.balance:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def transfer(self, recipient_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferência de R${amount:.2f} realizada para a conta {recipient_account.account_number}. Novo saldo: R${self.balance:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para transferência.")


if __name__ == "__main__":
    account1 = BankAccount("123456", 1000.0)
    account2 = BankAccount("789012", 500.0)

    account1.deposit(300.0)
    account1.withdraw(200.0)
    account1.transfer(account2, 400.0)

    print("Saldo final da conta 1:", account1.balance)
    print("Saldo final da conta 2:", account2.balance)
