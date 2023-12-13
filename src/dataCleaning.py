import pandas as pd

def test_data_types(df):
    """
    Test the data type of each column in the DataFrame.
    :param df: DataFrame
    :return: Dictionary with column names as keys and data types as values
    """
    data_types = df.dtypes.to_dict()
    return data_types

def clean_data_based_on_types(df, drop_threshold=0.9, fill_method='mean', constant_value='constant_value'):
    """
    Clean the DataFrame based on data types.
    :param df: DataFrame
    :param drop_threshold: Threshold for droppsing columns with missing values (default: 0.9)
    :param fill_method: Method for filling missing values ('mean', 'median', 'constant', etc.)
    :param constant_value: Constant value for filling missing values in non-numeric columns
    :return: DataFrame with missing values handled
    """
    # Drop columns with missing values exceeding the threshold
    df_dropped = df.dropna(axis=1, thresh=int(df.shape[0] * (1 - drop_threshold)))

    # Identify numeric columns for mean or median calculation
    numeric_columns = df_dropped.select_dtypes(include='number').columns

    # Identify non-numeric columns for constant filling
    non_numeric_columns = df_dropped.columns.difference(numeric_columns)

    # Fill missing values based on data types
    for col, dtype in test_data_types(df_dropped).items():
        if pd.api.types.is_numeric_dtype(dtype):
            if fill_method == 'mean':
                df_dropped[col] = df_dropped[col].fillna(df_dropped[col].mean())
            elif fill_method == 'median':
                df_dropped[col] = df_dropped[col].fillna(df_dropped[col].median())
        else:
            df_dropped[col] = df_dropped[col].fillna(constant_value)

    return df_dropped
