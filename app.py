import pandas as pd
import streamlit as st
import plotly.express as px
import tableauserverclient as TSC

st.set_page_config(layout="wide")

st.write('# Airbnb Data Analysis project')

data=pd.read_csv('Cleaned_Data.csv')
cropped_data=data.copy()

selectbox_dict={'property_type':'Select property type',
                'room_type':'Select room type',
                'bed_type':'Select bed type',
                'cancellation_policy':'Select cancellation_policy',
                'coutry':'Select Country'
                }

slider_dict={'accommodates':'Choose number of accomodates',
             'bedrooms':'Choose number of bedrooms',
             'beds':'Choose number of beds',
             'bathrooms':'Choose number of bathrooms'
             }

review_dict={'review_scores_accuracy':'Choose minimum score accuracy',
             'review_scores_cleanliness':'Choose minimum cleanliness score',
             'review_scores_checkin':'Choose minimum check in score',
             'review_scores_communication':'Choose minimum communication score',
             'review_scores_location':'Choose minimum location score',
             'review_scores_value':'Choose minimum value score',
             'review_scores_rating':'Choose minimum total rating'
             }

col1,col2=st.columns([0.5,0.5])

#Give user options to select fields
with col1:
    
    col1_1,col1_2=st.columns([0.5,0.5])
    with col1_1:
        for key,value in selectbox_dict.items():
            box=st.selectbox(value,data[key].unique(),index=None,placeholder='Any')
            if box!=None:
                cropped_data=cropped_data[cropped_data[key]==box]
                cropped_data=cropped_data.reset_index(drop=True)
    
        days=st.number_input('Type number of days you will be staying',
                             value=None,
                             placeholder='None selected',
                             step=1)
        if days!=None:
            cropped_data=cropped_data[
                (cropped_data['minimum_nights']<=days) &
                (cropped_data['maximum_nights']>=days)]
    
    with col1_2:
        for key,value in slider_dict.items():
            slide=st.slider(value,data[key].min(),data[key].max(),data[key].min())
            check=st.checkbox('Apply '+str(slide)+' '+key)
            if check:
                cropped_data=cropped_data[cropped_data[key]==slide]
                cropped_data=cropped_data.reset_index(drop=True)
    
    for key,value in review_dict.items():
        slide=st.slider(value,0,int(data[key].max()),0)
        cropped_data=cropped_data[cropped_data[key]>=slide]
        cropped_data=cropped_data.reset_index(drop=True)
        
#Display the accomodations as per selected fileds
with col2:
    st.write('Total number of accomodations:',len(cropped_data))
    show_data=cropped_data.drop(
        ['number_of_reviews','reviews_per_month','coordinate1',
         'coordinate2','coutry_code'],
        axis=1
        )
    show_data
        
    st.write('_'*100)
    Y_axis=st.selectbox('Select price field to view plots',
                        ['price','security_deposit','cleaning_fee',
                         'weekly_price','monthly_price'])
    X_axis=st.selectbox('Select against what you would like the field',
                        ['property_type','coutry','room_type'])
    
    type_val=st.selectbox('Select Min, Max, Average',
                      ['Minimum','Average','Maximum'])

    options=list(cropped_data[X_axis].unique())
    values=[]
    
    if type_val=='Minimum':
        for item in options:
            values.append(
                cropped_data[Y_axis][cropped_data[X_axis]==item].min()
                )
    elif type_val=='Maximum':
        for item in options:
            values.append(
                cropped_data[Y_axis][cropped_data[X_axis]==item].max()
                )
    else:
        for item in options:
            values.append(
                cropped_data[Y_axis][cropped_data[X_axis]==item].mean()
                )
    
    plot_data=pd.DataFrame(
        {
         'X': options,
         'Y': values,
         }
        )
    
    fig=px.bar(plot_data,x='X',y='Y')
    fig.update_xaxes(title_text=X_axis)
    fig.update_yaxes(title_text=Y_axis)
    st.plotly_chart(fig)

#Display the Tableau Tables


#Prwpare data for Geoplot
map_col=['minimum_nights','maximum_nights','accommodates',
         'bedrooms','beds','bathrooms','price','security_deposit',
         'cleaning_fee','extra_people','guests_included','weekly_price',
         'monthly_price','review_scores_accuracy','review_scores_cleanliness',
         'review_scores_checkin','review_scores_communication',
         'review_scores_location','review_scores_value','review_scores_rating']

map_data=pd.DataFrame(columns=['coutry_code','country']+map_col)

country_codes={'PT':'Portugal','BR':'Brazil','US':'United States',
               'TR':'Turkey','CA':'Canada','HK':'Hong Kong','ES':'Spain',
               'AU':'Australia','CN':'China'}

alpha_2_to_3={'PT':'PRT','BR':'BRA','US':'USA','TR':'TUR','CA':'CAN',
              'HK':'HKG','ES':'ESP','AU':'AUS','CN':'CHN'}

for code,country in country_codes.items():
    agg_data=data[data['coutry_code']==code]
    value=[alpha_2_to_3[code],country]
    for col in map_col:
        value.append(agg_data[col].mean())
    map_data.loc[len(map_data)]=value

map_data=map_data.round(2)

fig = px.choropleth(
    map_data,
    locations='coutry_code',
    locationmode='ISO-3',
    color='price',
    hover_name='country',
    hover_data=map_col,
    color_continuous_scale='Viridis',
    labels={'Value': 'Your Value Label'}
)

#Display Geoplot
st.write('## Geoplot')
st.plotly_chart(fig,use_container_width=True)