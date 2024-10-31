from utils import Utils
from auth import Auth
class Account:
    def __init__(self,current_user):
        self.current_user = current_user
        self.auth = Auth()

    def check_balance(self):
        for user in self.auth.users:
            if user['username'] == self.current_user['username']:
                return user['balance']
            continue
    
    def top_up(self):
        balance = self.check_balance() or 0
        amount = int(input("Enter amount: "))
        new_balance = float(balance) + float(amount)
        # self.auth.update_balance(new_balance)
        self.auth.update_balance(new_balance, self.current_user)

        Utils.alert("Top up success")
    
    def display_balance(self):
        while True:
            balance = self.check_balance()
            Utils.alert(f"Your balance is {Utils.format_money(balance)}")

            choice = input("Do you want to top up? (y/n): ").lower()

            if choice != 'y':
                break

            self.top_up()


