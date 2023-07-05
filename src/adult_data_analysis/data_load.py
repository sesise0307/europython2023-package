import pandas as pd


def load_data(data_file="../data/adult_data.csv"):
    COLUMN_NAMES = (
        "age",
        "workclass",
        "fnlwgt",
        "education",
        "education_num",
        "marital_status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital_gain",
        "capital_loss",
        "hours_per_week",
        "native_country",
        "income",
    )

    return pd.read_csv(data_file, names=COLUMN_NAMES, skipinitialspace=True)
