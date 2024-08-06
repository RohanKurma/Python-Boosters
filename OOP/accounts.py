import datetime
import pytz


class Accounts:
    """Simple Account class with balance"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        self.deposit(balance)
        print("Account Created for "+self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
            self.transaction_list.append((Accounts._current_time(), amount))
            self.show_balance()
    
    def withdraw(self, amount):
        if 0 < amount <=self.balance:
            self.balance -= amount
            self.transaction_list.append((Accounts._current_time(), -amount))
        else:
            print(f"The amount must be greater than zero and no more the your balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))
    
    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount>0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':

    tim = Accounts("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    #tim.show_balance()
    tim.withdraw(500)
    #tim.show_balance()
    tim.withdraw(2000)

    tim.show_transactions()


    steph = Accounts('Steph',800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)

