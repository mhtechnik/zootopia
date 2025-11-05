import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def print_animal_info(animal):
    """Prints available animal information based on nested structure."""
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    type_ = animal.get("characteristics", {}).get("type")

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if locations and isinstance(locations, list):
        print(f"Location: {locations[0]}")
    if type_:
        print(f"Type: {type_}")
    print()  # Leerzeile zwischen Einträgen


def main():
    animals_data = load_data("animals_data.json")

    # Iteriere über alle Tiere in der Liste
    for animal in animals_data:
        print_animal_info(animal)


if __name__ == "__main__":
    main()
