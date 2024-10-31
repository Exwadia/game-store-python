from auth_handler import AuthHandler
from menu_display import MenuDisplay

class Main:
    def __init__(self):
        self.auth_handler = AuthHandler(self)
        self.menu_display = None

    def main(self):
        while not self.auth_handler.user:
            self.auth_handler.user = self.auth_handler.display_auth()

        self.menu_display = MenuDisplay(self.auth_handler.user)
            
        if self.auth_handler.user['role'] == 'admin':
            self.menu_display.display_menu_admin()
        elif self.auth_handler.user['role'] == 'user':
            self.menu_display.display_menu_user()

if __name__ == "__main__":
    main = Main()
    main.main()