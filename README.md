# Cryptocurrency Tracker
## Overview
The Cryptocurrency Tracker is a Python-based application that allows users to visualize cryptocurrency price trends over the past 30 days. The application uses the CoinGecko API to fetch real-time cryptocurrency data and displays it in a graphical format using matplotlib and tkinter for the GUI.

## Features
Select cryptocurrency from a predefined list.
Choose currency for price conversion (USD, EUR, GBP).
View historical price data over the past 30 days.
Interactive graphical user interface (GUI).
Prerequisites
Python 3.6 or higher
requests library
pandas library
matplotlib library
tkinter library (usually included with Python)
## Installation
### Clone the Repository
~~~
git clone https://github.com/yourusername/cryptocurrency-tracker.git
cd cryptocurrency-tracker
~~~
### Install Dependencies

~~~
pip install requests pandas matplotlib
~~~
## Usage
### Run the Application

~~~
python main.py
~~~


## Interact with the GUI

Select Cryptocurrency: Choose from Bitcoin, Ethereum, or Litecoin from the dropdown menu.
Select Currency: Choose between USD, EUR, or GBP.
Update Chart: Click the "Update Chart" button to fetch the latest data and refresh the plot.
## Viewing the Plot
![image](https://github.com/user-attachments/assets/38c5475a-6cb4-4c2b-a7a5-2ce223fafbc4)

The plot will display the selected cryptocurrency's price trends over the last 30 days in the chosen currency.
## Troubleshooting
API Response Issues: Check the console for API response details if the data is not displaying correctly. Ensure your internet connection is active and stable.
Data Accuracy: Verify that the selected cryptocurrency and currency are supported by the CoinGecko API. Check the API documentation for any changes.
## Example Usage
### 1. Running the App
Open a terminal and run the Python script.
### 2. Selecting Options
Use the dropdown menus to select the cryptocurrency and currency.
### 3. Updating the Chart
Click the "Update Chart" button to load the data and view the plot.
## Known Issues
The application might not handle cases where the CoinGecko API response format changes. Ensure to check for updates or changes in the API.
## Future Enhancements
Add more cryptocurrencies to the selection list.
Include additional features such as notifications for price changes.
Improve error handling and provide user-friendly error messages.
