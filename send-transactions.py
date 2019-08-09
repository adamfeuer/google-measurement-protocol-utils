#!/usr/bin/env python

import csv
import uuid
import time
import argparse
from google_measurement_protocol import enhanced_item, enhanced_purchase, report
from prices import Money

#GOOGLE_ANALYTICS_ID = 'UA-13014811-1'

def main():
    parser = argparse.ArgumentParser(description='Send ecommerce transactions to Google Analytics')
    parser.add_argument('--google-analytics-id', '-G', dest='google_analytics_id', default=None, help='Google Analytics ID')
    parser.add_argument('--input-file', '-i', type=argparse.FileType('r'))

    args = parser.parse_args()
    google_analytics_id = args.google_analytics_id
    input_file = args.input_file

    with input_file as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            client_id = row['client_id']
            transaction_id = row['transaction_id']
            product_name = row['product_name']
            product_price = row['product_price']
            product_quantity = row['product_quantity']
            transaction_amount = row['transaction_amount']

            print(f"client_id:{client_id} transaction_id: {transaction_id} product: {product_name}: {product_price} quantity: {product_quantity} transaction amount: {transaction_amount}")
            items = [
                enhanced_item(product_name, Money(product_price, 'USD'), quantity=product_quantity)]
            data = enhanced_purchase(transaction_id, items, Money(transaction_amount, 'USD'), '/cart/')
            report(google_analytics_id, client_id, data)
            time.sleep(0.1)

if __name__ == "__main__":
    main()
