# Dataset Characteristics

0. Datenanalyse (Betreff Datei: team9_dataset_eval.ipynb)






1. BETRACHTUNG DER BUNDESLÄNDER UND FERIEN (Betreff Datei: Ferien_D_Variable.ipynb)

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


2. BETRACHTUNG der HEIMSPIELTAGE VON HOLSTEIN KIEL UND TAGEN OHNE SPIELE (Betreff Ordner: "Data Analysis")

Umsatzanalyse in Abhängigkeit von Heimspieltag oder normalem Tag
Beschreibung

In diesem Abschnitt wird der Einfluss von Heimspielen und normalen tagen auf den Umsatz untersucht. Die Analyse basiert auf täglichen Umsatzdaten, die mit Informationen zu Heimspieldaten ergänzt werden. Ziel der Analyse ist es, die Umsatzunterschiede während Heimspieltagen im Vergleich zu Tagen ohne Heimspiel zu identifizieren und statistisch zu validieren.

Daten
Die folgenden Datendateien werden im Projekt verwendet:

    Umsatzdaten (umsatzdaten_gekuerzt.csv): Infos siehe 1.
            
    Heimspieldaten (Heimspiel_Holstein_Kiel_finle.csv):
        Enthält spezifische Daten zu Heimspielen.

    Ergebnisse:
        Das Endergebnis ist eine zusammengeführte und aggregierte Übersicht der Umsätze, die auf Basis der Heimspiele untersucht wird.

Codeübersicht

siehe 1., adaptiert auf Umsatz und Heimspiele

Berechnungen

Die wichtigsten Berechnungen umfassen:

    Heimspielumsatz: Der durchschnittliche Umsatz während eines Heimspieltags.
    Umsatz kein Heimspiel: Der durchschnittliche Umsatz während eines normalen Tags ohne Heimspiel.

Für jeden dieser Umsätze werden die folgenden Kennzahlen berechnet:

    Mittelwert, Standardabweichung

Zusätzlich werden Konfidenzintervalle für den Mittelwert berechnet, um die Unsicherheit in den Ergebnissen zu quantifizieren.
Visualisierungen

    Balkendiagramme mit durchschnittlichem Umsatz bei Heimspiel und normalen Tagen inkl. 95% Konfidenzintervall

    t-Tests und Tukey HSD-Test

Ergebnisse:

-Durchschnittlicher Umsatz

Das Skript berechnet den durchschnittlichen Umsatz an Heimspieltagen und an normalen Tagen. Hier ist ein Beispiel für die Ausgabe:

Durchschnittlicher Umsatz an Heimspieltagen: 233.55 EUR
Durchschnittlicher Umsatz an normalen Tagen: 205.37 EUR

Dies zeigt, dass der durchschnittliche Umsatz an Heimspieltagen höher ist als an normalen Tagen.

-T-Test (Welch's T-Test)

Der T-Test überprüft, ob der Unterschied zwischen den Umsätzen an Heimspieltagen und normalen Tagen statistisch signifikant ist. Hier ist ein Beispiel für die Ausgabe des T-Tests:

T-Test: t=3.70, p=0.0002
Der Unterschied ist signifikant (p < 0.05).

Der p-Wert (0.0002) ist kleiner als das Signifikanzniveau (α = 0.05), was darauf hinweist, dass der Unterschied im Umsatz zwischen Heimspieltagen und normalen Tagen statistisch signifikant ist.

-ANOVA-Ergebnisse

Die ANOVA wird verwendet, um festzustellen, ob es signifikante Unterschiede im Umsatz zwischen verschiedenen Warengruppen gibt. Hier ist ein Beispiel für die Ausgabe der ANOVA:

ANOVA: Signifikant (p = 0.0043)

Der p-Wert (0.0043) ist kleiner als 0.05, was darauf hinweist, dass es signifikante Unterschiede im Umsatz zwischen den Warengruppen gibt.

-Tukey-HSD-Test (Paarweise Vergleiche)

Der Tukey HSD-Test führt paarweise Vergleiche durch, um zu ermitteln, zwischen welchen Warengruppen signifikante Unterschiede bestehen. Hier sind Beispielergebnisse aus dem Tukey HSD-Test:

Tukey-HSD-Ergebnisse:
   Multiple Comparison of Means - Tukey HSD, FWER=0.05   
=========================================================
group1 group2  meandiff p-adj    lower     upper   reject
---------------------------------------------------------
     1      2  280.3554    0.0  272.2095  288.5013   True
     1      3   41.1984    0.0   33.0525   49.3443   True
     1      4  -34.1885    0.0  -42.3952  -25.9817   True
     1      5   154.653    0.0  146.5071  162.7989   True
     1      6  -55.2259    0.0  -70.7132  -39.7386   True
     2      3  -239.157    0.0 -247.3029 -231.0111   True
     2      4 -314.5439    0.0 -322.7506 -306.3371   True
     2      5 -125.7024    0.0 -133.8483 -117.5565   True
     2      6 -335.5813    0.0 -351.0686  -320.094   True
     3      4  -75.3869    0.0  -83.5936  -67.1801   True
     3      5  113.4546    0.0  105.3087  121.6005   True
     3      6  -96.4243    0.0 -111.9116   -80.937   True
     4      5  188.8415    0.0  180.6347  197.0482   True
     4      6  -21.0374 0.0016  -36.5568    -5.518   True
     5      6 -209.8789    0.0 -225.3662 -194.3916   True
---------------------------------------------------------

Der Tukey HSD-Test zeigt, dass es signifikante Unterschiede zwischen den Warengruppen gibt, was durch das reject-Label in der Spalte reject angezeigt wird.

5. Visualisierung der Ergebnisse

Das Skript erzeugt Balkendiagramme zur Darstellung der Ergebnisse:

    Balkendiagramm für den Umsatzvergleich an Heimspieltagen und normalen Tagen mit Konfidenzintervallen und Signifikanzmarkierungen.
    Balkendiagramm für den Vergleich des Umsatzes zwischen verschiedenen Warengruppen an Heimspieltagen und normalen Tagen, ebenfalls mit Konfidenzintervallen und Signifikanzmarkierungen.

Die Signifikanz wird durch ein Sternchen (*) über den Balken angezeigt, wenn der p-Wert des T-Tests unter 0.05 liegt.




    


