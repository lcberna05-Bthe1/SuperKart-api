import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = "http://backend:7860"

# Set the title of the Streamlit app
st.title("SuperKartFinal")

import streamlit as st
import re

st.set_page_config(page_title="Product Store Sales Prediction", layout="wide")

st.title("🛒 Product Store Sales Prediction")
st.write("Enter product and store details below.")

# -----------------------------
# Product Information
# -----------------------------
st.subheader("Product Information")

product_id = st.text_input(
    "Product ID",
    placeholder="Example: FD123"
)

# Validate Product ID
if product_id:
    if not re.match(r"^[A-Za-z]{2}\d+$", product_id):
        st.warning("Product ID must start with 2 letters followed by numbers (Example: FD123)")

product_weight = st.number_input(
    "Product Weight (kg)",
    min_value=0.0,
    value=1.0,
    step=0.1
)

product_sugar_content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

product_allocated_area = st.slider(
    "Allocated Display Area Ratio",
    min_value=0.0,
    max_value=1.0,
    value=0.1,
    step=0.01
)

product_type = st.selectbox(
    "Product Type",
    [
        "Meat",
        "Snack Foods",
        "Hard Drinks",
        "Dairy",
        "Canned",
        "Soft Drinks",
        "Health and Hygiene",
        "Baking Goods",
        "Bread",
        "Breakfast",
        "Frozen Foods",
        "Fruits and Vegetables",
        "Household",
        "Seafood",
        "Starchy Foods",
        "Others"
    ]
)

product_mrp = st.number_input(
    "Product MRP ($)",
    min_value=0.0,
    value=100.0,
    step=1.0
)

# -----------------------------
# Store Information
# -----------------------------
st.subheader("Store Information")

store_id = st.text_input(
    "Store ID",
    placeholder="Example: OUT049"
)

store_establishment_year = st.number_input(
    "Store Establishment Year",
    min_value=1900,
    max_value=2100,
    value=2000,
    step=1
)

store_size = st.selectbox(
    "Store Size",
    ["High", "Medium", "Low"]
)

store_city_type = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

store_type = st.selectbox(
    "Store Type",
    [
        "Departmental Store",
        "Supermarket Type 1",
        "Supermarket Type 2",
        "Food Mart"
    ]
)

# -----------------------------
# Sales Information
# -----------------------------
st.subheader("Sales Information")

product_store_sales_total = st.number_input(
    "Product Store Sales Total ($)",
    min_value=0.0,
    value=1000.0,
    step=10.0
)

# -----------------------------
# Submit Button
# -----------------------------
if st.button("Submit"):

    user_input = {
        "Product_Id": product_id,
        "Product_Weight": product_weight,
        "Product_Sugar_Content": product_sugar_content,
        "Product_Allocated_Area": product_allocated_area,
        "Product_Type": product_type,
        "Product_MRP": product_mrp,
        "Store_Id": store_id,
        "Store_Establishment_Year": store_establishment_year,
        "Store_Size": store_size,
        "Store_Location_City_Type": store_city_type,
        "Store_Type": store_type,
        "Product_Store_Sales_Total": product_store_sales_total
    }

    st.success("Data Submitted Successfully!")

    st.subheader("Collected Input Data")
    st.json(user_input)
