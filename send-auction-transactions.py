#!/usr/bin/env python

import csv
import uuid
import time
import argparse
from google_measurement_protocol import enhanced_item, enhanced_purchase, report
from prices import Money

def main():
    parser = argparse.ArgumentParser(description='Send ecommerce transactions to Google Analytics')
    parser.add_argument('--google-analytics-id', '-g', dest='google_analytics_id', default=None, help='Google Analytics ID')
    parser.add_argument('--input-file', '-i', type=argparse.FileType('r'))

    args = parser.parse_args()
    google_analytics_id = args.google_analytics_id
    input_file = args.input_file

    with input_file as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            client_id = row['userid']
            transaction_id = ''
            product_name = 'Auction Win'
            product_price = 0
            product_quantity = row['Transactions']
            raw_transaction_amount = row['Revenue']
            transaction_amount = raw_transaction_amount.replace('$', '')
            cd1 = 'purchase'
            url = row['Landing Page']

            print(f"client_id:{client_id} url: {url} transaction_id: {transaction_id} product: {product_name}: {product_price} quantity: {product_quantity} transaction amount: {transaction_amount} cd1: {cd1}")
            items = [
                enhanced_item(product_name, Money(product_price, 'USD'), quantity=product_quantity)]
            data = enhanced_purchase(transaction_id, items, Money(transaction_amount, 'USD'), url, cd1=cd1)
            report(google_analytics_id, client_id, data)
            time.sleep(0.1)

if __name__ == "__main__":
    main()
