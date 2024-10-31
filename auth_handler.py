from auth import Auth

class AuthHandler:
    def __init__(self,main):
        self.user = None
        self.main = main

    def display_auth(self):
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = int(input("Enter choice: "))

        if choice not in [1, 2, 3]:
            print("Invalid choice")
            return None

        username = input("Enter username: ")
        password = input("Enter password: ")

        auth = Auth()

        if choice == 1:
            user = auth.login(username,password)
        elif choice == 2:
            user = auth.register(username,password)
        else:
            print("Exiting...")
            exit()

        self.user = user
        return user
