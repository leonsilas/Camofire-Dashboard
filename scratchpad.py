import streamlit as st

header = st.container()
header_left, header_right = header.columns([1,1])
header_left.date_input("Date for Queue:", datetime.date(2024, 3, 13)) # Date selection
header_right.number_input("Purchase Limit:", value=3, min_value=0) # Purchase limit

st.data_editor(edited_df, use_container_width=True, num_rows="dynamic")


# Statefullness Achieved fuck yes
if "total" not in st.session_state:
    st.session_state.total = start_df["price"].sum()

new_total = st.button("New Total")
if new_total:
    st.session_state.total = start_df["cost"].sum()