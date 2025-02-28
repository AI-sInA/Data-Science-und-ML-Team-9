# Dataset Characteristics

## Overview

This project involves analyzing and evaluating various datasets to understand their characteristics and relationships. The datasets include information on sales, weather, holidays, consumer price index, producer price index, and local events. The analysis aims to preprocess the data, merge different datasets, and visualize key insights.

## Data Sources

The following datasets are used in this project:
- **Sales Data**: Contains sales information.
- **Weather Data**: Includes weather conditions such as temperature, cloud cover, and wind speed.
- **Holiday Data**: Information on holidays, bridge days, and school vacations.
- **Consumer Price Index (CPI)**: Data on consumer prices for various goods.
- **Producer Price Index (PPI)**: Data on producer prices for various goods.
- **Local Events**: Information on local events such as Kieler Woche and home games of Holstein Kiel.

## Data Preprocessing

The data preprocessing steps include:
1. Converting date columns to datetime format.
2. Handling missing values.
3. Merging datasets on the date column.
4. Converting categorical variables to appropriate data types.

## Feature Engineering

New features are created to capture temporal patterns and event-specific information:
- Extracting date-related features such as year, month, day of the week, and day of the year.
- Creating cyclical features for month and day of the year.
- Encoding categorical variables using one-hot encoding.

## Data Analysis & Visualization

The analysis includes:
- Displaying basic information and summary statistics of the dataset.
- Visualizing the distribution of the target variable (sales).
- Calculating the correlation of sales with other features.
- Plotting relationships between sales and key features.
