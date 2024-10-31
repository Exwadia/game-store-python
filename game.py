from utils import Utils

class Game :
    def __init__(self):
        self.json_file = 'json/games.json'
        self.games = Utils.load_json(self.json_file)
    


    def get_games(self):
        return self.games

    def create_game(self, game):
        self.games.append(game)
        Utils.save_json(self.json_file, self.games)

    def update_game(self, index,updated_game):
        self.games[index].update(updated_game)
        Utils.save_json(self.json_file, self.games)

    def delete_game(self, index):
        self.games.pop(index)
        Utils.save_json(self.json_file, self.games)

    def search_game(self,search):
        results = []
        for game in self.games:
            if(search.lower() in game['nama'].lower()):
                results.append(game)
        
        return results

    def is_exist(self, game):
        return game in self.games

    def is_valid_game_index(self, index):
        return 0 < index <= len(self.games)

    def sort_by_latest(self):
        return sorted(self.games, key=lambda x: x['rilis'], reverse=True)

    def sort_by_highest_price(self):
        return sorted(self.games, key=lambda x: x['harga'], reverse=True)

    def sort_by_lowest_price(self):
        return sorted(self.games, key=lambda x: x['harga'])
