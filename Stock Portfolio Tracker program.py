import requests
import datetime

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}
        self.api_key = "YOUR_API_KEY"  # Replace with your financial API key
        self.base_url = "https://www.alphavantage.co/query"  # Using Alpha Vantage API

    def add_stock(self, symbol, shares, purchase_price):
        """
        Add a stock to the portfolio.
        :param symbol: Stock ticker symbol
        :param shares: Number of shares purchased
        :param purchase_price: Purchase price per share
        """
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
            self.portfolio[symbol]['purchase_price'] = purchase_price
        else:
            self.portfolio[symbol] = {
                'shares': shares,
                'purchase_price': purchase_price,
                'current_price': None,
                'last_updated': None
            }
        print(f"Added {shares} shares of {symbol} at ${purchase_price} per share.")

    def remove_stock(self, symbol):
        """
        Remove a stock from the portfolio.
        :param symbol: Stock ticker symbol
        """
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"Removed {symbol} from your portfolio.")
        else:
            print(f"Stock {symbol} not found in the portfolio.")

    def fetch_stock_price(self, symbol):
        """
        Fetch the latest stock price for a given symbol using Alpha Vantage API.
        :param symbol: Stock ticker symbol
        :return: Current stock price
        """
        try:
            params = {
                "function": "TIME_SERIES_INTRADAY",
                "symbol": symbol,
                "interval": "5min",
                "apikey": self.api_key
            }
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            # Extract the latest price
            time_series = data["Time Series (5min)"]
            latest_timestamp = list(time_series.keys())[0]
            current_price = float(time_series[latest_timestamp]["4. close"])

            # Update portfolio
            self.portfolio[symbol]['current_price'] = current_price
            self.portfolio[symbol]['last_updated'] = datetime.datetime.now()
            return current_price
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def view_portfolio(self):
        """
        Display the current portfolio, including real-time performance.
        """
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\n--- Stock Portfolio ---")
        total_investment = 0
        total_value = 0

        for symbol, data in self.portfolio.items():
            current_price = self.fetch_stock_price(symbol)
            if current_price:
                shares = data['shares']
                investment_value = shares * data['purchase_price']
                current_value = shares * current_price
                profit_loss = current_value - investment_value

                print(f"{symbol} - Shares: {shares} | Purchase Price: ${data['purchase_price']} | Current Price: ${current_price:.2f} | P/L: ${profit_loss:.2f}")
                total_investment += investment_value
                total_value += current_value
            else:
                print(f"{symbol} - Error fetching data")

        print("-----------------------")
        print(f"Total Investment: ${total_investment:.2f}")
        print(f"Current Portfolio Value: ${total_value:.2f}")
        print(f"Overall Profit/Loss: ${total_value - total_investment:.2f}\n")

if __name__ == "__main__":
    tracker = StockPortfolioTracker()
    
    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            price = float(input("Enter purchase price per share: "))
            tracker.add_stock(symbol, shares, price)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            tracker.remove_stock(symbol)
        elif choice == "3":
            tracker.view_portfolio()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
