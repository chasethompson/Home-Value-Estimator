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

def iqr_robust_scaler(train, test):
    """
    Scales features using stats that are robust to outliers by removing the median and scaling data to the IQR.

    When calling the function rename the variables to maintain original:
    X_train_iqr_robust_scaled, X_test_iqr_robust_scaled = iqr_robust_scaler(X_train, X_test)

    """ 
    scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled