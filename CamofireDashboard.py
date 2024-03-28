import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import datetime

# Dataframe and aesthetic changes
input = pd.read_csv("items_to_q.csv")
df = pd.DataFrame(input)
df.drop(columns=["Unnamed: 0"], inplace=True)
df.insert(0, "In Queue", False)

start_df = df.copy()
   
# Utilities
st.set_page_config(page_title="Camofire Automated Queue Selection", page_icon="🔥", layout="wide")
#selectbox = st.sidebar.selectbox('Select a model', ['Pricing', 'Queuing', 'Forecasting'])

###                  ###
### MAIN APPLICATION ###
###                  ###

"""
# Camofire Queue Selection
"""

# Session Variables
if 'sales_value' not in st.session_state:
    st.session_state.sales_value = 0
    
if "total" not in st.session_state:
    st.session_state.total = start_df["price"].sum()

if "stateful_df" not in st.session_state:
    st.session_state_stateful_df = start_df

if "checked_sum" not in st.session_state:
    st.session_state.checked_sum = 0

###################
# Database Editor
###################
# TODO Alert if too many checked    
edited_df = st.data_editor(start_df, use_container_width=True, num_rows="dynamic")

if st.session_state_stateful_df is not edited_df: # Edge case of changing back to original df not updating totals
    st.session_state.total = edited_df["price"].sum()
    st.session_state.checked_sum = edited_df["In Queue"].sum()
    
    if st.session_state.checked_sum > 80:
        st.error("You have selected more than 80 items to queue, please unselect some items to continue.")
    
# Debugging Output  
st.write("Total estimated sales value")
st.write(st.session_state.total)
st.write("Total checked items")
st.write(st.session_state.checked_sum)

###################
# Buttons
###################
buttons_left, buttons_middle, buttons_right = st.columns([1,1,1])

# Button to select first 80 items
first_eighty = buttons_left.button('Select first 80') # TODO Make this button dynamic to select first 80 items

# Button for next day generation
# TODO Make this button dynamic to update data to day after selected date
# TODO Update this again later to have model retrained based off selected queue for current day
buttons_middle.button('Generate next day')

# Button to download selections to csv
buttons_right.download_button(
    label="Download Selected to CSV",
    data=edited_df.to_csv().encode('utf-8'),
    file_name='edited_df.csv',
    mime='text/csv',
)

###################
# Metrics
###################
# TODO Make this text dynamic to selected queue items
total = 1000000
st.session_state.sales_value = start_df["price"].sum()
revenue = 20922.01
revenue_percent = 18.8
estimated_percent = 23.6

# Metrics
# TODO Change all these widgets to writes since widgets can't be stateful once instantiated
st.metric("Total selected value", f"${total}")
metric_left, metric_right = st.columns([1,1])
metric_left.metric("Total estimated sales value", f"${st.session_state.sales_value}")
metric_left.metric("Average selected revenue %", f"{revenue_percent}%")
metric_right.metric("Total estimated revenue", f"${revenue}")
metric_right.metric("Average estimated revenue %", f"{estimated_percent}%")
# TODO Add more outputs based on Camofire requests


