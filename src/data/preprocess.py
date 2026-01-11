# preprocess.py
import pandas as pd
import numpy as np

def clean_data(df):
    """
    Cleans raw telecom customer data for churn modeling.
    
    - Converts TotalCharges to numeric
    - Fills missing values
    - Drops irrelevant columns
    """
    df = df.copy()
    
    # Drop customerID
    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)
    
    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    
    # Fill missing TotalCharges with 0
    df["TotalCharges"] = df["TotalCharges"].fillna(0)
    
    return df
