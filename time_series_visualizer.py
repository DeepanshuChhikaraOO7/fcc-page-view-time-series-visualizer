import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. Import data (Parse dates and set index)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Clean data (Filter out top 2.5% and bottom 2.5%)
lower_limit = df['value'].quantile(0.025)
upper_limit = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]

def draw_line_plot():
    # 3. Draw Line Plot
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    
    # Titles and Labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # 4. Copy and modify data for bar plot
    df_bar = df.copy()
    # Extract Year and Month Name
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # 5. Draw Bar Plot
    # We need to sort months correctly (Jan -> Dec), not alphabetically
    months_order = ["January", "February", "March", "April", "May", "June", 
                    "July", "August", "September", "October", "November", "December"]
    
    # Categorize and Sort
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months_order, ordered=True)
    
    # Group by Year and Month, calculate Mean
    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Plot
    fig = df_pivot.plot(kind='bar', figsize=(10, 8), legend=True).figure
    
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # 6. Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Sort months (Jan, Feb, Mar...) for the second plot
    months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months_order, ordered=True)

    # 7. Draw Box Plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    
    # Plot 1: Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    # Plot 2: Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
