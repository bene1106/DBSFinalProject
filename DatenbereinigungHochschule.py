#   Datenbereinigung:

# rausnehmen:
# - Homepage (Brauchen wir nicht für unsere Abfragen und hilft uns nicht auf einen anderen Datensatz zuzugreifen)
# - Hochschulkurzname (Wir haben den ganzen Hochschulnamen schon)
# - Hochschultyp (Brauchen wir nicht für unsere Abfragen und hilft uns nicht auf einen anderen Datensatz zuzugreifen)
# - Gründungsjahr (Brauchen wir nicht für unsere Abfragen und auch nicht um auf den anderen Datensatz zuzugreifen)
# - Habilitationsrecht (Brauchen wir nicht für unsere Abfragen und auch nicht um auf den anderen Datensatz zuzugreifen)
# - Promotionsrecht (Brauchen wir nicht für unsere Abfragen und hilft uns nicht auf einen anderen Datensatz zuzugreife
# - Staße

import pandas as pa

# Datei laden
file_path = 'D:\FU\DBS\FinalProject\hochschulen.csv'
df_hochschulen = pa.read_csv(file_path, encoding='latin1')

# Zu entfernende spalten (als array für schnelleren zugriff):
columns_to_remove = [
    'Homepage', 
    'Hochschulkurzname', 
    'Hochschultyp', 
    'Gründungsjahr', 
    'Habilitationsrecht', 
    'Promotionsrecht', 
    'Straße',
    'Bundesland'
]

# Entfernen der Spalten
df_cleaned = df_hochschulen.drop(columns=columns_to_remove)

# in neue CSV-Datei speichern
cleaned_file_path = 'D:\FU\DBS\FinalProject\cleaned_hochschulen.csv'
df_cleaned.to_csv(cleaned_file_path, index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_hochschulen.csv'.")
