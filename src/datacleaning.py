import pandas as pd

from dataloading import Data

obj = Data()
df = obj.loader(r'artifacts\Train.csv')

class Cleaner:
    def __init__(self):
        pass

    def clean(df = df):
        print(df.shape)

