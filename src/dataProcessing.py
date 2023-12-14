import pandas as pd

def convert_to_datetime(df):
    df['Start'] = pd.to_datetime(df['Start'])
    df['End'] = pd.to_datetime(df['End'])
    return df

def calculate_session_duration(df):
    df['Session Duration (s)'] = (df['End'] - df['Start']).dt.total_seconds()
    return df

def aggregate_per_user(df, all_app):
    user_aggregated = df.groupby('MSISDN/Number').agg({
        'Bearer Id': 'count',
        'Session Duration (s)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum',
        **{f'{app} DL (Bytes)': 'sum' for app in all_app},
        **{f'{app} UL (Bytes)': 'sum' for app in all_app}
    })

    for app in all_app:
        user_aggregated[f'{app} (Total Bytes)'] = user_aggregated[f'{app} DL (Bytes)'] + user_aggregated[f'{app} UL (Bytes)']

    user_aggregated.drop([f'{app} DL (Bytes)' for app in all_app] + [f'{app} UL (Bytes)' for app in all_app], axis=1, inplace=True)

    user_aggregated.rename(columns={'Bearer Id': 'Number of xDR sessions', 'Total DL (Bytes)': 'Total Download (Bytes)', 'Total UL (Bytes)': 'Total Upload (Bytes)'}, inplace=True)

    return user_aggregated

import pandas as pd

def calculate_all_metrics(data):
    quantitative_columns = data.select_dtypes(include=['number']).columns

    metrics_data = pd.DataFrame(index=quantitative_columns, columns=[
        'Range', 'Variance', 'Standard Deviation', 'IQR',
        'Coefficient of Variation', 'Mean Absolute Deviation',
        'Range (P10 to P90)', 'Z-Score Range'
    ])

    for column in quantitative_columns:
        column_data = data[column].dropna() 

        data_range = column_data.max() - column_data.min()
        data_variance = column_data.var()
        data_std_dev = column_data.std()
        data_iqr = column_data.quantile(0.75) - column_data.quantile(0.25)

        # Calculate additional metrics
        coefficient_of_variation = (column_data.std() / column_data.mean()) * 100
        mean_absolute_deviation = column_data.mad()

        p10 = column_data.quantile(0.10)
        p90 = column_data.quantile(0.90)
        range_p10_p90 = p90 - p10

        z_scores = (column_data - column_data.mean()) / column_data.std()
        z_score_range = z_scores.max() - z_scores.min()

        # Store values in the DataFrame
        metrics_data.loc[column] = [
            data_range, data_variance, data_std_dev, data_iqr,
            coefficient_of_variation, mean_absolute_deviation,
            range_p10_p90, z_score_range
        ]

    return metrics_data

import pandas as pd
