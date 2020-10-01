The purpose of this project is to develop a web crawler to extract the data from the CoinSpot crypto currency trading platform.

The URL is https://www.coinspot.com.au/tradecoins which has a table with the prices of multiple crypto currencies.

We prefer Python programming language. You are free to choose either Python 2.7 version or 3.x version. 

Note that the above URL contains Javascript which is used to render the HTML table. Therefore, if you just download the HTML page source of above URL, it would not be containing the table and the data.

You can use a library to render the Javascript and then extract the data in the HTML table.

For each crypto currency listed in the above URL, we need to get the following attributes.

1. Coin Code name
2. Coin name
3. Buying rate
4. Selling rate
5. Market Cap
6. Volume (24 hours)
7. Change Rate (24 hours)

You can basically print each extracted row data on screen at the initial phase.