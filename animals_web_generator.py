import json
from pathlib import Path
from html import escape

TEMPLATE_PATH = Path("animals_template.html")
DATA_PATH = Path("animals_data.json")
OUTPUT_PATH = Path("animals.html")


def load_data(file_path):
    """Lädt die JSON-Daten."""
    with open(file_path, "r", encoding="utf-8") as h:
        return json.load(h)


def serialize_animal(animal_obj):
    """Serialisiert ein einzelnes Tier zu HTML (<li>...</li>)"""
    characteristics = animal_obj.get("characteristics", {})
    name = animal_obj.get("name")
    diet = characteristics.get("diet")
    type_ = characteristics.get("type")
    locations = animal_obj.get("locations", [])
    first_location = locations[0] if isinstance(locations, list) and locations else None

   
    if not name:
        return ""

    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{escape(name)}</div>\n'
    output += '  <p class="card__text">\n'

    if diet:
        output += f'      <strong>Diet:</strong> {escape(diet)}<br/>\n'
    if first_location:
        output += f'      <strong>Location:</strong> {escape(first_location)}<br/>\n'
    if type_:
        output += f'      <strong>Type:</strong> {escape(type_)}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    """Liest Daten, generiert HTML und ersetzt Platzhalter in der Vorlage."""
    animals = load_data(DATA_PATH)

    
    output = ""
    for animal_obj in animals:
        output += serialize_animal(animal_obj)

   
    template_html = TEMPLATE_PATH.read_text(encoding="utf-8")
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)

   
    OUTPUT_PATH.write_text(final_html, encoding="utf-8")
    print(f"Datei erstellt: {OUTPUT_PATH.resolve()}")


if __name__ == "__main__":
    main()
