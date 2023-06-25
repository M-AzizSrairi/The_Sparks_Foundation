import yfinance as yf

# Define the ticker symbol, here it should be ^BSESN
ticker = "^BSESN"

# Download the historical stock price data
data = yf.download(ticker, start="1997-07-02", end="2023-06-04")

# Save the data to a CSV file
data.to_csv("historical_data.csv")

# Display the data
print(data)

