import streamlit as st
import pandas as pd
from datetime import datetime

# ----------- CONFIGURATION -----------
VALID_LOGIN_ID = "admin"
VALID_PASSWORD = "2580"
EXPIRY_DATE = datetime(2026, 8, 10)  # YYYY, M, D
EXCEL_FILE = "98002238.xlsx"
# -------------------------------------

# Set page config
st.set_page_config(page_title="Dynamic Login", page_icon="🔐", layout="centered")

# Expiry Check
today = datetime.today()
if today > EXPIRY_DATE:
    st.markdown("## ⚠️ Session Expired")
    st.warning("This app is no longer active.")
    st.stop()

# Load Excel data
@st.cache_data
def load_data():
    return pd.read_excel(EXCEL_FILE, header=None, engine="openpyxl")

# Login Page
def login_page():
    st.markdown("## 🔐 Admin Login")
    login_id = st.text_input("Enter Login ID")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if login_id == VALID_LOGIN_ID and password == VALID_PASSWORD:
            st.session_state["authenticated"] = True
        else:
            st.error("❌ Incorrect Login ID or Password")

# Main Application
def main_app():
    st.markdown("## 🔐 Dynamic Login")
    st.write("Enter Counter Number to fetch the corresponding value from the system.")
    
    df = load_data()
    max_index = len(df)
    
    counter = st.number_input("Enter Counter Number:", min_value=1, max_value=max_index, step=1)
    
    if st.button("Get Value"):
        value = df.iloc[counter - 1, 0]
        clean_value = str(value).replace(".0", "")
        st.success(f"✅ Value for Counter Number {counter} is: {clean_value}")

# Login Session Check
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login_page()
else:
    main_app()
