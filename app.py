import streamlit as st
import pandas as pd
from datetime import datetime

# ==== 1. Check Expiry ====
if datetime.now() > datetime(2026, 8, 5):
    st.error("❌ Session expired. Please contact admin.")
    st.stop()

# ==== 2. Login Page ====
st.title("🔐 Dynamic Login")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Enter Login ID")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if username == "Admin" and password == "12345":
            st.session_state.logged_in = True
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")
    st.stop()

# ==== 3. App Content ====

st.header("🔍 Search For Password ")
st.write("Enter Counter Number to fetch the corresponding value from the system.")

# Load Excel File
@st.cache_data
def load_data():
    df = pd.read_excel("98002238.xlsx")
    return df

df = load_data()

# Input
counter_number = st.number_input("Enter Counter Number:", min_value=1, step=1)
if st.button("Get Value"):
    # Search
    result = df[df[df.columns[0]] == counter_number]
    if not result.empty:
        value = result.iloc[0, 1]  # Get second column value
        st.success(f"✅ Result: **{value}**")
    else:
        st.warning("❗ Counter number not found.")



