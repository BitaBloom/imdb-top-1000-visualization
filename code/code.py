import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Define dataset path
dataset_path = "data/imdb_top_1000.csv"

# Load the dataset
df = pd.read_csv(dataset_path)

# Display the first few rows to understand the structure
print(df.head())

# Data Preprocessing
# Convert Released_Year to numeric and drop invalid rows
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df.dropna(subset=['Released_Year'], inplace=True)
df['Released_Year'] = df['Released_Year'].astype(int)

# Group data by year and genre, summing up votes
genre_popularity = df.groupby(['Released_Year', 'Genre'])['No_of_Votes'].sum().reset_index()

# Pivot the data for visualizations
genre_trends = genre_popularity.pivot(index='Released_Year', columns='Genre', values='No_of_Votes').fillna(0)

# Plot the stacked area chart
plt.figure(figsize=(15, 8))
genre_trends.plot(kind='area', stacked=True, alpha=0.7)
plt.title("Genre Popularity Over Time (Based on Votes)")
plt.xlabel("Year")
plt.ylabel("Total Votes")
plt.legend(title="Genre", loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig("reports/genre_popularity_over_time.png", dpi=300)
plt.show()

# Filter to show only the top 5 genres over time
top_genres = genre_popularity.groupby('Genre')['No_of_Votes'].sum().nlargest(5).index
genre_trends_top = genre_trends[top_genres]

# Plot line chart for the top genres
genre_trends_top.plot(figsize=(15, 8))
plt.title("Popularity of Top 5 Genres Over Time (Based on Votes)")
plt.xlabel("Year")
plt.ylabel("Total Votes")
plt.legend(title="Genre", loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig("reports/top_genres_trend.png", dpi=300)
plt.show()

# Pivot the data for the heatmap
heatmap_data = genre_trends_top.T

# Plot the heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap='Blues', annot=False, cbar=True)
plt.title("Popularity of Genres Over Time (Heatmap)")
plt.xlabel("Year")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("reports/genre_heatmap.png", dpi=300)
plt.show()

# Interactive line plot with Plotly
melted_data = genre_trends_top.reset_index().melt(id_vars='Released_Year', var_name='Genre', value_name='Votes')
fig = px.line(melted_data, x='Released_Year', y='Votes', color='Genre', title="Genre Popularity Over Time")
fig.write_html("reports/interactive_genre_trend.html")
fig.show()

# Drilldown: Top movies driving genre popularity spikes
top_years = genre_popularity.groupby('Genre').apply(lambda x: x.nlargest(1, 'No_of_Votes')).reset_index(drop=True)
drilldown_years = top_years['Released_Year'].unique()
drilldown_movies = df[df['Released_Year'].isin(drilldown_years)][['Series_Title', 'Released_Year', 'Genre', 'IMDB_Rating', 'No_of_Votes']]
drilldown_movies = drilldown_movies.sort_values(by='No_of_Votes', ascending=False)

# Plot bar chart for top movies
drilldown_top_movies = drilldown_movies.nlargest(10, 'No_of_Votes')
plt.figure(figsize=(12, 8))
sns.barplot(data=drilldown_top_movies, x='No_of_Votes', y='Series_Title', hue='Genre')
plt.title("Top Movies Driving Popularity in Key Years")
plt.xlabel("Number of Votes")
plt.ylabel("Movie Title")
plt.legend(title="Genre", loc="upper right")
plt.tight_layout()
plt.savefig("reports/top_movies_popularity.png", dpi=300)
plt.show()

# Print current working directory
print("Current working directory:", os.getcwd())
