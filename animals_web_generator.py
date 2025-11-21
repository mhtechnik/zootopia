# animals_web_generator.py
import data_fetcher


def build_html_for_animals(animal_name, animals):
    """Erzeugt den kompletten HTML Text für die Webseite."""

    if not animals:
        # Milestone 3: Fehlermeldung, wenn kein Tier gefunden wurde
        body_html = f"""
        <h2>The animal "{animal_name}" does not exist in the database.</h2>
        <p>Please try another animal name.</p>
        """
    else:
        cards_html_parts = []

        for animal in animals:
            name = animal.get("name", "Unknown")
            locations = ", ".join(animal.get("locations", [])) or "Unknown"
            characteristics = animal.get("characteristics", {})
            diet = characteristics.get("diet", "Unknown")
            lifespan = characteristics.get("lifespan", "Unknown")

            card_html = f"""
            <div class="animal-card">
                <h2>{name}</h2>
                <p><strong>Locations:</strong> {locations}</p>
                <p><strong>Diet:</strong> {diet}</p>
                <p><strong>Lifespan:</strong> {lifespan}</p>
            </div>
            """
            cards_html_parts.append(card_html)

        body_html = "\n".join(cards_html_parts)

    # Du kannst hier natürlich dein altes Zootopia Layout einbauen
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Zootopia Animals - {animal_name}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Animals matching "{animal_name}"</h1>
    {body_html}
</body>
</html>
"""
    return html


def main():
    animal_name = input("Enter a name of an animal: ").strip()
    if not animal_name:
        print("No animal name entered. Aborting.")
        return

    animals = data_fetcher.fetch_data(animal_name)
    html = build_html_for_animals(animal_name, animals)

    with open("animals.html", "w", encoding="utf8") as f:
        f.write(html)

    print('Website was successfully generated to the file animals.html.')


if __name__ == "__main__":
    main()
