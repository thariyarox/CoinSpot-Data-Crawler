# CoinSpot Data Crawler

The purpose of this project is to extract the data from the CoinSpot crypto currency trading platform.

The URL is https://www.coinspot.com.au/tradecoins which has a table with the prices of multiple crypto currencies.

## Install

Create a virtual environment, activate it and then install the requirements.

```sh
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Run

To execute, you can do it in two ways. Using `runspider` or `crawler`.

```sh
(venv) $ scrapy runspider crawler/spiders/coinspot.py
(venv) $ scrapy crawl coinspot
```

You can save scraped items in a file. Add `-o FILE` to the command line. These formats are supported (check scrapy docs):

- JSON
- JSON lines
- CSV
- XML

For example, to generate the CSV file you can run the following command -

```sh
(venv) $ scrapy crawl coinspot -o test_data.csv
```

## Scraped Items

- `code_name`: Coin Code name
- `name`: Coin name
- `buy`: Buying rate
- `sell`: Selling rate
- `market_cap`: Market Cap
- `volume`: Volume (24 hours)
- `change`: Change Rate (24 hours)
