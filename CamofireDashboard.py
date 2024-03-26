import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import datetime

# Functions
def update_totals(edited_df):
    edited_df["Unit Price"].sum()
    
def save_df():  
    return edited_df #TODO make this stateful to currently selected "in queue"
    
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

# Utilities
st.set_page_config(page_title="Camofire Automated Queue Selection", page_icon="🔥", layout="wide")
selectbox = st.sidebar.selectbox('Select a model', ['Pricing', 'Queuing', 'Forecasting'])

###                  ###
### MAIN APPLICATION ###
###                  ###

"""
# Camofire Automated Queue Selection
"""

###################
# Database Editor
###################
header = st.container()
header_left, header_right = header.columns([1,1])
header_left.date_input("Selecting items for:", datetime.date(2024, 3, 13)) # Date selection
header_right.number_input("Purchase limit:", value=3, min_value=0) # Purchase limit

edited_df = st.data_editor(df, use_container_width=True)

# TODO Alert if too many checked

###################
# Buttons
###################
buttons_left, buttons_middle_left, buttons_middle_right, buttons_right = st.columns([1,1,1,1])

# Button to select first 80 items
buttons_left.button('Select first 80') # TODO Make this button dynamic to select first 80 items

# Button to update totals
buttons_middle_left.button('Update Totals')#, on_click=update_totals)

# Button for next day generation
# TODO Make this button dynamic to update data to day after selected date
# TODO Update this again later to have model retrained based off selected queue for current day
buttons_middle_right.button('Generate next day')

# Button to download selections to csv
buttons_right.download_button(
    label="Download to CSV",
    data=save_df().to_csv().encode('utf-8'),
    file_name='edited_df.csv',
    mime='text/csv',
)

###################
# Metrics
###################
# TODO Make this text dynamic to selected queue items
total = 1000000
sales_value = 23947.34
revenue = 20922.01
revenue_percent = 18.8
estimated_percent = 23.6

# Metrics
st.metric("Total selected value", f"${total}")
metric_left, metric_right = st.columns([1,1])
metric_left.metric("Total estimated sales value", f"${sales_value}")
metric_left.metric("Average selected revenue %", f"{revenue_percent}%")
metric_right.metric("Total estimated revenue", f"${revenue}")
metric_right.metric("Average estimated revenue %", f"{estimated_percent}%")
# TODO Add more outputs based on Camofire requests