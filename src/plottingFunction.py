import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    plt.figure(figsize=(8, 5))
    plt.hist(df[column].dropna(), bins=30, color='lightblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


# Scatter Plot of Total Data Usage(DL + UL) for Each Application
def scatter_plot_total_data(df, app):
        sns.scatterplot(x=df[app + ' DL (Bytes)'] + df[app + ' UL (Bytes)'], y=df['Total UL (Bytes)'] + df['Total DL (Bytes)'], label=app)
        plt.title('Scatter Plot of Total Data Usage(DL + UL) for Each Application')
        plt.xlabel('Total Data Usage (DL+UL) for Each App')
        plt.ylabel('Total Data Usage (DL+UL)')
        plt.legend()
        plt.show()
       
def scatter_plot_UL_vs_DL(df, applications):
    plt.figure(figsize=(14, 10))
    for app in applications:
        sns.scatterplot(x=df[app + ' DL (Bytes)'], y=df[app + ' UL (Bytes)'], label=app)
    plt.title('Scatter Plot of DL vs. UL Data for Each Application')
    plt.xlabel('DL Data Usage')
    plt.ylabel('UL Data Usage')
    plt.legend()
    plt.show()