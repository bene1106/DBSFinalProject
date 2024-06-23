import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Einlesen der Hochschulendaten
hochschulen_df = pd.read_csv('hochschulen_cleaned.csv', delimiter=';', encoding='ISO-8859-1')

# Sicherstellen, dass die Spalte 'Anzahl Studierende' numerisch ist
hochschulen_df['Anzahl Studierende'] = pd.to_numeric(hochschulen_df['Anzahl Studierende'], errors='coerce')

# Entfernen von Zeilen mit fehlenden Werten in 'Anzahl Studierende'
hochschulen_df = hochschulen_df.dropna(subset=['Anzahl Studierende'])

# Balkendiagramm: Anzahl der Studierenden pro Hochschule
plt.figure(figsize=(12, 8))
sns.barplot(x='Anzahl Studierende', y='Hochschulkurzname', data=hochschulen_df, palette='viridis')
plt.xlabel('Anzahl der Studierenden')
plt.ylabel('Hochschule')
plt.title('Anzahl der Studierenden an verschiedenen Hochschulen')
plt.tight_layout()
plt.show()


# y-Achsenbeschriftungen schräg anzeigen lassen
plt.yticks(rotation=0, ha='right')
plt.tight_layout()
plt.show()