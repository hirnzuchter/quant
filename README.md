# Fourier Transform Price Trend Tool
Dependencies: SciPy, Matplotlib, Requests, Numpy, nltk, tweepy, pandas, yfinance, cleanco

## Current Features
- Fourier Transform Tool
- Asset Rebalance Tool
    - Momentum Investing Strategy
    - Sentiment Analysis Strategy
    - Risk Allocation Strategy
    - Expected Return Strategy

### Current Features Notes
The application does not make trades; it only provides the user with information and suggests management directions given the user's tracked assets.
Due the the 5 call per minute limit of the free tier of the AlphaVantage API, loading may take artificially long.

## Future Features
- Backtesting Tool
- Forecasting Tool
    - Monte Carlo Simulation
- Asset Rebalance Tool
    - Sentimental Analysis Strategy
        - Data Update Feature
 
### Future Features Notes
For Forecasting Tool, I plan to add a Monte Carlo simulation. Every time the sentimental analysis tool is run, 
have it check if the time the data was last updated was more than 60 minutes ago, and if this is true,
update the data.
