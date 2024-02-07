import yfinance as yf
import matplotlib.pyplot as plt
import pyautogui as pygui
import pyperclip as pyclip
import webbrowser
import time


def get_stock_data(ticker):
    return yf.Ticker(ticker).history("3mo").Close

def plot_stick_chart(closing_prices, stock_symbol):
    closing_prices.plot()
    plt.title(f"Stock Closing Prices Chart for {stock_symbol}")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.savefig("sotck_chart.png")
    #plt.show() Active when necessary

def calculate_statistics(closing_prices):
    max, min, current = (round(closing_prices.max(), 2),  round(closing_prices.min(), 2), round(closing_prices.iloc[-1], 2))
    return max, min, current









def user_input():
    return input("Digite o símbolo da ação: ")

