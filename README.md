# Airbnb-data-analysis

Introduction

The Airbnb Analysis project focuses on analyzing Airbnb data from the travel industry and property management domain. By leveraging MongoDB Atlas and various data analysis and visualization tools, we aim to extract valuable insights into pricing dynamics, availability patterns, and location-based trends in Airbnb listings.

Table of Contents

1.	Key Technologies
2.	Installation
3.	Usage
4.	Workflow

Key Technologies • Python scripting • MongoDB • Streamlit • Power BI • Pandas • Numpy • Plotly

Installation

To run this project, you will need to install the following packages
    pip install streamlit
    pip install numpy
    pip install plotly
    pip install pandas
    pip install pymongo
    And the installation of power bi on the system

Usage

To use this project, kindly follow the following steps:

    1.	Clone the repository: git clone https://github.com/Theressac/Airbnb-data-analysis
    2.	Install the required packages
    3.	Run the Streamlit app: streamlit run app.py
    4.	Access the app in your browser at http://localhost:8501

Workflow

•	MongoDB Connection and Data Retrieval

We established a connection to MongoDB Atlas and retrieved the Airbnb dataset. MongoDB queries and data retrieval operations were performed to extract the necessary information for analysis.

•	Data Cleaning and Preparation

The dataset underwent a comprehensive data cleaning and preparation process. This involved handling missing values, removing duplicates, and converting data types for accurate analysis. The dataset was made ready for exploratory data analysis and visualization tasks.

•	Geospatial Visualization using Streamlit

We developed a Streamlit web application that utilizes geospatial data from the Airbnb dataset. Interactive maps were created to visualize the distribution of Airbnb listings across different locations, allowing users to explore prices, ratings, and other relevant factors.

•	Price Analysis and Visualization

Using the cleaned data, we conducted a thorough analysis of how prices vary across different locations, property types, and seasons. Dynamic plots and charts were created to enable users to explore price trends, outliers, and correlations with other variables.

•	Availability Analysis by Season

We analyzed the availability of Airbnb listings based on seasonal variations. Occupancy rates, booking patterns, and demand fluctuations throughout the year were visualized using line charts, heatmaps, or other suitable visualizations.

•	Location-Based Insights

We investigated how the price of listings varies across different locations. MongoDB queries and data aggregation techniques were used to extract relevant information for specific regions or neighborhoods. These insights were visualized on interactive maps or created dashboards in tools like 
Tableau or Power BI.

•	Interactive Visualizations

Dynamic and interactive visualizations were developed to allow users to filter and drill down into the data based on their preferences. Users could interact with the visualizations to explore specific regions, property types, or time periods of interest.

•	Dashboard Creation using Tableau or Power BI

A comprehensive dashboard was built using Tableau or Power BI, combining various visualizations to present key insights from the analysis. This dashboard provided a holistic view of the Airbnb dataset and its patterns.

Author

@Theressac

