import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    plt.figure(figsize=(8, 5))
    plt.hist(df[column].dropna(), bins=30, color='lightblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()



def scatter_plot(cleaned_data, applications):
    cleaned_data['Total Data (DL+UL)'] = cleaned_data['Total UL (Bytes)'] + cleaned_data['Total DL (Bytes)']

    plt.figure(figsize=(14, 10))
    
    for app in applications:
        sns.scatterplot(x=cleaned_data[app + ' DL (Bytes)'], y=cleaned_data[app + ' UL (Bytes)'], label=app)

    plt.xlabel('DL Data (Bytes)')
    plt.ylabel('UL Data (Bytes)')
    plt.title('Scatter Plot of DL vs. UL Data for Each Application')
    plt.legend()
    plt.show()