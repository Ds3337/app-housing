import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) by Yuchen Li')
df = pd.read_csv('housing.csv')

median_house_value_filter = st.slider('Minimal Median House Price', 0, 500001, 200000)

st.header('See more filters in the sidebar:')
st.map(df)

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),
     df.ocean_proximity.unique()
     )

income_level = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High')
)

df = df[df.median_house_value >= median_house_value_filter]

df = df[df.ocean_proximity.isin(location_filter)]

if income_level == 'Low':
    df = df[df.median_income <=2.5]
elif income_level =='Medium':
    df = df[(df.median_income <4.5) & (df.median_income > 2.5)]
else:
    df = df[df.median_income >= 4.5]

st.header('Histogram of the median house value')
fig,ax = plt.subplots()
ax.hist(df.median_house_value,bins=30)
st.pyplot(fig=fig)

   