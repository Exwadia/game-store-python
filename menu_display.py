from game_manager import GameManager
from  account import Account

class MenuDisplay:
    def __init__(self,current_user):
        self.current_user = current_user
        self.game_manager = GameManager(current_user)
        self.account = Account(current_user)

    def display_menu_admin(self):
        while True:
            self.game_manager.view_games()
            print("1. Add game")
            print("2. View games")
            print("3. Update game")
            print("4. delete game")
            print("5. Exit")

            choice = int(input("Enter choice: "))
            if choice == 1:
                self.game_manager.add_game()
            elif choice == 2:
                self.game_manager.view_games()
            elif choice == 3:
                self.game_manager.update_game()
            elif choice == 4:
                self.game_manager.delete_game()
            elif choice == 5:
                exit()
            else:
                print("Invalid choice")

    def display_menu_user(self):
        while True:
            self.game_manager.view_games()
            print("1. cari game")
            print("2. Sorting game")
            print("3. Cek akun")
            print("4. Cek saldo")
            print("5. Exit")

            choice = int(input("Enter Choice : "))

            if choice == 1:
                self.game_manager.search_game()
            elif choice == 2:
                self.game_manager.sort_game()
            elif choice == 4:
                self.account.display_balance()
            elif choice == 5:
                exit()
            else:
                print("Invalid choice")