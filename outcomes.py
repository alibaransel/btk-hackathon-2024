import pandas as pd


def list_of_outcomes():
    df = pd.read_csv("c1u1.csv")

    df.fillna(value=0, inplace=True)

    list_of_outcomes_dict = []

    for i in range(len(df["outcome"])):
        outcomes_dict = {"outcome": df["outcome"][i], "description": df["description"][i]}
        list_of_outcomes_dict.append(outcomes_dict)

    return list_of_outcomes_dict
