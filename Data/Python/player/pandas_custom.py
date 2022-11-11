import pandas as pd

def drop_duplicate(**kwargs):
    df_original = kwargs['df_original']
    col_name_1 = kwargs['col_name_1']
    col_name_2 = kwargs['col_name_2']
    col_name_3 = kwargs['col_name_3']
    col_name_4 = kwargs['col_name_4']
    col_name_5 = kwargs['col_name_5']
    col_name_6 = kwargs['col_name_6']

    df_drop_duplicate = df_original.drop_duplicates([str(col_name_3)])
    df_custom = df_drop_duplicate[[str(col_name_1), str(col_name_2), str(col_name_3), str(col_name_4), str(col_name_5), str(col_name_6)]]

    return df_custom.reset_index(drop=True).dropna()