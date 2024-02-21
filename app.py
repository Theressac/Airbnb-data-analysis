import streamlit as st
from streamlit_option_menu import option_menu
import pymongo
import pandas as pd
import plotly_express as px

#setting up streamlit

st.set_page_config(page_title = "Airbnb data analysis | Theressa Coujandessamy",
                   layout= "centered",
                     initial_sidebar_state= "auto",
                   menu_items={'About': """# This app is developed by *Theressa Coujandessamy*! 
                                The data is gathered by mongodb atlas"""
                               })
st.sidebar.title("Airbnb Data Insights")
#Creating the sidebar menu option


st.title("Airbnb Data Analysis")

#Cleaned Data 
df = pd.read_csv('airbnb_cleaned_data4.csv')


    
#owverview

# GETTING USER INPUTS
country = st.sidebar.multiselect('Country',sorted(df.Country.unique()),sorted(df.Country.unique()))
neighbourh = st.sidebar.multiselect('City',df.City.unique())
prop = st.sidebar.multiselect('Property type',sorted(df.Property_type.unique()),sorted(df.Property_type.unique()))
room = st.sidebar.multiselect('Room type',sorted(df.Room_type.unique()),sorted(df.Room_type.unique()))
bedroom = st.sidebar.multiselect('Total bedrooms',sorted(df.Total_bedrooms.unique()),sorted(df.Total_bedrooms.unique()))
no_of_accomodates = st.sidebar.multiselect('No of guests',sorted(df.Accomodates.unique()),sorted(df.Accomodates.unique()))
total_beds = st.sidebar.multiselect('Total beds',sorted(df.Total_beds.unique()),sorted(df.Total_beds.unique()))
#bedroom = st.sidebar.slider('Total bedrooms',df.Total_bedrooms.min(),df.Total_bedrooms.max(),(df.Total_bedrooms.min(),df.Total_bedrooms.max()))
#no_of_accomodates = st.sidebar.slider('No of guests',df.Accomodates.min(),df.Accomodates.max(),(df.Accomodates.min(),df.Accomodates.max()))
#total_beds = st.sidebar.slider('Total beds',df.Total_beds.min(),df.Total_beds.max(),(df.Total_beds.min(),df.Total_beds.max()))

price = st.sidebar.slider('Price',df.Price.min(),df.Price.max(),(df.Price.min(),df.Price.max()))
review_scor = st.sidebar.slider('Ratings',df.Review_scores.min(),df.Review_scores.max(),(df.Review_scores.min(),df.Review_scores.max()))
#no_of_reviews = st.sidebar.slider('Number of Reviews',df.No_of_reviews.min(),df.No_of_reviews.max(),(df.No_of_reviews.min(),df.No_of_reviews.max()))
availability = st.sidebar.slider('Availability',df.Availability_365.min(),df.Availability_365.max(),(df.Availability_365.min(),df.Availability_365.max()))
cleaning_fee = st.sidebar.slider('Cleaning Fee',df.Cleaning_fee.min(),df.Cleaning_fee.max(),(df.Cleaning_fee.min(),df.Cleaning_fee.max()))
cancellation_policy = st.sidebar.multiselect('Cancellation Policy',sorted(df.Cancellation_policy.unique()),sorted(df.Cancellation_policy.unique()))

# CONVERTING THE USER INPUT INTO QUERY
#neighbourhood in {neighbourh} &
#&  Amenities in {amenities} &  Accomodates in {no_of_accomodates}
#&  No_of_reviews in {no_of_reviews}
query = f'Country in {country} & Room_type in {room} &  Total_bedrooms in {bedroom} & Property_type in {prop} & City in {neighbourh} &  Price >= {price[0]} & Price <= {price[1]} &  Review_scores in {review_scor} &  Accomodates in {no_of_accomodates} &  Total_beds in {total_beds} &  Cancellation_policy in {cancellation_policy} &  Availability_365 in {availability} &  Cleaning_fee in {cleaning_fee}'


# Average Price by property type
avg_property_type= df.query(query).groupby('Property_type',as_index=False)['Price'].mean().sort_values(by='Price')
fig = px.bar(data_frame=avg_property_type,
                x='Property_type',
                y='Price',
                color='Price',
                title='Average price per property type'
            )
st.plotly_chart(fig,use_container_width=True)

df1 = df.query(query).groupby(["Property_type"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
fig = px.bar(df1,
                    title='Property Type',
                    x='Property_type',
                    y='Listings',
                    orientation='v',
                    color='Property_type',
                    color_continuous_scale=px.colors.sequential.Electric)
st.plotly_chart(fig,use_container_width=True) 


# Average minimum nights per Room Type
avg_min_night_roomtype= df.query(query).groupby('Room_type',as_index=False)['Min_nights'].mean().sort_values(by='Min_nights')
fig = px.bar(data_frame=avg_min_night_roomtype,
                x='Room_type',
                y='Min_nights',
                orientation='v',
                color='Room_type',
                title='Average minimum nights per Room Type'
            )
st.plotly_chart(fig,use_container_width=True)

# Average Price for city
avg_price_city= df.query(query).groupby('City',as_index=False)['Price'].mean().sort_values(by='Price')
fig = px.bar(data_frame=avg_price_city,
                x='Price',
                y='City',
                orientation='h',
                color='Price',
                title='Average price per city'
            )
st.plotly_chart(fig,use_container_width=True)

# Top cities by ratings
top_city_ratings= df.query(query).groupby('City',as_index=False)['Review_scores'].sum().sort_values(by='Review_scores')
fig = px.bar(data_frame=top_city_ratings,
                x='Review_scores',
                y='City',
                orientation='h',
                color='Review_scores',
                title='Top cities by ratings'
            )
st.plotly_chart(fig,use_container_width=True)

# Which property types have the best ratings?
property_type_best_ratings= df.query(query).groupby('Property_type',as_index=False)['Review_scores'].count().sort_values(by='Review_scores')
fig = px.bar(data_frame=property_type_best_ratings,
                x='Review_scores',
                y='Property_type',
                orientation='h',
                color='Review_scores',
                title='Which property types have the best ratings?'
            )
st.plotly_chart(fig,use_container_width=True)

    
# TOTAL LISTINGS IN EACH ROOM TYPES PIE CHART
df1 = df.query(query).groupby(["Room_type"]).size().reset_index(name="counts")
fig = px.pie(df1,
                title='Room Type',
                names='Room_type',
                values='counts',
                color_discrete_sequence=px.colors.sequential.Rainbow
            )
fig.update_traces(textposition='outside', textinfo='value+label')
st.plotly_chart(fig,use_container_width=True)


# Average Price per room type
pr_df = df.query(query).groupby('Room_type',as_index=False)['Price'].mean().sort_values(by='Price')
fig = px.bar(data_frame=pr_df,
                x='Room_type',
                y='Price',
                color='Price',
                title='Average Price per Room type'
            )
st.plotly_chart(fig,use_container_width=True)


# Average price in each country
country_df = df.query(query).groupby('Country',as_index=False)['Price'].mean()
fig = px.scatter_geo(data_frame=country_df,
                                locations='Country',
                                color= 'Price', 
                                hover_data=['Price'],
                                locationmode='country names',
                                size='Price',
                                title= 'Average Price in each Country',
                                color_continuous_scale='agsunset'
                    )
st.plotly_chart(fig,use_container_width=True)

# TOTAL LISTINGS BY COUNTRY CHOROPLETH MAP
country_df = df.query(query).groupby(['Country'],as_index=False)['Name'].count().rename(columns={'Name' : 'Total_Listings'})
fig = px.choropleth(country_df,
                    title='Total Listings in each Country',
                    locations='Country',
                    locationmode='country names',
                    color='Total_Listings',
                    color_continuous_scale=px.colors.sequential.Plasma
                    )
st.plotly_chart(fig,use_container_width=True)


        

