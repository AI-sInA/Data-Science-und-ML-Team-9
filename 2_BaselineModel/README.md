# Baseline Model

## Overview

This project aims to build a baseline model for predicting sales (`Umsatz`) using various features such as weather data, holiday information, and economic indices. The model is implemented using Python and several machine learning libraries.

## Data Sources

The following datasets are used in this project:
- `umsatzdaten_gekuerzt.csv`: Sales data
- `wetter.csv`: Weather data
- `kiwo.csv`: Kieler Woche event data
- `Feier_Bruecke_Ferien_bis2018.csv`: Holidays, bridge days, and vacation data
- `VPI.csv`: Consumer price index data
- `EPI.csv`: Producer price index data
- `Heimspiel_Holstein_Kiel_finle.csv`: Home games of Holstein Kiel
- `Kieler_Umschlag_finale.csv`: Kieler Umschlag event data
- `Schulferien_Litauen_finale.csv`: School holidays in Lithuania

## Data Preprocessing

The data preprocessing steps include:
1. Converting date columns to datetime format.
2. Adding new features such as year, month, weekday, and cyclic features (sine and cosine transformations).
3. Handling missing values and categorical variables.

## Feature Engineering

New features are created to capture temporal patterns and event-specific information:
- Year, month, weekday, and calendar week.
- Day of the year (sine and cosine transformations).
- Month (sine and cosine transformations).
- Weekday (sine and cosine transformations).
- Boolean flag for weekends.

## Model Training

Two models are trained and evaluated:
1. **Linear Regression**: A simple linear model to establish a baseline.
2. **RandomForestRegressor**: An ensemble model to capture non-linear relationships.

## Evaluation

The models are evaluated using R² and adjusted R² scores on the test set. The RandomForestRegressor outperforms the Linear Regression model.

## Visualization

Scatter plots and residual plots are generated to compare the actual vs. predicted values and to analyze the residuals for both models.

## Submission

The trained RandomForestRegressor model is used to predict sales on a submission dataset, and the results are saved in `team9_baseline_submission.csv`.

## Usage

To run the project, execute the Jupyter notebook `team9_baseline.ipynb` which contains all the steps from data loading to model evaluation and submission preparation.

## Requirements

- Python 3.11
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib

Install the required packages using:
```bash
pip install pandas numpy scikit-learn seaborn matplotlib