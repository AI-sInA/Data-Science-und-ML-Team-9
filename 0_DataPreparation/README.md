## Data Preparation

This data preparation is used to pre-process and model sales data in conjunction with weather data, seasonal information and other relevant factors. The code performs several steps, including data preparation, feature engineering and transformation, and prepares the data for machine learning.
Voraussetzungen

    Python 3.x
    Pandas
    NumPy
    Scikit-learn

## Data sources

The code processes several CSV files that contain different data records:

    umsatzdaten_gekuerzt.csv: Basic data set with sales data.
    wetter.csv: Weather data containing temperature, cloud cover, wind speed and other weather information.
    kiwo.csv: Data on Kieler Woche.
    Feier_Bruecke_Ferien_bis2018.csv: Public holidays, bridging days and school holidays.
    VPI.csv: Consumer price index data.
    EPI.csv: Producer price index data.
    Heimspiel_Holstein_Kiel_finle.csv: Data on the home matches of Holstein Kiel.
    Kieler_Umschlag_finale.csv: Data on the ‘Kieler Umschlag’ festival.
    Schulferien_Litauen_finale.csv: School holidays in Lithuania.

## Code Description

    The CSV files are loaded with pandas.read_csv() and merged with merge() based on the date column.
    The date column is converted to datetime format to extract time-based features.
    Missing values are handled in different columns:
        For numeric features, the missing values are replaced by the mean value.
        The KielerWoche column is filled with False and treated as a Boolean value.


## Feature Engineering

    Several time-based features are created by the add_features() function:
        Year (Jahr), Month (Monat), Weekday (Wochentag), Calendar Week (Kalenderwoche), Day in Year (Tag_im_Jahr).
        Cyclical features such as day_in_year_sin, day_in_year_cos, month_sin, month_cos, weekday_sin, weekday_cos are added to better capture seasonal patterns.


## Model preparation

    Columns for numerical features: A variety of features such as weather data, public holidays, price indices and regional variables are taken into account here.
    Columns for categorical features: These include day of the week, weather code and product group, which are coded with a OneHotEncoder.
    Column conversion with ColumnTransformer: The ColumnTransformer is used to combine different pre-processing steps for numerical and categorical features:
        Numerical features: Are imputed using the mean value and then scaled.
        Categorical features: Are converted into dummy variables using a OneHotEncoder.


## Usage

    Read in and pre-process data: Make sure that the CSV files are available and specify the correct path to the files in the code. Then execute the script to load and pre-process the data.

