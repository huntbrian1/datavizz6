#!/usr/bin/env python
# coding: utf-8

# In[3]:


# app.py
# This script is generated from the Jupyter Notebook `notebook.ipynb`

import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page layout to wide
st.set_page_config(layout="wide")

# Load the data into a DataFrame named 'df'
df = pd.read_csv("mgt4250spring2024_assignment6.csv")

# Create the 'count_by_state' DataFrame
count_by_state = df.groupby('std_state')['org_id'].nunique().reset_index()
count_by_state.columns = ['State', 'Count']

# Choose three US states of interest
initial_states = ['CA', 'TX', 'NY']

# Replace the list with a multiselect widget
all_states = count_by_state['State'].tolist()
target_states = st.multiselect('Select US States of Interest', options=all_states, default=initial_states)

# Slice the DataFrame to only have rows for the selected states
df_sliced = df[df['std_state'].isin(target_states)]

# Count 'org_subtype_irs' values by 'std_state'
state_orgtype = df_sliced.groupby(['std_state', 'org_subtype_irs']).size().reset_index(name='Count')
state_orgtype.columns = ['State', 'OrgType', 'Count']

# Create the filled map of US states colored by "Count"
fig1 = px.choropleth(
    count_by_state,
    locations='State',
    locationmode="USA-states",
    color='Count',
    scope="usa",
    color_continuous_scale="Viridis",
    title="Unique org_id Count by US State"
)

# Create the treemap
fig2 = px.treemap(
    state_orgtype,
    path=['State', 'OrgType'],
    values='Count',
    title='Treemap of Org Subtypes by State',
    color='Count',
    color_continuous_scale='Viridis'
)

# Split the application screen into two columns - Left 40% and Right 60%
col1, col2 = st.columns([0.4, 0.6])

# Place the figures in the respective columns
with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)


# In[4]:





# In[ ]:




