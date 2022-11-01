import pandas as pd

def drop_duplicate(**kwargs):
    df_original = kwargs['df_original']
    col_name = kwargs['col_name']

    df_drop_duplicate = df_original.drop_duplicates([str(col_name)])
    df_custom = df_drop_duplicate[[str(col_name)]]

    return df_custom.reset_index(drop=True).dropna()