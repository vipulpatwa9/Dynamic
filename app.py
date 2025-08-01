import streamlit as st
import pandas as pd

# Load Excel data
@st.cache_data
def load_data():
    df = pd.read_excel("98002238.xlsx", header=None)
    df.columns = ['Index', 'Value']
    return df

df = load_data()

# 🔐 Title and Instructions
st.title("🔐 Dynamic Login")
st.write("Enter Counter Number to fetch the corresponding value from the system.")

# Input field
number = st.number_input("Enter Counter Number:", min_value=1, step=1)

# Button click action
if st.button("Get Value"):
    result = df[df['Index'] == number]
    if not result.empty:
        # Convert value to int if it's a whole number
        value = result.iloc[0]['Value']
        if value == int(value):
            value = int(value)
        st.success(f"✅ Value for Counter Number {int(number)} is: {value}")
    else:
        st.error("❌ Counter Number not found in the file.")
