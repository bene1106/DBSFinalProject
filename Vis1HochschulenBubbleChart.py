import pandas as pd
import folium

# Pfad zur CSV-Datei mit den Koordinaten
# file_path = 'E:\FU\DBS\FinalProject\hochschulen_cleaned.csv'

# CSV-Datei laden
hochschulen_df = pd.read_csv('hochschulen_cleaned.csv', delimiter=';')

# Prüfe die Spaltennamen
print(hochschulen_df.columns)

# Interaktive Karte initialisieren, zentriert auf Deutschland
m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

# Jede Hochschule als Punkt auf der Karte hinzufügen
for idx, row in hochschulen_df.iterrows():
    if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
        folium.CircleMarker(
            location=(row['Latitude'], row['Longitude']),
            radius=max(row['Anzahl Studierende'] / 1000, 1),  # Radius anpassen
            popup=f"{row['Hochschulname']}: {row['Anzahl Studierende']} Studierende",
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(m)

# Karte als HTML-Datei speichern
map_path = 'hochschulen_map.html'
m.save(map_path)


print(f"Map has been saved to {map_path}")