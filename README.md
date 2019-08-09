# google-measurement-protocol-utils

Utilities for sending offline ecommerce measurements to Google Analytics. This might be useful
if you want to tie offline transactions to website traffic tracked by Google Analytics.

Right now there is one script `send-measurements.py` that sends offline ecommerce transactions from a CSV file to Google Analytics via the 
[Google Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/v1/).

# Installation

1. `pip install pyenv`
1. `pyenv install python 3.6.5`
1. `pip install pipenv`
1. `pipenv shell` 

You'll also need a Google Analytics ID for your web property, it will look something like `UA-XXXXXXXX-Y` 
where X and Y are decimal digits. Get it from your Google Analytics console under Settings.

# Usage

`./send-transactions.py --google-analytics-id <GOOGLE_ANALYTICS_ID> --input-file transactions.csv`

See the file `transactions.csv` file format, it should have a header row and the following fields:

`client_id,transaction_id,product_name,product_price,product_quantity,transaction_amount`


# Credits

This uses the great [google-measurement-protocol](https://github.com/mirumee/google-measurement-protocol) library.


# License

MIT.

# Author

I hope you find this useful.

cheers  
adam  
Adam Feuer  
Seattle, WA, USA  


