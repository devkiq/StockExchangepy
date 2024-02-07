import yfinance as yf
import matplotlib.pyplot as plt
import pyautogui as pygui
import pyperclip as pyclip
import webbrowser
import time

def get_stock_data(ticker):
    return yf.Ticker(ticker).history("6mo").Close

def plot_stock_chart(closing_prices, stock_symbol):
    closing_prices.plot()
    plt.title(f"Stock Closing Prices Chart for {stock_symbol}")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.savefig("stock_chart.png")
    #plt.show() Active when needed to see the chart

def calculate_statistics(closing_prices):
    max_price, min_price, current_price = (
        round(closing_prices.max(), 2),
        round(closing_prices.min(), 2),
        round(closing_prices.iloc[-1], 2)
    )
    return max_price, min_price, current_price

def open_gmail_and_create_email(recipient, subject, message):
    webbrowser.open('https://mail.google.com')
    time.sleep(4)

    # Click on compose email
    pygui.click(x=126, y=211)

    pygui.PAUSE = 2

    # Fill email fields
    fill_field(recipient)
    fill_field(subject)
    fill_field(message)

def fill_field(value):
    pyclip.copy(value)
    time.sleep(1) 
    pygui.hotkey("ctrl", "v")
    pygui.hotkey("tab")

def get_user_input():
    return input("Enter the stock symbol: ")

def run():
    stock_symbol = get_user_input()
    closing_prices = get_stock_data(stock_symbol)

    plot_stock_chart(closing_prices, stock_symbol)

    max_price, min_price, current_price = calculate_statistics(closing_prices)

    recipient = input("Digite o e-mail do destinatário: ")
    subject = f'Stock Analysis for {stock_symbol}'
    message = f"""Hello *** below are the requested analyses:

    STOCK {stock_symbol} WITH REFERENCE TO THE LAST 6 MONTHS

    Maximum Price: ${max_price}
    Minimum Price: ${min_price}
    Current Price: ${current_price}

    Feel free to contact for any questions.

    Regards,
    My name
    """

    open_gmail_and_create_email(recipient, subject, message)

if __name__ == "__main__":
    run()
