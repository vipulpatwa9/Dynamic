import streamlit as st
import pandas as pd
from datetime import datetime

# ==== 1. Check Expiry ====
if datetime.now() > datetime(2026, 8, 10):
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
        if username == "admin" and password == "2580":
            st.session_state.logged_in = True
            st.success("✅ Login successful!")
            st.experimental_rerun()  # rerun to show main content
        else:
            st.error("Invalid credentials")
    st.stop()

# ==== 3. Main App Content ====
st.header("🔍 Search Counter Number")
st.write("Enter Counter Number to fetch the corresponding value from the system.")

# ==== Load Excel Data ====
@st.cache_data
def load_data():
    return pd.read_excel("98002238.xlsx")

df = load_data()

# ==== Debug Info (Optional) ====
st.write("Raw Counter Column:", df[df.columns[0]].tolist())
st.write("Data Types:", df[df.columns[0]].map(type).value_counts())

# ==== Sanitize Data ====
# Convert counter column to str and strip spaces
df[df.columns[0]] = df[df.columns[0]].astype(str).str.strip()

# ==== Input and Lookup ====
counter_number = st.number_input("Enter Counter Number:", min_value=1, step=1)

if st.button("Get Value"):
    match_value = str(counter_number).strip()

    result = df[df[df.columns[0]] == match_value]

    if not result.empty:
        value = result.iloc[0, 1]  # Get value from second column
        st.success(f"✅ Result: **{value}**")
    else:
        st.warning("❗ Counter number not found.")
