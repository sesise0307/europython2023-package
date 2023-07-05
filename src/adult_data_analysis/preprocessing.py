import pandas as pd


def add_age_group(adult_df):
    age_group = pd.cut(
        adult_df["age"],
        bins=range(10, 101, 10),
        right=False,
        labels=[f"{age_start}~{age_start + 9}" for age_start in range(10, 100, 10)],
    )

    return adult_df.assign(age_group=age_group)


def change_education_type_to_category(adult_df):
    education_order = (
        adult_df.groupby("education")["education_num"].unique().sort_values().index
    )

    return adult_df.astype(
        {
            "education": pd.CategoricalDtype(categories=education_order, ordered=True),
            "education_num": pd.CategoricalDtype(ordered=True),
        }
    )
