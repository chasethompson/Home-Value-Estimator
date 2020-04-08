import pandas as pd
from sklearn.preprocessing import StandardScaler, PowerTransformer, MinMaxScaler, RobustScaler, QuantileTransformer
from sklearn.model_selection import train_test_split
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols


def split_my_data(df, train_pct, seed=None):
    """
    Function will take df, train ratio and seed

    Then return train and test
    
    """
    train, test = train_test_split(df, train_size=train_pct, random_state=seed)
    return train, test