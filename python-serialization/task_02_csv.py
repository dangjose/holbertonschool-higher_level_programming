#!/usr/bin/python3
"""Task 2. Converting CSV Data to JSON Format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    '''
        Convert csv data to json using serialization techniques.

        Args:
            csv_filename: Name of csv file to be converted.

        Returns:
            Boolean
    '''
    data = []
    try:
        with open(csv_filename, 'rb') as csv_f:
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        with open('data.json', 'wb') as json_f:
            json.dump(data, json_f)

        return True
    except Exception:
        return False
