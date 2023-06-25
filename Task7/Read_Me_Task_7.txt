Stock Market Prediction using Numerical and Textual Analysis.

In this task I worked first on the sentimental analysis of the indian news headline in which I classified each text as natural, negative or positive based on the sentiment label score.
For the stock price dataset, I used yfinance library to get it from yahoo finance and then performed time series analysis to conclude the model type and extract its orders and features and then I combined the pricing and sentimental analysis and fed the data to a ANN and then to a LSTM neural network which yielded better MSE.


Tools : 
Python
Libraries : 
- yfinance
- pandas
- numpy
- nltk
- sklearn
- scipy
- Matplotlib
- statsmodels
- pmdarima
- tensorflow