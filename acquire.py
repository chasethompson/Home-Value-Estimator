import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
from env import host, user, password

# function to contact database

def get_db_url(db_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

# function to query db and return df

def wrangle_zillow():
    url = get_db_url('zillow')
    query = """
    SELECT
        bathroomcnt as bathrooms,
        bedroomcnt as bedrooms,
        calculatedfinishedsquarefeet as sqft,
        regionidzip as zip,
        taxvaluedollarcnt as home_value,
        taxamount as taxes,
        propertylandusetypeid as SFR,
        fips,
        latitude,
        longitude
    FROM
        predictions_2017
    JOIN
        properties_2017 USING(id)
    WHERE
        (transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-30')
        AND bathroomcnt > 0
        AND bedroomcnt > 0
        AND calculatedfinishedsquarefeet > 0
        AND taxvaluedollarcnt > 0
        AND taxamount > 0
        AND propertylandusetypeid = '261'
        AND fips > 0
    ORDER BY fips;
    """
    zillow = pd.read_sql(query,url)
    return zillow

def clean_zillow_data(df):
    df = df.dropna()
    df['bathrooms'] = df['bathrooms'].astype(int)
    df['bedrooms'] = df['bedrooms'].astype(int)
    df['sqft'] = df['sqft'].astype(int)
    df['zip'] = df['zip'].astype(int)
    df['home_value'] = df['home_value'].astype(int)
    df['SFR_property_code'] = df['SFR_property_code'].astype(int)
    df['fips'] = df['fips'].astype(int)
    return df

