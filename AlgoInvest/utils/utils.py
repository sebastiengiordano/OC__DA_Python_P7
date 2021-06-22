import os
import pandas as pd

import csv

def csv_to_list(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        return list(reader)


def csv_to_DataFrame(file_path=None, delimiter=','):
# def csv_to_DataFrame(file_path=None, delimiter=r'\s*,\s*'):
    if not file_path:
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        file_path = os.path.join(fileDir, "../test_wxPython/models/Log.csv")
    return pd.read_csv(file_path, sep=delimiter, header=None)
