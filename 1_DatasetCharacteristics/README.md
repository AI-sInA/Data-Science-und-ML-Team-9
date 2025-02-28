# Dataset Characteristics

















BETRACHTUNG DER BUNDESLÄNDER UND FERIEN (Betreff Datei: Ferien_D_Variable.ipynb)

Umsatzanalyse in Abhängigkeit der Ferien pro Bundesland
Beschreibung

In diesem Abschnitt wird der Einfluss von Ferien und Schultagen auf den Umsatz in verschiedenen deutschen Bundesländern untersucht. Die Analyse basiert auf täglichen Umsatzdaten, die mit Informationen über Feiertage, Brückentage und Schulferien kombiniert werden. Ziel der Analyse ist es, die Umsatzunterschiede während Ferienzeiten im Vergleich zu den regulären Schultagen zu identifizieren und statistisch zu validieren.
Daten

Die folgenden Datendateien werden im Projekt verwendet:

    Umsatzdaten (umsatzdaten_gekuerzt.csv):
        Enthält täglich erfasste Umsätze zusammen mit zusätzlichen Informationen zu Feiertagen, Brückentagen und Schulferien in verschiedenen Bundesländern.
        Wichtige Spalten:
            Datum: Das Datum des Umsatzes.
            Warengruppe: Kategorie des Produkts.
            Umsatz: Der Umsatz an diesem Tag.
            Feiertag/Brückentag/Bundesländer: Kennzahlen, ob der Tag ein Feiertag oder Brückentag ist, sowie Ferieninformationen für jedes Bundesland (z.B. BW, BY, etc.).

    Feiertagsdaten (Feier_Bruecke_Ferien_bis2018.csv):
        Enthält spezifische Daten zu Feiertagen, Brückentagen und Schulferien in jedem Bundesland.

    Ergebnisse:
        Das Endergebnis ist eine zusammengeführte und aggregierte Übersicht der Umsätze, die auf Basis der Ferien- und Schulzeiten der einzelnen Bundesländer untersucht wird.

Codeübersicht

    Daten einlesen und zusammenführen:
        Beide CSV-Dateien werden eingelesen und anhand der gemeinsamen Datum-Spalte zusammengeführt.

    Datenaggregation:
        Die Umsätze werden nach Datum aggregiert.
        Für jedes Bundesland werden die Feiertags- und Brückentags-Kennzahlen zusammengefasst, sodass die Umsatzdaten für jedes Bundesland und Datum zusammengeführt werden.

    Berechnungen:
        Mittelwert und Standardabweichung: Der durchschnittliche Umsatz sowie die Standardabweichung werden für jedes Bundesland sowohl während der Ferien als auch während der Schulzeit berechnet.
        Konfidenzintervalle: 95%-Konfidenzintervalle für den Umsatz werden für jedes Bundesland in Ferien- und Schulzeiten berechnet.
        t-Tests: Für jede Warengruppe wird ein t-Test durchgeführt, um festzustellen, ob es einen signifikanten Unterschied im Umsatz zwischen den Ferien- und Schulzeiten gibt.

    Ergebnisse ausgeben:
        Die berechneten Mittelwerte, Standardabweichungen und p-Werte werden für jedes Bundesland und jede Warengruppe ausgegeben.

    Speichern der aggregierten Daten:
        Die aggregierten und berechneten Daten werden in einer neuen CSV-Datei gespeichert, um eine spätere Analyse oder Visualisierung zu ermöglichen.

Berechnungen

Die wichtigsten Berechnungen umfassen:

    Ferienumsatz: Der durchschnittliche Umsatz während der Ferien eines Bundeslands.
    Schulumsatz: Der durchschnittliche Umsatz während der Schulzeit (außerhalb der Ferien) eines Bundeslands.

Für jedes dieser Zeiträume werden die folgenden Kennzahlen berechnet:

    Mittelwert: Der durchschnittliche Umsatz während Ferien und Schule.
    Standardabweichung: Die Streuung des Umsatzes während der beiden Zeiträume.
    Anzahl der Tage: Die Anzahl der Tage, an denen Umsatzdaten vorliegen.

Zusätzlich werden Konfidenzintervalle für den Mittelwert berechnet, um die Unsicherheit in den Ergebnissen zu quantifizieren.
Visualisierungen

    Balkendiagramme:
        Es werden Balkendiagramme erstellt, die den durchschnittlichen Umsatz für Ferien und Schule für jedes Bundesland darstellen. Balken für die Ferienzeit werden in blauer Farbe und die für die Schulzeit in roter Farbe angezeigt.
        Fehlerbalken: Diese visualisieren das 95%-Konfidenzintervall des Umsatzes und zeigen die Unsicherheit der Mittelwertberechnungen.
        Signifikanzsterne: Ein Stern (*) wird über den Balken angezeigt, wenn der Unterschied zwischen Ferien- und Schulumsatz statistisch signifikant ist (p < 0,05).

    t-Tests:
        Ein t-Test wird für jede Warengruppe durchgeführt, um zu prüfen, ob der Umsatz während der Ferien signifikant höher oder niedriger ist als während der Schulzeit.
        Die p-Werte dieser Tests werden im Diagramm angezeigt und geben Aufschluss darüber, ob die Unterschiede in den Umsätzen zufällig oder signifikant sind.

Beispiel einer Ausgabe:

Die Ergebnisse können für jedes Bundesland wie folgt aussehen:
Für Nordrhein-Westfalen (NW):

    Ferienumsatz: Durchschnittlicher Umsatz während der Ferienzeit.
    Schulumsatz: Durchschnittlicher Umsatz während der Schulzeit.
    p-Wert: Wenn der p-Wert unter 0,05 liegt, ist der Unterschied statistisch signifikant.

Beispiel der berechneten Werte:

    Durchschnittlicher Umsatz Ferien (NW): 140 EUR
    Durchschnittlicher Umsatz Schule (NW): 120 EUR
    p-Wert: 0.03 (signifikant, da p < 0,05)

Anforderungen

Für die Ausführung des Projekts werden folgende Python-Pakete benötigt:

    Pandas: Für die Datenmanipulation und Aggregation.
    Matplotlib: Für die Visualisierung der Ergebnisse.
    Scipy: Für statistische Tests und Berechnungen der Konfidenzintervalle.



