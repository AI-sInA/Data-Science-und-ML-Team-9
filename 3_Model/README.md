# Model Definition and Evaluation

## Overview

This project involves defining and evaluating machine learning models for sales prediction. The steps include data preparation, feature engineering, model training, hyperparameter optimization, and model evaluation.

## Data Preparation and Preprocessing

The data preparation and preprocessing steps include:
1. Loading various datasets such as sales data, weather data, holiday data, and more.
2. Merging the datasets.
3. Performing feature engineering by converting date columns to datetime format, filling missing values, and adding new features such as year, month, weekday, and cyclic features.

## Feature Engineering

New features are created to capture temporal patterns and event-specific information:
- Extracting year, month, weekday, and other cyclic features from the date column.
- Processing features like weather code and holiday indicators.

## Data Splitting

The data is split into training, validation, and test sets based on the date:
- Training set: Data up to 2016.
- Validation set: Data from 2017.
- Test set: Data from 2018 onwards.

## Data Transformation

A `ColumnTransformer` is defined to preprocess numerical and categorical features:
- Numerical features are imputed and scaled.
- Categorical features are one-hot encoded.

## Model Training

### Neural Network Model

A neural network model is defined using TensorFlow Keras. The model consists of:
- Multiple dense layers with ReLU activation.
- Dropout layers for regularization.
- A final linear layer for regression.

The model is compiled with the Adam optimizer and mean squared error loss. It is trained on the preprocessed training data and evaluated on the validation data.

### Hyperparameter Optimization

Hyperparameter optimization is performed using Optuna. The optimization process involves tuning:
- Batch size
- Number of layers
- Number of units in each layer
- Activation functions
- Dropout rates
- Learning rate

The best hyperparameters are selected based on the validation loss.

### Optimized Models

Two optimized models are defined based on the best hyperparameters found during the optimization process. These models are trained and evaluated on the preprocessed data.

## Model Evaluation

The models are evaluated using R² and adjusted R² metrics on the test data. Additionally, the Mean Absolute Percentage Error (MAPE) is calculated for each model and for each product group.

## Loss Function Visualization

The training and validation loss for each model is plotted to visualize the training process and identify any overfitting or underfitting issues.

## Submission

The final model is used to make predictions on the submission dataset. The predictions are saved to a CSV file for submission.

## Code Structure

The code is structured into several functions and sections for data loading, preprocessing, feature engineering, model training, hyperparameter optimization, and evaluation. This modular approach ensures that the code is organized and easy to understand.

## Conclusion

The notebook demonstrates a complete workflow for building and evaluating machine learning models for sales prediction. The use of feature engineering, data preprocessing, neural networks, and hyperparameter optimization ensures that the models are well-tuned and provide accurate predictions.