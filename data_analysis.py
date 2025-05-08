import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
try:
    df = pd.read_csv('owid-covid-data.csv')
    print("Dataset loaded successfully")
except FileNotFoundError:
    print("File not found. Please make sure the file exists in the project folder")

# Clean dataset
df.dropna(subset=['date', 'location'], inplace=True)
df['date'] = pd.to_datetime(df['date'])

# Filter countries
countries_of_interest = ['Kenya', 'Algeria', 'China', 'India', 'South Africa']
df = df[df['location'].isin(countries_of_interest)]

# Fill missing numeric data
df[['total_cases', 'total_deaths', 'new_cases', 'people_vaccinated', 'people_vaccinated_per_hundred']] = \
    df[['total_cases', 'total_deaths', 'new_cases', 'people_vaccinated', 'people_vaccinated_per_hundred']].fillna(0)

# Plot 1: Total cases over time
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='total_cases', hue='location')
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Total deaths over time
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='total_deaths', hue='location')
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Daily new cases over time
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='new_cases', hue='location')
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 4: Death rate over time
df['death_rate'] = df['total_deaths'] / df['total_cases']
df['death_rate'] = df['death_rate'].fillna(0)

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='death_rate', hue='location')
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 5: Vaccination progress
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='people_vaccinated', hue='location')
plt.title('Cumulative Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('People Vaccinated')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 6: % Vaccinated (Bar chart - latest data)
latest = df.sort_values('date').groupby('location').tail(1)
plt.figure(figsize=(10,6))
sns.barplot(data=latest, x='location', y='people_vaccinated_per_hundred')
plt.title('Vaccinated Population (%) by Country')
plt.ylabel('Percent Vaccinated')
plt.xlabel('Country')
plt.tight_layout()
plt.show()

# Summary statistics with death rate
summary = latest[['location', 'total_cases', 'total_deaths']]
summary['death_rate'] = summary['total_deaths'] / summary['total_cases']
print("\nSummary Statistics:")
print(summary.set_index('location'))
