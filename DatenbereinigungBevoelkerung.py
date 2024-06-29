# Datenbereinugung:
# Bevölkerung reinigen
# -> Zeilen, die nicht vollständig mit Werten ausgefüllt sind werden entfenrt

# Pandas-Bib ermöglicht Datenmanipulation und -analyse:
import pandas as pa

# CSV-Datei laden:
file_path = '/mnt/data/bevoelkerung.csv'  # hier liedt die Datei
# Funktion zum Einlesen: pandas.read
bev = pa.read_csv(file_path, encoding='latin1', delimiter=';', skiprows=6, error_bad_lines=False)
# Parameter:
# encoding = 'latin1': Zeichen werden richtig dargestellt
# delimeter: Trennzeichen der CSV
# skiprows: erste 6 Zeilen überspringen (Tabelle geht da noch nicht los; Metadata)
# (error_bad_lines: nicht notwendig; überspringt Zeilen die nicht eingelesen werden können)


# Zeilen mit fehlenden WErten entfernen:
# dropna() entfernt Spalten, die mindestens einen fehlenden Wert enthalten
# (Standardparameter: how='any' -> min. 1 fehl. val
# axis=0 -> Zeilen)
cleaned_bev = bev.dropna()

# speichern der bereinigten Datei in neue CSV:
cleaned_bev.to_csv('/mnt/data/cleaned_bevoelkerung.csv', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_bevoelkerung.csv'.")
