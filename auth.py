from utils import Utils

class Auth:
    def __init__(self):
        # self.username = username
        self.users = Utils.load_json('json/users.json')
        # self.password = password

    def login(self, username, password):
        user = self.get_user(username,password)
        if user:
            Utils.alert("Login Success")
            return user
        else:
            Utils.alert("Login Failed")
            return False

    def register(self,username,password):
        user = self.get_user(username,password)
        if user:
            Utils.alert("User already exists")
            return False
        else:
            self.users.append({
                'username': username,
                'password': password,
                'role' : 'user',
                'balance' : 0
            })
            Utils.save_json('json/users.json', self.users)
            Utils.alert("Register success")
            return self.get_user()
    
    def get_user(self,username,password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.username = user['username']
                return user
        return False
    
    def update_balance(self, balance, current_user):
        for user in self.users:
            if user['username'] == current_user['username']:
                user['balance'] = balance
                Utils.save_json('json/users.json', self.users)
                return True
        return False