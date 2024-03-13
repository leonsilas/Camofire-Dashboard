import streamlit as st
import pandas as pd

# Headings 
st.title('My First Streamlit App')
st.write('Here\'s our first attempt at using data to create a table:')

# Create a sample dataframe
data = {'Name': ['John', 'Jane', 'Mike'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Display the dataframe as a table
st.write(df)