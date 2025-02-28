# Model Definition and Evaluation


## Data Preparation and Preprocessing

The data preparation and preprocessing steps include loading various datasets, merging them, and performing feature engineering. The datasets include sales data, weather data, holiday data, and more. The preprocessing steps involve converting date columns to datetime format, filling missing values, and adding new features such as year, month, weekday, and cyclic features.

## Feature Engineering

Feature engineering is performed to create new features from the existing data. This includes extracting year, month, weekday, and other cyclic features from the date column. Additionally, features like weather code and holiday indicators are processed and added to the dataset.

## Data Splitting

The data is split into training, validation, and test sets based on the date. The training set includes data up to 2016, the validation set includes data from 2017, and the test set includes data from 2018 onwards.

## Data Transformation

A `ColumnTransformer` is defined to preprocess numerical and categorical features. Numerical features are imputed and scaled, while categorical features are one-hot encoded. The transformed data is then used for training and evaluation.

## Model Training

### Neural Network Model

A neural network model is defined using TensorFlow Keras. The model consists of multiple dense layers with ReLU activation, dropout layers for regularization, and a final linear layer for regression. The model is compiled with the Adam optimizer and mean squared error loss. The model is trained on the preprocessed training data and evaluated on the validation data.

### Hyperparameter Optimization

Hyperparameter optimization is performed using Optuna. The optimization process involves tuning the batch size, number of layers, number of units in each layer, activation functions, dropout rates, and learning rate. The best hyperparameters are selected based on the validation loss.

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