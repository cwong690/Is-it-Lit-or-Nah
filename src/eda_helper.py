#!/usr/bin/env python3

import numpy as np
import pandas as pd

def get_null_percentage(df:pd.DataFrame, column:str) -> float:
    return round(1 - sum(pd.notnull(df[column]))/len(df[column]), 2)