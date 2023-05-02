import requests
import datetime
from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt

def denoise(symbol, days):
    date = datetime.date.today()
    url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/minute/{date - datetime.timedelta(days=days+2)}/{date}?adjusted=true&sort=asc&limit=120&apiKey=boxpAGWE_Xk0mYgLO4zX72bVQIJVSxwL'
    data = requests.get(url).json()['results']
    data = np.array([x['c'] for x in data])
    plt.plot(data)
    plt.title(f"{symbol} Price Data")
    plt.show()
    ft = fft(data)
    q = np.quantile(ft, 0.9)
    ft = ft[ft > q]
    data = ifft(ft)
    plt.plot(data)
    plt.title("Denoised Trend")
    plt.show()
