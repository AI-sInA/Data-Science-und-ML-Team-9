# Data Preparation

## Overview

This data preparation step involves pre-processing and modeling sales data in conjunction with weather data, seasonal information, and other relevant factors. The code performs several steps, including data preparation, feature engineering, and transformation, to prepare the data for machine learning.

## Data Sources

The following datasets are used in this project:
- `umsatzdaten_gekuerzt.csv`: Basic sales data.
- `wetter.csv`: Weather data containing temperature, cloud cover, wind speed, and other weather information.
- `kiwo.csv`: Data on Kieler Woche.
- `Feier_Bruecke_Ferien_bis2018.csv`: Public holidays, bridging days, and school holidays.
- `VPI.csv`: Consumer price index data.
- `EPI.csv`: Producer price index data.
- `Heimspiel_Holstein_Kiel_finle.csv`: Data on the home matches of Holstein Kiel.
- `Kieler_Umschlag_finale.csv`: Data on the Kieler Umschlag festival.
- `Schulferien_Litauen_finale.csv`: School holidays in Lithuania.

## Data Preprocessing

The data preprocessing steps include:
1. Loading CSV files using `pandas.read_csv()` and merging them based on the date column.
2. Converting the date column to datetime format to extract time-based features.
3. Handling missing values:
   - For numeric features, missing values are replaced by the mean value.
   - The `KielerWoche` column is filled with `False` and treated as a Boolean value.

## Feature Engineering

New features are created to capture temporal patterns and event-specific information:
- Year, month, weekday, calendar week, and day in year.
- Cyclical features such as `day_in_year_sin`, `day_in_year_cos`, `month_sin`, `month_cos`, `weekday_sin`, and `weekday_cos`.

## Model Preparation

Columns for numerical and categorical features are prepared:
- Numerical features: Weather data, public holidays, price indices, and regional variables.
- Categorical features: Day of the week, weather code, and product group, which are encoded using a `OneHotEncoder`.

A `ColumnTransformer` is used to combine different preprocessing steps:
- Numerical features are imputed using the mean value and then scaled.
- Categorical features are converted into dummy variables using a `OneHotEncoder`.

## Usage

To run the project:
1. Ensure that the CSV files are available and specify the correct path to the files in the code.
2. Execute the script to load and preprocess the data.

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn

Install the required packages using:
```bash
pip install pandas numpy scikit-learn