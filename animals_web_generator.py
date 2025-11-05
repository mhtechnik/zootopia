import json
from pathlib import Path
from html import escape  # falls Namen/Orte Sonderzeichen enthalten

TEMPLATE_PATH = Path("animals_template.html")
DATA_PATH = Path("animals_data.json")
OUTPUT_PATH = Path("animals.html")

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as h:
        return json.load(h)

def make_animals_html_items(animals):
    """Erzeugt den HTML-String mit <li class="cards__item"> und <br/>-Zeilen."""
    output = ""

    for animal in animals:
        name = animal.get("name")
        diet = (animal.get("characteristics") or {}).get("diet")
        type_ = (animal.get("characteristics") or {}).get("type")
        locations = animal.get("locations") or []
        first_location = locations[0] if isinstance(locations, list) and locations else None

        # Baue den <li>-Block nur, wenn es mind. ein Feld gibt
        lines = []
        if name:
            lines.append(f"Name: {escape(name)}<br/>")
        if diet:
            lines.append(f"Diet: {escape(diet)}<br/>")
        if first_location:
            lines.append(f"Location: {escape(first_location)}<br/>")
        if type_:
            lines.append(f"Type: {escape(type_)}<br/>")

        if lines:
            output += '<li class="cards__item">'
            # Newlines im String sind optional, Browser ignoriert Whitespace
            output += "\n" + "\n".join(lines) + "\n"
            output += "</li>\n"

    return output

def main():
    animals = load_data(DATA_PATH)
    items_html = make_animals_html_items(animals)

    template_html = TEMPLATE_PATH.read_text(encoding="utf-8")
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", items_html)

    OUTPUT_PATH.write_text(final_html, encoding="utf-8")
    print(f"Fertig! {OUTPUT_PATH.resolve()}")

if __name__ == "__main__":
    main()
