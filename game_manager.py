from transaction import Transaction
from game import Game
from utils import Utils
from prettytable import PrettyTable

class GameManager:
    def __init__(self,current_user):
        self.game = Game()
        self.transaction = Transaction(current_user)

    def is_valid_game_index(self, index,games):
        return 0 < index <= len(games)

    
    def show_table(self,games):
        table = PrettyTable(['Index', 'Nama', 'Rilis', 'Pengembang', 'Genre', 'Harga'])
        for index, game in enumerate(games):
            table.add_row([index + 1, game['nama'], game['rilis'], game['pengembang'], game['genre'], Utils.format_money(game['harga'])])
        print(table)

    def view_games(self):
        games = self.game.get_games()
        self.show_table(games)
       
    def add_game(self):
        while True:
            nama = input("Enter game name: ")
            rilis = input("Enter release date: ")
            pengembang = input("Enter developer: ")
            genre = input("Enter genre: ")
            deskripsi = input("Enter description: ")
            harga = input("Enter price: ")

            self.game.create_game({
                'nama': nama,
                'rilis': rilis,
                'pengembang': pengembang,
                'genre': genre,
                'deskripsi': deskripsi,
                'harga': harga
            })

            print("Game added successfully")
            again = input("Apakah anda ingin menambahkan game lagi? (y/n): ").lower()
            if again != 'y':
                break

    def update_game(self):
        while True:
            index = int(input("Enter game no : "))

            if not self.is_valid_game_index(index,self.game.games):
                print("No data found for the given game number. Please try again.")
                continue

            selected_game = self.game.games[index - 1]
            nama = input(f"Enter game name (default: {selected_game['nama']}): ") or selected_game['nama']
            rilis = input(f"Enter release date (default: {selected_game['rilis']}): ") or selected_game['rilis']
            pengembang = input(f"Enter developer (default: {selected_game['pengembang']}): ") or selected_game['pengembang']
            genre = input(f"Enter genre (default: {selected_game['genre']}): ") or selected_game['genre']
            deskripsi = input(f"Enter description (default: {selected_game['deskripsi']}): ") or selected_game['deskripsi']
            harga = input(f"Enter price (default: {selected_game['harga']}): ") or selected_game['harga']

            updated_game = {
                'nama': nama,
                'rilis': rilis,
                'pengembang': pengembang,
                'genre': genre,
                'deskripsi': deskripsi,
                'harga': harga
            }

            self.game.update_game(index - 1,updated_game)

            print("Game updated successfully")
            again = input("Apakah anda ingin mengupdate game lagi? (y/n): ").lower()
            if again != 'y':
                break

    def delete_game(self):
        while True:
            self.view_games()
            index = int(input("Enter game no : "))

            if not self.is_valid_game_index(index,self.game.games):
                print("No data found for the given game number. Please try again.")
                continue;

            confirm = input("Konfirmasi hapus (y/n):")

            if confirm != 'y':
                break
        
            self.game.delete_game(index - 1)


            print("Game deleted successfully")
            again = input("Apakah anda ingin menghapus game lagi? (y/n): ").lower()
            if again != 'y':
                break
    
    def search_game(self):
        while True:
            search = input("Input Nama Game: ")

            games = self.game.search_game(search)

            if games:
                self.show_table(games)
            else:
                Utils.alert("No Data Found")
                continue;

            print("1. Pilih Game")
            print("2. Searching lagi")
            print("3. Ke Menu")

            choice = int(input("Masukkan pilihan: "))

            if choice == 1:
                if self.buy_game(games):
                    break
            elif choice == 2:
                continue
            elif choice == 3:
                break

    def sort_game(self):
        while True:
            print("1. Sorting berdasarkan baru")
            print("2. Sorting berdasarkan harga tertinggi")
            print("3. Sorting berdasarkan harga terendah")
            print("4. Kembali ke menu")

            choice = int(input("Masukkan pilihan: "))

            if choice == 1:
                games = self.game.sort_by_latest()
                self.show_table(games)
            elif choice == 2:
                games = self.game.sort_by_highest_price()
                self.show_table(games)
            elif choice == 3:
                games = self.game.sort_by_lowest_price()
                self.show_table(games)
            elif choice == 4:
                break

            print("1. Pilih Game")
            print("2. Kembali ke sorting")
            print("3. Kembali ke menu")

            choice = int(input("Masukkan pilihan: "))

            if choice == 1:
                if self.buy_game(games):
                    break
            elif choice == 2:
                continue
            elif choice == 3:
                break
    

    def buy_game(self,games):
        while True:
            index = int(input("Masukkan no game: "))

            if not self.is_valid_game_index(index, games):
                print("No data found for the given game number. Please try again.")
                continue

            game = games[index - 1]

            print("Deskripsi", game['nama'],":")
            print(game['deskripsi'])
            print("")
            print("1. Beli")
            print("2. Kembali ke searching")
            print("3. Kembali ke menu")

            choice = int(input("Masukkan pilihan: "))

            if choice == 1:
                if self.transaction.create_transaction(game):
                    Utils.alert("Game berhasil dibeli")
                return True
            elif choice == 2:
                return False  
            elif choice == 3:
                return True  