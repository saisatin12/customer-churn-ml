# build_features.py
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def engineer_features(df, target="Churn", test_size=0.2, random_state=42):
    """
    Splits data into train/test and applies one-hot encoding & scaling.
    Returns: X_train, X_test, y_train, y_test, preprocessor object
    """
    # Separate features and target
    X = df.drop(target, axis=1)
    y = df[target]
    
    # Identify categorical and numerical columns
    cat_cols = X.select_dtypes(include="object").columns.tolist()
    num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    
    # Preprocessor
    preprocessor = ColumnTransformer([
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), cat_cols)
    ])
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state
    )
    
    return X_train, X_test, y_train, y_test, preprocessor, num_cols, cat_cols
