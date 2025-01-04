import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# CSV-Datei laden
df = pd.read_csv(r'C:\Users\Jojo\Downloads\merged_umsatz_heimspiel.csv')

# Konvertiere das Datum in datetime
df['Datum'] = pd.to_datetime(df['Datum'])

# Berechne den Mittelwert und die Standardabweichung für Heimspieltage (Heimspiel Holstein Kiel == 1)
home_game_sales = df[df['Heimspiel Holstein Kiel'] == 1]['Umsatz']
mean_home_game = home_game_sales.mean()
std_home_game = home_game_sales.std()
n_home_game = home_game_sales.count()

# Berechne den Standardfehler
std_error_home_game = std_home_game / np.sqrt(n_home_game)

# Berechne das 95%-Konfidenzintervall für Heimspieltage
confidence_level = 0.95
z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)  # Z-Wert für 95% Konfidenzintervall

# Konfidenzintervall berechnen
confidence_interval_home_game = (mean_home_game - z_score * std_error_home_game,
                                 mean_home_game + z_score * std_error_home_game)

# Berechne den Mittelwert und die Standardabweichung für normale Tage (kein Heimspiel, Heimspiel Holstein Kiel == 0)
normal_day_sales = df[df['Heimspiel Holstein Kiel'] == 0]['Umsatz']
mean_normal_day = normal_day_sales.mean()
std_normal_day = normal_day_sales.std()
n_normal_day = normal_day_sales.count()

# Berechne den Standardfehler für normale Tage
std_error_normal_day = std_normal_day / np.sqrt(n_normal_day)

# Berechne das 95%-Konfidenzintervall für normale Tage
confidence_interval_normal_day = (mean_normal_day - z_score * std_error_normal_day,
                                  mean_normal_day + z_score * std_error_normal_day)

# Ergebnisse ausgeben
print(f"Durchschnittlicher Umsatz an Heimspieltagen: {mean_home_game:.2f} EUR")
print(f"95%-Konfidenzintervall für den Umsatz an Heimspieltagen: ({confidence_interval_home_game[0]:.2f}, {confidence_interval_home_game[1]:.2f}) EUR")

print(f"Durchschnittlicher Umsatz an normalen Tagen: {mean_normal_day:.2f} EUR")
print(f"95%-Konfidenzintervall für den Umsatz an normalen Tagen: ({confidence_interval_normal_day[0]:.2f}, {confidence_interval_normal_day[1]:.2f}) EUR")

# Plotten
labels = ['Heimspiel', 'Normaler Tag']
means = [mean_home_game, mean_normal_day]
conf_intervals = [(confidence_interval_home_game[0], confidence_interval_home_game[1]),
                  (confidence_interval_normal_day[0], confidence_interval_normal_day[1])]

# Erstelle das Balkendiagramm
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(labels, means, yerr=[(means[0] - confidence_interval_home_game[0]), 
                                   (confidence_interval_normal_day[1] - means[1])], 
              capsize=5, color=['skyblue', 'lightgreen'])

# Konfidenzintervalle als Fehlerbalken hinzufügen
for bar, conf_int in zip(bars, conf_intervals):
    ax.errorbar(bar.get_x() + bar.get_width() / 2, bar.get_height(), 
                yerr=[[bar.get_height() - conf_int[0]], [conf_int[1] - bar.get_height()]], 
                fmt='none', color='black', capsize=5)

# Titel und Labels hinzufügen
ax.set_title('Durchschnittlicher Umsatz an Heimspieltagen vs. normalen Tagen mit Konfidenzintervall')
ax.set_ylabel('Durchschnittlicher Umsatz (EUR)')

# Zeige das Diagramm
plt.tight_layout()
plt.show()
