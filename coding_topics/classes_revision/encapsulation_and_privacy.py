class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def __add_interest(self, interest_rate):
        self.__balance += self.__balance * interest_rate

    def add_yearly_interest(self):
        self.__add_interest(0.02)


if __name__ == "__main__":
    bank_account = BankAccount(1234, 100)
    bank_account.add_yearly_interest()
