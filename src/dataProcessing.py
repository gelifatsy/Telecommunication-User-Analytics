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