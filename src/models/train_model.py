# train_model.py
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

def train_logistic(X_train, y_train, preprocessor):
    """
    Trains a baseline Logistic Regression model with preprocessing.
    """
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(max_iter=1000))
    ])
    pipeline.fit(X_train, y_train)
    return pipeline

def train_rf(X_train, y_train, preprocessor, n_estimators=300, max_depth=12, random_state=42):
    """
    Trains a Random Forest model with preprocessing.
    """
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=random_state
        ))
    ])
    pipeline.fit(X_train, y_train)
    return pipeline
