-- Importieren der Daten in die Tabelle Region
COPY Region(Region, Weiblich, Maennlich)
FROM 'D:\\FU\DBS\\FinalProject\\cleaned_bevoelkerung.csv'
DELIMITER ';'
CSV HEADER;

-- Importieren der Daten in die Tabelle Ort
COPY Ort(Region, Ort)
FROM 'D:\\FU\\DBS\\FinalProject\\ort.csv'
DELIMITER ','
CSV HEADER;

-- Importieren der Daten in die Tabelle HOCHSCHULE
COPY HOCHSCHULE(Hochschulname, Trägerschaft, Anzahl_Studierende, Ort)
FROM 'D:\\FU\\DBS\\FinalProject\\cleaned_hochschulen.csv'
DELIMITER ';'
CSV HEADER;
