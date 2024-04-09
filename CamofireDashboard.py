import streamlit as st
import pandas as pd
import datetime

# TODO INT: There should be: id, sold_price, sale sold_price, days since queued, purchase limit, suggested quantity
    #  Camofire asked to include description and instead of item ID have item name; Also include different colors/sizes

# Setting up df
input = pd.read_csv("items_to_queue.csv")
df = pd.DataFrame(input)
#df.drop(columns=["Unnamed: 0"], inplace=True) # Uncomment if there is an extra column
df.drop(columns=["queue_date"], inplace=True)
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
    "sold_price": st.column_config.NumberColumn(
        "Selling Price (in USD)",
        format="$%.2f",
        step=0.01,
        required=True,),
    "quantity_in_inventory": st.column_config.NumberColumn(
        "Qty In Stock",
        format="%.0f",
        step=1,
        required=True,),
    # "days_since_queued": st.column_config.NumberColumn(
    #     "Days Since Last Queued",
    #     format="%.0f",
    #     step=1,),
    "quantity_to_queue": st.column_config.NumberColumn(
        "Qty To Queue",
        format="%.0f",
        step=1,),
    "retail_price": st.column_config.NumberColumn(
        "Retail Price",
        format="$%.2f",
        step=0.01,
        required=True,),
}

# Session Variables
state = st.session_state
if 'key' not in state:
    state.key = 0   
if 'date' not in state:
    state.date = datetime.date.today()  
if 'purchase_limit' not in state:
    state.purchase_limit = 2
if "stateful_df" not in state:
    state.stateful_df = start_df
if "checked_sum" not in state:
    state.checked_sum = 0   
if "total_value" not in state:
    state.total_value = 0 
if 'sales_value' not in state:
    state.sales_value = 0
if 'revenue_value' not in state:
    state.revenue_value = 0 
if 'profit_value' not in state:
    state.profit_value = 0
if 'margin_value' not in state:
    state.margin_value = 0
    
# Functions      
def reset():
    state.stateful_df = start_df
    state.key += 1
    
def change_day():
    state.date += datetime.timedelta(days=1)
    # TODO INT: Have df update with date selection
    state.key += 1
    
def create_queue_df():
    queue_df = edited_df.copy()
    for i in range(0, len(edited_df)):
        if edited_df["In Queue"][i] == False:
            queue_df.drop(i, inplace=True)
    queue_df.reset_index(drop=True, inplace=True)
    queue_df.drop(columns=["In Queue"], inplace=True)
    return queue_df

def calculate_metrics():
    # In Queue sum
    state.checked_sum = edited_df["In Queue"].sum()
    
    # Total selected value calcuation
    state.total_value = 0
    state.sales_value = 0
    state.revenue_value = 0
    state.profit_value = 0
    state.margin_value = 0
    for i in range(0, len(edited_df)):
        if edited_df["In Queue"][i] == True:
            # cogs
            state.total_value += df["cost"][i] * df["quantity_to_queue"][i]   
            # sales value
            state.sales_value += df["retail_price"][i] * df["quantity_to_queue"][i]
            # gross revenue
            state.revenue_value += df["sold_price"][i] * df["quantity_to_queue"][i]
            # profit
            state.profit_value += (df["sold_price"][i] * df["quantity_to_queue"][i]) - (df["cost"][i] * df["quantity_to_queue"][i]) / state.checked_sum
            # profit margin
            state.margin_value += ((df["sold_price"][i] * df["quantity_to_queue"][i] - df["cost"][i] * df["quantity_to_queue"][i]) / (df["sold_price"][i] * df["quantity_to_queue"][i]) * 100 ) / state.checked_sum

def select_first_eighty():   
    edited_df["In Queue"] = False
    edited_df.loc[0:79, "In Queue"] = True
    state.stateful_df = edited_df

def align_buttons():
    st.write("")
    st.write("")

# Setup Header
st.image("assets/camofire_logo_text.png", width=600)
header_date, header_next_day, header_filler, header_reset, header_select_eighty, header_download = st.columns([.5,.25, 1.5,.25,.25,.41])    

###################
# Database Editor
###################
edited_df = st.data_editor(state.stateful_df, column_config= config, use_container_width=True, key=f'editor_{state.key}')

# Update session variables from changes to df      
if state.stateful_df is not None:    
    calculate_metrics()
    
    # Alert if too many are checked
    #if state.checked_sum > 80:
    #    st.error("You have selected more than 80 items to queue, please unselect some items to continue.")
    
# Tracks number of items selected to queue
if edited_df["In Queue"].sum() > 0:
    st.write("Items selected to queue: {}".format(state.checked_sum))


###################
# Header & Buttons
###################
with header_date:
    st.date_input("Date for Queue:", value=state.date, format="MM/DD/YYYY") # Date selection
with header_next_day:
    align_buttons()
    st.button("Next Day", on_click=change_day, use_container_width=True) # Refreshes page with model output for next date
with header_reset:
    align_buttons()
    st.button("Reset Data", on_click=reset, use_container_width=True) # Button to reset data to original    
with header_select_eighty:
    align_buttons()
    st.button("Select first 80", on_click=select_first_eighty, use_container_width=True) # Button to select first 80 items 
with header_download:
    align_buttons()
    save_date = state.date.strftime("%m_%d") 
    st.download_button(
        label="Download Selected to CSV",
        data=create_queue_df().to_csv().encode("utf-8"), # Button to download selections to csv
        file_name= f"queuefor_{save_date}.csv",
        mime="text/csv",
        use_container_width=True
    )

###################
# Metrics
###################
metrics_left, metrics_middle, metrics_right = st.columns(3)
with metrics_left:
    st.metric(label="Total Cost", value=f"${'{:.2f}'.format(round(state.total_value, 2))}")
    st.metric(label="Total Estimated Revenue", value=f"${'{:.2f}'.format(round(state.revenue_value, 2))}") 
with metrics_middle:
    st.metric(label="Total Retail Value", value=f"${'{:.2f}'.format(round(state.sales_value, 2))}")
    st.metric(label="Total Estimated Profit", value=f"${'{:.2f}'.format(round(state.profit_value, 2))}")
with metrics_right:
    st.metric(label="empty", value="", label_visibility="hidden") # Empty metrics to center the metrics
    st.metric(label="empty", value="", label_visibility="hidden")
    st.metric(label="Average Profit Margin %", value=f"{'{:.2f}'.format(round(state.margin_value, 2))}%")

# Button to calculate new metrics
#calculate = buttons_middle.button("Calculate Metrics", on_click=calculate_metrics) # Backup button in case we don't want dynamic output of current csv (currently loads quickly)    