import json

def cargar_archivo(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_new_pokemon():
    poke_name = input("Enter the name of the Pokemon: ")
    poke_type = input("Enter the type of the Pokemon: ")

    base_stats = {}
    for stat in ['HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed']:
            while True:
                try:
                    value = int(input(f"Enter the {stat} of the Pokemon: "))
                    base_stats[stat] = value
                    break
                except ValueError:
                    print("Please enter a valid integer for the base stats.")
    new_pokemon = {
        'name': poke_name.strip().capitalize(),
        'type': [poke_type.strip().capitalize()],
        'base': base_stats
    }
    return new_pokemon

def main():
    file_path = 'pokemons.json'
    data = cargar_archivo(file_path)
    data.append(add_new_pokemon())
    write_json_file(file_path, data)
    print("New Pokemon added successfully!")

main()