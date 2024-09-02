# Portfolio Optimizer 2.0

This project implements a stock portfolio optimization system using LSTM (Long Short-Term Memory) neural networks, sentiment analysis, and the Efficient Frontier algorithm. The system fetches historical stock data, predicts future returns using LSTM models, analyzes market sentiment, and then optimizes the portfolio allocation based on these inputs. Adds sentiment analysis to the output via Alpha Vantage.


## Project Structure

The project consists of several components:

1. `app.py`: The main Streamlit application for user interaction.
2. `controller.ipynb`: Orchestrates the execution of various components.
3. `Data_Retrieval.ipynb`: Handles the initial data collection process.
4. `LSTM_model.ipynb`: Contains the core logic for data preprocessing, LSTM modeling, and portfolio optimization.
5. `Sentiment.ipynb`: Performs sentiment analysis on the selected stocks.
6. `Visualizations.ipynb`: Generates visualizations of the results.

## Features

- User-friendly Streamlit interface for inputting stock symbols
- Data retrieval from Yahoo Finance API
- LSTM model implementation with hyperparameter tuning
- Sentiment analysis integration (optional)
- Portfolio optimization using the Efficient Frontier algorithm
- Visualizations of results

## Dependencies

- streamlit
- pandas
- numpy
- yfinance
- scikit-learn
- tensorflow
- keras
- keras-tuner
- PyPortfolioOpt
- Pillow (PIL)
- nbformat
- nbconvert

## Usage

1. Run the Streamlit app:
    
    Copy
    
    `streamlit run app.py`
    
2. Enter desired stock symbols (2-10) in the web interface.
3. Optionally, check the "Include Sentiment?" box for sentiment analysis.
4. Click "Optimize!" to run the portfolio optimization process.

## Key Components

### Streamlit App (`app.py`)

- Provides a user interface for entering stock symbols
- Manages the execution flow of the optimization process
- Displays results and visualizations

### Controller (`controller.ipynb`)

- Orchestrates the execution of various notebook components
- Conditionally runs sentiment analysis based on user preference

### Data Retrieval(`Data_Retrieval.ipynb`)

- Fetches historical stock data for specified symbols
- Saves cleaned data as pickle files for further processing

### LSTM Model(`LSTM_model.ipynb`)

- Implements an LSTM neural network for predicting stock returns
- Uses Bayesian Optimization for hyperparameter tuning
- Employs walk-forward validation for model evaluation
- Calculates annualized expected returns based on LSTM weekly returns predictions
- Calculates the optimized portfolio weights 
- Saves the annualized expected returns and weights as pickle files which are used in the visualization

### Sentiment Analysis(`Sentiment.ipynb`)

- Analyzes market sentiment for the selected stocks (optional)
- Limited to 25 API calls per day

### Portfolio Optimization/Visualizations(`Visualizations.ipynb`)

- Computes the covariance matrix using the Ledoit-Wolf shrinkage method
- Applies the Efficient Frontier algorithm to determine optimal portfolio weights
- Generates visual representations of the optimization results.
- Saves the visualization to to separate directory to display in the app as outputs

## Output

The system generates:

- Visualizations of the results (displayed in the Streamlit app):
	- Optimized portfolio weights
	- Expected annual return
	- Annual volatility
	- Sharpe Ratio of the optimized portfolio
	- Covarience matrix
	- Effecient Frontier plots
	- Sentiment analysis (optional)

## Notes

- The project uses fixed random seeds for reproducibility.
- The LSTM model architecture and hyperparameters are optimized using Keras Tuner.
- The portfolio optimization aims to maximize the Sharpe ratio.
- Sentiment analysis is optional and can be toggled by the user.

