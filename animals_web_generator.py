import json
from pathlib import Path

TEMPLATE_PATH = Path("animals_template.html")
DATA_PATH = Path("animals_data.json")
OUTPUT_PATH = Path("animals.html")

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def make_animals_html(animals):
    """Erzeugt HTML-Listeneinträge für alle Tiere."""
    html_blocks = []

    for animal in animals:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations", [])
        first_location = locations[0] if locations else None
        type_ = animal.get("characteristics", {}).get("type")

        
        html = '<li class="cards__item">\n'
        if name:
            html += f'  <h2 class="card__title">{name}</h2>\n'
        html += '  <div class="card__text">\n'
        if diet:
            html += f'    <p><strong>Diet:</strong> {diet}</p>\n'
        if first_location:
            html += f'    <p><strong>Location:</strong> {first_location}</p>\n'
        if type_:
            html += f'    <p><strong>Type:</strong> {type_}</p>\n'
        html += '  </div>\n'
        html += '</li>\n'

        html_blocks.append(html)

    return "\n".join(html_blocks)

def main():
    
    animals = load_data(DATA_PATH)

    
    animals_html = make_animals_html(animals)

    
    template_html = TEMPLATE_PATH.read_text(encoding="utf-8")
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    
    OUTPUT_PATH.write_text(final_html, encoding="utf-8")
    print(f"✅ Fertig! Datei gespeichert unter: {OUTPUT_PATH.resolve()}")

if __name__ == "__main__":
    main()
