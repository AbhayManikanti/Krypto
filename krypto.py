import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def fetch_crypto_data(crypto_symbol, currency):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_symbol}/market_chart?vs_currency={currency}&days=30'
    response = requests.get(url)


    print(f"API Response: {response.text}")

    data = response.json()

    if 'prices' not in data:
        raise ValueError("The API response does not contain 'prices' data. Response keys: " + str(data.keys()))

    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df


def plot_crypto_data(df, crypto_symbol, currency):
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['price'], label=f'{crypto_symbol.capitalize()} Price in {currency.upper()}')
    plt.title(f'{crypto_symbol.capitalize()} Price Over the Last 30 Days')
    plt.xlabel('Date')
    plt.ylabel(f'Price ({currency.upper()})')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()


def update_plot():
    crypto_symbol = crypto_var.get().lower()
    currency = currency_var.get().lower()


    try:
        df = fetch_crypto_data(crypto_symbol, currency)
        plot_crypto_data(df, crypto_symbol, currency)


        for widget in plot_frame.winfo_children():
            widget.destroy()


        fig = plt.gcf()
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    except Exception as e:
        print(f"Error: {e}")

        for widget in plot_frame.winfo_children():
            widget.destroy()
        error_label = tk.Label(plot_frame, text=f"Error: {e}", fg="red")
        error_label.pack(padx=10, pady=10)

root = tk.Tk()
root.title("Cryptocurrency Tracker")

crypto_var = tk.StringVar(value='bitcoin')
crypto_label = ttk.Label(root, text="Select Cryptocurrency:")
crypto_label.pack(padx=10, pady=5)
crypto_dropdown = ttk.Combobox(root, textvariable=crypto_var, values=['bitcoin', 'ethereum', 'litecoin'])
crypto_dropdown.pack(padx=10, pady=5)

currency_var = tk.StringVar(value='usd')
currency_label = ttk.Label(root, text="Select Currency:")
currency_label.pack(padx=10, pady=5)
currency_dropdown = ttk.Combobox(root, textvariable=currency_var, values=['usd', 'eur', 'gbp'])
currency_dropdown.pack(padx=10, pady=5)

update_button = ttk.Button(root, text="Update Chart", command=update_plot)
update_button.pack(padx=10, pady=10)

plot_frame = ttk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True)

# Initial plot
update_plot()

root.mainloop()