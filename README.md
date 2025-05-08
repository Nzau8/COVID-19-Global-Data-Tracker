# COVID-19 Data Analysis Project

## Project Description
This project analyzes COVID-19 data from multiple countries, focusing on key metrics such as total cases, deaths, vaccination rates, and death rates. The analysis provides visual insights into how different countries have been affected by and responded to the COVID-19 pandemic.

## Objectives
- Analyze COVID-19 trends across selected countries (Kenya, Algeria, China, India, and South Africa)
- Visualize key COVID-19 metrics over time
- Compare vaccination progress between countries
- Calculate and display death rates
- Generate summary statistics for each country

## Tools and Libraries Used
- Python 3.x
- pandas: For data manipulation and analysis
- matplotlib: For creating static visualizations
- seaborn: For enhanced statistical visualizations
- plotly: For interactive visualizations
- Jupyter Notebook (optional): For interactive development

## How to Run the Project
1. Ensure you have Python installed on your system
2. Install the required packages:
   ```bash
   pip install pandas matplotlib seaborn plotly
   ```
3. Download the dataset:
   - The project uses the 'owid-covid-data.csv' file from Our World in Data
   - Place the CSV file in the same directory as the Python script
4. Run the script:
   ```bash
   python data_analysis.py
   ```

## Project Outputs
The script generates six different visualizations:
1. Total COVID-19 cases over time
2. Total COVID-19 deaths over time
3. Daily new cases over time
4. Death rate over time
5. Cumulative vaccinations over time
6. Vaccinated population percentage by country

Additionally, it provides summary statistics for each country including total cases, total deaths, and death rates.



## Data Source
The data is sourced from Our World in Data's COVID-19 dataset, which provides comprehensive and up-to-date information about the pandemic across different countries. 