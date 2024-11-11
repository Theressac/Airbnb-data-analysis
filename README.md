# Airbnb-data-analysis

## Introduction

The Airbnb Analysis project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations and location-based trends

## Table of Contents

1.	Key Technologies
2.	Installation
3.	Usage
4.	Workflow

## Key Technologies 

• Python scripting 
• MongoDB 
• Streamlit 
• Power BI 
• Pandas 
• Numpy 
• Plotly

## Installation

To run this project, you will need to install the following packages
    pip install streamlit
    pip install numpy
    pip install plotly
    pip install pandas
    pip install pymongo
    And the installation of power bi on the system

## Usage

To use this project, kindly follow the following steps:

    1.	Clone the repository: git clone https://github.com/Theressac/Airbnb-data-analysis
    2.	Install the required packages
    3.	Run the Streamlit app: streamlit run app.py
    4.	Access the app in your browser at http://localhost:8501

## Workflow

    MongoDB Connection and Data Retrieval:
      Connection established to MongoDB Atlas
      Fetched the sample Airbnb dataset from MongoDB
      
    Data Cleaning and Preparation:
      Undertaken the EDA process in google colaboratory
      Handled the missing values, removing duplicates, and converting data types for accurate analysis
      The dataset was made ready for exploratory data analysis and visualization tasks
    
    Price Analysis and Visualization:
      Using the cleaned data, we conducted in-depth analysis of how prices vary across different locations, property types, and seasons. Dynamic            plots and charts were created to enable users to explore price trends
    
    Location-Based Insights:
        We investigated how the price of listings varies across different locations. MongoDB queries and data aggregation techniques were used to             extract relevant information for specific regions or neighborhoods. These insights were visualized on interactive maps or created dashboards          in Power BI.
    
    Geospatial Visualization using Streamlit:
        We developed a Streamlit web application that utilizes geospatial data from the Airbnb dataset. Interactive maps were created to visualize            the distribution of Airbnb listings across different locations, allowing users to explore prices, ratings, and other relevant factors.

## Author

@Theressac

