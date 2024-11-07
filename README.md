# cotacao-dolar
Dollar Exchange Rate in Python

This Python script retrieves and prints the current dollar exchange rate using Selenium. You can easily adapt it to your application by copying the `fetch_exchange_rate()` function.

## Dependencies:

To use this script, make sure to install the required dependencies:

```bash
$ pip install selenium webdriver-manager
```

## Exchange Rate Source:
*Wise Currency Converter*: [https://wise.com/br/currency-converter/dolar-hoje](https://wise.com/br/currency-converter/dolar-hoje)

## How it Works
The script opens the URL for the exchange rate, waits for the page to load, and retrieves the value using Selenium. It’s configured to run in headless mode for a seamless experience without opening a browser window.

For more details, refer to the comments in the code.

## Usage
To use this script, simply run it with Python:

```bash
$ python3 cotacao-dolar.py
```

The output will display the current dollar exchange rate in BRL.

## Notes
- **Execution Time**: Due to page loading and interaction through Selenium, this script might take a few seconds to complete.
- **Adaptability**: This code can be adapted to fetch other currency rates by changing the source URL and adjusting the element selectors.
  
If you have any questions or suggestions, please refer to the comments in the code or contact the author.

---
**Author**: Fábio Berbert de Paula <fberbert@gmail.com>  
**Repository**: [https://github.com/fberbert/cotacao-dolar](https://github.com/fberbert/cotacao-dolar)
