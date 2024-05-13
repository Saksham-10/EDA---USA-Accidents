# EDA---USA-Accidents
US Accidents Exploratory Data Analysis (EDA)
In this project, I conducted a comprehensive Exploratory Data Analysis (EDA) on a public dataset of US traffic accidents obtained from Kaggle. This README summarizes the key findings and insights gained from the analysis.

Data Description

The dataset provided a wealth of information on accidents across various US cities, including:

Location: City name
Timing: Start time of the accident
Geospatial Data: Start latitude and longitude for accident location
Weather Conditions (if available): Details like temperature, precipitation, etc.
Additional Information: Other relevant details pertaining to the accident
Content of the Repository

US_accidents_EDA.ipynb: This Jupyter notebook is the heart of the project. It houses the entire EDA workflow, including data cleaning, exploration, and visualization.
Running the Analysis

To replicate this analysis, you'll need the following:

Libraries: Ensure you have libraries like Pandas, seaborn, and folium installed in your development environment.
Kaggle API Key (Optional): If the data requires download from Kaggle, you'll need a Kaggle API key. Instructions for obtaining a key are beyond the scope of this README.
Jupyter Notebook Execution: Open the US_accidents_EDA.ipynb notebook in your Jupyter Notebook environment and execute the code cells sequentially.
Key Findings and Insights

My analysis revealed several interesting patterns and trends in US traffic accidents:

Temporal Distribution: Accidents are more frequent during mornings (6 AM to 10 AM) and evenings (3 PM to 6 PM). Weekends exhibit a different distribution compared to weekdays.
Weather and Accidents: While initial exploration suggests a possible link between weather and accidents, further investigation is necessary to establish a definitive relationship.
Data Quality: Potential data quality issues were identified with the Bing data source. This necessitates a closer examination to ensure data integrity.
City-wise Accident Distribution: The number of accidents exhibits an exponential decrease across cities. A significant portion of cities report less than 1000 accidents annually. Over 1200 cities even report only one accident, which warrants further investigation.
Further Exploration Opportunities

This EDA lays a solid foundation for deeper analysis. Here are some potential areas for further exploration:

City-Specific Analysis: Conduct a more granular analysis of cities with high accident rates to identify contributing factors specific to those locations.
Weather Impact Analysis: Delve deeper into the relationship between weather conditions and accidents to understand potential correlations.
Data Cleaning and Quality Enhancement: Investigate and address any data quality issues discovered during the initial exploration.
Feature Engineering: Craft new features from existing data to gain richer insights.
Predictive Modeling (Optional): If your goal extends beyond understanding patterns, you could develop models to predict potential accidents based on various factors like time, weather, and location.
Summary and Conclusion

This EDA provides valuable insights into the patterns and trends of US traffic accidents. It highlights potential correlations between accident frequency and factors like time of day, weather conditions, and data quality. The findings serve as a springboard for further investigation and potentially the development of predictive models to help mitigate traffic accidents.

Ask & Answer Questions

While this summary provides a general overview, the Jupyter notebook offers a deeper dive into the data. Here are some questions you might be able to answer through further exploration:

Are there more accidents in warmer or colder areas? (Requires weather data analysis)
Which 5 states have the highest number of accidents? How about per capita? (Requires state information and population data)
Does New York show up in the data? If yes, why is the count lower if this the most populated city. (The analysis confirms New York data is missing)
Among the top 100 cities in number of accidents, which states do they belong to most frequently? (Requires city location and state information)
Data Exploration Questions (May require further analysis in the notebook):

Which days of the week have the most accidents?
Which months have the most accidents?
What is the trend of accidents year over year (decreasing/increasing?)
When is accidents per unit of traffic the highest? (Requires data on traffic volume)
