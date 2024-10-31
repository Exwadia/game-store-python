from auth import Auth
from utils import Utils
class Transaction:
    def __init__(self,current_user):
        self.json_file = 'json/transactions.json'
        self.current_user = current_user
        self.auth = Auth()
        transactions = Utils.load_json(self.json_file)

        self.transactions = []

        for transaction in transactions:
            if(transaction['username'] == self.current_user['username']):
                self.transactions.append(transaction)

    def create_transaction(self,game):
        if float(self.current_user['balance']) < float(game['harga']):
            Utils.alert("Saldo tidak cukup")
            return

        
        confirm = input(f"Apakah anda yakin ingin membeli {game['nama']}? (y/n): ").lower()

        if confirm != 'y':
            return

        self.transactions.append({
            'username': self.current_user['username'],
            'game': game
        })
        Utils.save_json(self.json_file, self.transactions)

        new_balance = float(self.current_user['balance']) - float(game['harga'])

        self.auth.update_balance(new_balance, self.current_user) 

