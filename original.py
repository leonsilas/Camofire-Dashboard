import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import datetime

# Functions

def update_totals(edited_df):
    st.write(edited_df["Unit Price"].sum())

###                  ###
### MAIN APPLICATION ###
###                  ###

"""
# Camofire Automated Queue Selection
"""

# Dataframe
#should be: is included, price, sale price, days since queued, purchase limit, suggested quantity
# Camofire asked to include description and instead of item ID have item name; Also include different colors/sizes
df = pd.DataFrame( # test DF
    [
        {"Include in Queue": True, "Item ID": "ABC_12345", "Days Since Queued": 12, "Queue Qty": 600, "Unit Price": "$2.12", "Sale Price": "$8.56"},
        {"Include in Queue": True, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": True, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": True, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": True, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": True, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": True, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": True, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": True, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": True, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": True, "Item ID": "ABC_12345", "Days Since Queued": 12, "Queue Qty": 600, "Unit Price": "$2.12", "Sale Price": "$8.56"},
        {"Include in Queue": True, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": True, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": True, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": True, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": True, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": True, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": True, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": True, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": True, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": True, "Item ID": "ABC_12345", "Days Since Queued": 12, "Queue Qty": 600, "Unit Price": "$2.12", "Sale Price": "$8.56"},
        {"Include in Queue": True, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": True, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": True, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": True, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": True, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": True, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": True, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": True, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": True, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": True, "Item ID": "ABC_12345", "Days Since Queued": 12, "Queue Qty": 600, "Unit Price": "$2.12", "Sale Price": "$8.56"},
        {"Include in Queue": True, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": True, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": True, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": True, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": True, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": True, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": True, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": True, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": True, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": True, "Item ID": "ABC_12345", "Days Since Queued": 12, "Queue Qty": 600, "Unit Price": "$2.12", "Sale Price": "$8.56"},
        {"Include in Queue": True, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": True, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": True, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": True, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": True, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": True, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": True, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": True, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": True, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": True, "Item ID": "ABC_12345", "Days Since Queued": 12, "Queue Qty": 600, "Unit Price": "$2.12", "Sale Price": "$8.56"},
        {"Include in Queue": True, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": True, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": True, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": True, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": True, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": True, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": True, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": True, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": True, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": True, "Item ID": "ABC_12345", "Days Since Queued": 12, "Queue Qty": 600, "Unit Price": "$2.12", "Sale Price": "$8.56"},
        {"Include in Queue": True, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": True, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": True, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": True, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": True, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": True, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": True, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": True, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": True, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": True, "Item ID": "ABC_12345", "Days Since Queued": 12, "Queue Qty": 600, "Unit Price": "$2.12", "Sale Price": "$8.56"},
        {"Include in Queue": True, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": True, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": True, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": True, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": True, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": True, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": True, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": True, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": True, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": True, "Item ID": "ABC_12345", "Days Since Queued": 12, "Queue Qty": 600, "Unit Price": "$2.12", "Sale Price": "$8.56"},
        {"Include in Queue": False, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": False, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": False, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": False, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": False, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": False, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": False, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": False, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": False, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": False, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": False, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": False, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": False, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": False, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": False, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": False, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": False, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": False, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": False, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": False, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": False, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": False, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": False, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": False, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": False, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": False, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": False, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": False, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": False, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": False, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": False, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": False, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": False, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": False, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": False, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": False, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": False, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": False, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": False, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": False, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": False, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": False, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": False, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": False, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": False, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": False, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": False, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": False, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": False, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": False, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": False, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": False, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": False, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": False, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": False, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": False, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": False, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": False, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": False, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": False, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": False, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
        {"Include in Queue": False, "Item ID": "YZ_62795", "Days Since Queued": 2, "Queue Qty": 15, "Unit Price": "$80.00", "Sale Price": "$165.88"},
        {"Include in Queue": False, "Item ID": "FOO_65314", "Days Since Queued": 80, "Queue Qty": 55, "Unit Price": "$46.00", "Sale Price": "$124.88"},
        {"Include in Queue": False, "Item ID": "DEF_67890", "Days Since Queued": 14, "Queue Qty": 20, "Unit Price": "$100.00", "Sale Price": "$150"},
        {"Include in Queue": False, "Item ID": "GHI_11235", "Days Since Queued": 8, "Queue Qty": 24, "Unit Price": "$450.00", "Sale Price": "$900"},
        {"Include in Queue": False, "Item ID": "JKL_31415", "Days Since Queued": 4, "Queue Qty": 80, "Unit Price": "$37.00", "Sale Price": "$94"},
        {"Include in Queue": False, "Item ID": "MNO_92653", "Days Since Queued": 17, "Queue Qty": 160, "Unit Price": "$1.17", "Sale Price": "$4.01"},
        {"Include in Queue": False, "Item ID": "PQR_58979", "Days Since Queued": 9, "Queue Qty": 610, "Unit Price": "$5.36", "Sale Price": "$9.04"},
        {"Include in Queue": False, "Item ID": "STU_32384", "Days Since Queued": 41, "Queue Qty": 60, "Unit Price": "$48.38", "Sale Price": "$99.99"},
        {"Include in Queue": False, "Item ID": "VWX_62664", "Days Since Queued": 27, "Queue Qty": 95, "Unit Price": "$12.36", "Sale Price": "$27.33"},
    ]
)

st.write("\n\n")

# Date selection
d = st.date_input("Selecting items for:", datetime.date(2024, 3, 13))

# TODO Figure out what this means
purchase_limit = st.number_input("Purchase limit:", value=3, min_value=0)

#Button to select first 80 items for queue
# TODO Make this button dynamic to select first 80 items
st.button('Select first 80')

#estimated revenue:
#total estimated revenue %
#total estimated revenue
#total cost in

# Interactive selection using Dataframe
# TODO Alert if too many checked
edited_df = st.data_editor(df)

# Print out information from edited_df
# TODO Make this text dynamic to selected queue items
# TODO Add more outputs based on Camofire requests
# TODO Print out total price of selected items
#total = df["Unit Price"].sum()
#st.text(total)
st.text("Total selected value: $25,486.37")
st.text("Total estimated sales value: $17,794.22")
st.text("Total estimated revenue: $1,564.23")
st.text("Average selected revenue %: 8.6%")
st.text("Average estimated revenue %: 8.8%")

# Button to download selections to csv
st.download_button(
    label="Download selection data as CSV",
    data=edited_df.to_csv().encode('utf-8'),
    file_name='edited_df.csv',
    mime='text/csv',
)

# Button for next day generation
# TODO Make this button dynamic to update data to day after selected date
# TODO Update this again later to have model retrained based off selected queue for current day
st.button('Generate next day')

