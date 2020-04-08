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
        propertylandusetypeid as SFR_property_type,
        fips
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
    zillow['bathrooms'] = zillow['bathrooms'].astype(int)
    zillow['bedrooms'] = zillow['bedrooms'].astype(int)
    zillow['sqft'] = zillow['sqft'].astype(int)
    zillow['zip'] = zillow['zip'].astype(int)
    zillow['home_value'] = zillow['home_value'].astype(int)
    zillow['SFR_property_code'] = zillow['SFR_property_code'].astype(int)
    zillow['fips'] = zillow['fips'].astype(int)
    return df

