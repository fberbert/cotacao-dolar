#!/usr/bin/env python3
"""
Author: Fábio Berbert de Paula <fberbert@gmail.com>
Repository: https://github.com/fberbert/cotacao-dolar
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def fetch_exchange_rate():
    # URL of the page with the exchange rate
    url = 'https://wise.com/br/currency-converter/dolar-hoje'

    # ChromeDriver configuration
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (no graphical interface)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)

        # Wait for the element containing the exchange rate to be present
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='text-success']"))
        )

        # Extract the exchange rate value
        exchange_rate = driver.find_element(By.XPATH, "//span[@class='text-success']").text
        return exchange_rate

    except Exception as e:
        print("Error finding the exchange rate:", e)
    finally:
        # Close the browser
        driver.quit()

# Fetch the exchange rate and print it
exchange_rate_value = fetch_exchange_rate()
if exchange_rate_value:
    print('R$ ' + exchange_rate_value)
else:
    print("Exchange rate not found or unexpected format.")

