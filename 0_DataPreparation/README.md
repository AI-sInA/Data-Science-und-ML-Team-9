# Data Preparation

Diese Data Preparation dient der Vorverarbeitung und Modellierung von Umsatzdaten in Verbindung mit Wetterdaten, saisonalen Informationen und anderen relevanten Faktoren. Der Code führt mehrere Schritte durch, einschließlich Datenvorbereitung, Feature Engineering und Transformation, und bereitet die Daten für maschinelles Lernen vor.

Voraussetzungen

    Python 3.x
    Pandas
    NumPy
    Scikit-learn

Datenquelle

Der Code verarbeitet mehrere CSV-Dateien, die unterschiedliche Datensätze enthalten:

    umsatzdaten_gekuerzt.csv: Basisdatensatz mit den Umsatzdaten.
    wetter.csv: Wetterdaten, die Temperatur, Bewölkung, Windgeschwindigkeit und weitere Wetterinformationen enthalten.
    kiwo.csv: Daten zur Kieler Woche.
    Feier_Bruecke_Ferien_bis2018.csv: Feiertage, Brückentage und Schulferien.
    VPI.csv: Verbraucherpreisindex-Daten.
    EPI.csv: Erzeugerpreisindex-Daten.
    Heimspiel_Holstein_Kiel_finle.csv: Daten zu den Heimspielen von Holstein Kiel.
    Kieler_Umschlag_finale.csv: Daten zum Fest „Kieler Umschlag“.
    Schulferien_Litauen_finale.csv: Schulferien in Litauen.

Code-Erklärung
Datenvorverarbeitung

    Die CSV-Dateien werden mit pandas.read_csv() geladen und mit merge() auf Grundlage der Datum-Spalte zusammengeführt.
    Die Spalte Datum wird in das datetime-Format konvertiert, um Zeitbasierte Features zu extrahieren.
    Fehlende Werte werden in verschiedenen Spalten behandelt:
        Für numerische Features werden die fehlenden Werte durch den Mittelwert ersetzt.
        Die KielerWoche-Spalte wird mit False gefüllt und als boolescher Wert behandelt.

Feature Engineering

    Mehrere zeitbasierte Features werden durch die add_features()-Funktion erzeugt:
        Jahr (Jahr), Monat (Monat), Wochentag (Wochentag), Kalenderwoche (Kalenderwoche), Tag im Jahr (Tag_im_Jahr).
        Zyklische Merkmale wie Tag_im_Jahr_sin, Tag_im_Jahr_cos, Monat_sin, Monat_cos, Wochentag_sin, Wochentag_cos werden hinzugefügt, um saisonale Muster besser erfassen zu können.

Modellvorbereitung

    Spalten für numerische Features: Hier werden eine Vielzahl von Features wie Wetterdaten, Feiertage, Preisindizes und regionale Variablen berücksichtigt.
    Spalten für kategorische Features: Dazu gehören Wochentag, Wettercode und Warengruppe, die mit einem OneHotEncoder kodiert werden.
    Spaltenumwandlung mit ColumnTransformer: Der ColumnTransformer wird verwendet, um verschiedene Vorverarbeitungsschritte für numerische und kategorische Features zu kombinieren:
        Numerische Features: Werden imputationstechnisch mit dem Mittelwert und anschließend skaliert.
        Kategorische Features: Werden mit einem OneHotEncoder in Dummy-Variablen umgewandelt.

Verwendung

    Daten einlesen und vorverarbeiten: Stellen Sie sicher, dass die CSV-Dateien vorhanden sind und den richtigen Pfad zu den Dateien im Code angeben. Führen Sie dann das Skript aus, um die Daten zu laden und vorzuverarbeiten.
