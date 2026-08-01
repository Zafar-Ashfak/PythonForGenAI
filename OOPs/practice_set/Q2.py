class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} debited successfully!")

    def credit(self, amount):
        self.balance = self.balance + amount
        print(f"₹{amount} credited successfully!")

    def show_balance(self):
        print(f"Your available balance: {self.balance}")


def main():
    acc = Account(9381911, 8000)
    acc.show_balance()

    amount = int(input("Enter the credit amount: "))
    acc.credit(amount)
    acc.show_balance()

    amount = int(input("Enter the withdraw amount: "))
    acc.debit(amount)
    acc.show_balance()

main()