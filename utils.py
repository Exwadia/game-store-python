import json

class Utils:
    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_json(filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def search_json(filename, key, value):
        data = Utils.load_json(filename)
        for item in data:
            if item[key] == value:
                return item
        return None
    
    @staticmethod
    def format_money(value):
        value = float(value)
        return f"Rp{value:,.2f}"

    @staticmethod
    def alert(message):
        print("\n" + "*" * 50)
        print("**" + " " * 14 + message + " " * 14 + "**")
        print("*" * 50 + "\n")