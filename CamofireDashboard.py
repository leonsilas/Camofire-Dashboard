import streamlit as st
import pandas as pd
import datetime

# Setting up df
input = pd.read_csv("items_to_q.csv")
df = pd.DataFrame(input)
df.drop(columns=["Unnamed: 0"], inplace=True)
df.insert(0, "In Queue", False)

start_df = df.copy()
   
# Utilities
st.set_page_config(page_title="Camofire Automated Queue Selection", page_icon="🔥", layout="wide")
config = {
    "item_id": st.column_config.NumberColumn(
        "Item ID",
        format="%.0f",
        step=1,
        disabled=True,),
    "cost": st.column_config.NumberColumn(
        "Cost (in USD)",
        format="$%.2f",
        step=0.01,
        required=True,),
    "price": st.column_config.NumberColumn(
        "Price (in USD)",
        format="$%.2f",
        step=0.01,
        required=True,),
}
# TODO General formatting changes to application for aesthetic

###                  ###
### MAIN APPLICATION ###
###                  ###

"""
# Camofire Queue Selection
"""

# Session Variables
state = st.session_state

if 'key' not in state:
    state.key = 0
    
if 'date' not in state:
    state.date = datetime.date(2024, 3, 13)
    
if 'purchase_limit' not in state:
    state.purchase_limit = 3

if "stateful_df" not in state:
    state_stateful_df = start_df

if "checked_sum" not in state:
    state.checked_sum = 0
    
if "total_value" not in state:
    state.total_value = 0
    
if 'sales_value' not in state:
    state.sales_value = 0 #Replace with algorithm output

if 'revenue_value' not in state:
    state.revenue_value = 0 #Replace with algorithm output
    
if 'revenue_percent_value' not in state:
    state.revenue_percent_value = 0 #Replace with algorithm output

if 'revenue_estimate_value' not in state:
    state.revenue_estimate_value = 0 #Replace with algorithm output
    
# Functions      
def reset():
    state.key += 1
    
def change_day(date):
    state.date += datetime.timedelta(days=1)
    date = state.date
    
def create_queue_df():
    queue_df = edited_df.copy()
    for i in range(0, len(edited_df)):
        if edited_df["In Queue"][i] == False:
            queue_df.drop(i, inplace=True)
    queue_df.reset_index(drop=True, inplace=True)
    queue_df.drop(columns=["In Queue"], inplace=True)
    return queue_df

def select_first_eighty():   
    # TODO Make this update df first 80 items to True
    pass

###################
# Database Editor
###################
header_left, header_right = st.columns([1,1])
date = header_left.date_input("Date for Queue:", value="today", format="MM/DD/YYYY") # Date selection
header_right.number_input("Purchase Limit:", value=state.purchase_limit, min_value=0) # Purchase limit
   
edited_df = st.data_editor(state_stateful_df, column_config= config, use_container_width=True, key=f'editor_{state.key}')

# Update session variables from changes to df
if state_stateful_df is not edited_df: # TODO Fix edge case of changing back to original df not updating totals
    # Total selected value calcuation
    state.total_value = 0
    for i in range(0, len(edited_df)):
        if edited_df["In Queue"][i] == True:
            state.total_value += df["price"][i]
              
    # TODO Update with necessary outputs        
    #state.sales_value # Update this with algorithm output
    #state.revenue_value # Update this with algorithm output
    #state.revenue_estimate_value # Update this with algorithm output
    #state.revenue_percent_value # Update this with algorithm output
    
    # In Queue sum
    state.checked_sum = edited_df["In Queue"].sum()
    
    # Alert if too many are checked
    if state.checked_sum > 80:
        st.error("You have selected more than 80 items to queue, please unselect some items to continue.")
    
# Tracks number of items selected to queue
if edited_df["In Queue"].sum() > 0:
    st.write("Items selected to queue")
    st.write(state.checked_sum)

###################
# Buttons
###################
buttons_left, buttons_middle_left, buttons_middle_right, buttons_right = st.columns([1,1,1,1])

# Button to reset data to original
reset = buttons_left.button("Reset Data", on_click=reset) 

# Button to select first 80 items
first_eighty = buttons_middle_left.button("Select first 80", on_click=select_first_eighty)

# Button to download selections to csv
buttons_right.download_button(
    label="Download Selected to CSV",
    data=create_queue_df().to_csv().encode("utf-8"),
    file_name="edited_df.csv",
    mime="text/csv",
)

###################
# Metrics
###################
st.metric(label="Total selected value", value=f"${'{:.2f}'.format(round(state.total_value, 2))}")

metrics_left, metrics_right = st.columns([1,1])
metrics_left.metric(label="Total estimated sales value", value=f"${'{:.2f}'.format(round(state.sales_value, 2))}")

metrics_right.metric(label="Total estimated revenue", value=f"${'{:.2f}'.format(round(state.revenue_value, 2))}")

metrics_right.metric(label="Average estimated revenue %", value=f"{'{:.2f}'.format(round(state.revenue_estimate_value, 2))}%")

metrics_left.metric(label="Average selected revenue %", value=f"{'{:.2f}'.format(round(state.revenue_percent_value, 2))}%")

# Nice to have's / next steps
# TODO Add more outputs based on Camofire requests
# TODO Button for next day generation (Moved to backlog)

# Unused features still in code
# Button to calculate new metrics
#calculate = buttons_middle.button("Calculate Metrics") # Backup button in case we don't want dynamic output of current csv (currently loads quickly)    
