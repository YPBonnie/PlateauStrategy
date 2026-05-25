import streamlit as st
import csv
import os
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

def get_sheet(sheet_name):
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
    )
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1

def save_signup(name, email, phone):
    sheet = get_sheet("ProspeX Signups")
    sheet.append_row([datetime.now().isoformat(), name, email, phone])

def save_user(name, email):
    sheet = get_sheet("ProspeX Users")
    sheet.append_row([email, "", "pending", name, datetime.now().isoformat()])

def check_login(email, password):
    sheet = get_sheet("ProspeX Users")
    records = sheet.get_all_records()
    for row in records:
        if row["email"].lower() == email.lower():
            if row["status"] != "approved":
                return False, "YOur account is pending approval."
            if str(row["password"]) == password:
                return True, row["name"]
            return False, "Incorrect password."
    return False, "Email not found. Please sign up first."

#def save_signup(name, email, phone):
#    creds = Credentials.from_service_account_info(
#        st.secrets["gcp_service_account"],
#        scopes=[
#            "https://www.googleapis.com/auth/spreadsheets",
#            "https://www.googleapis.com/auth/drive"
#        ]
#    )
#    client = gspread.authorize(creds)
#    sheet = client.open("ProspeX Signups").sheet1
#    sheet.append_row([datetime.now().isoformat(), name, email, phone])

@st.dialog("Sign Up")
def show_signup():
    st.write("Join the ProspeX investor list to receive updates.")
    name  = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")

    if st.button("Submit", key="signup_submit"):
        if not name or not email:
            st.warning("Name and email are required.")
        else:
            try:
                save_signup(name, email, phone)
                save_user(name, email)
                st.success(f"Thank you, {name}! We'll be in touch.")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

@st.dialog("Login")
def show_login():
    email = st.text_input("Email Address")
    password = st.text_input("Password", type = "password")

    if st.button("Login", key="login_submit"):
        if not email or not password:
            st.warning("Please enter your email and password.")
        else:
            try:
                success, message = check_login(email, password)
                if success:
                    st.session_state.authorized = True
                    st.session_state.user_name = message
                    st.rerun()
                else:
                    st.error(message)
            except Exception as e:
                st.error(f"Error: {e}")

# Initialize session state
if 'authorized' not in st.session_state:
    st.session_state.authorized = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Header
header_col1, header_col2 = st.columns([2, 1])

with header_col1:
    st.markdown("#### [PlateauStrategy.US](https://plateaustrategy-ghy8bs3mwfcmre9idoaujr.streamlit.app/)")

with header_col2:
    menu_col1, menu_col2 = st.columns(2)
    with menu_col1:
        if not st.session_state.authorized:
            if st.button("Sign up"):
                show_signup()
    with menu_col2:
        if st.session_state.authorized:
            if st.button("Logout"):
                st.session_state.authorized = False
                st.session_state.user_name = ""
                st.rerun()
        else:
            if st.button("Login"):
                show_login()

st.divider()

st.title("Plateau Strategy Phase V: ProspeX")

with st.container():
    st.markdown("""
    ### Welcome to ProspeX
    **ProspeX** high-impact initiative investment platform focused on operational efficiency,
    pricing optimization, and business-driven data strategy.

    *   **What is this:** A curated showcase of advanced analytical frameworks applied to real-world marketplace challenges.
    *   **Who built it:** Bonnie Dou, a Data Scientist with 10+ years of experience in enterprise environments (eBay, Microsoft, Google), specializing in pricing engines and AI deployment.
    *   **The Outcome:** Scalable, robust solutions that balance aggressive revenue growth with disciplined risk management.
    """)
    st.divider()

# Project details — approved users only
if st.session_state.authorized:
    st.write(f"Welcome back, **{st.session_state.user_name}**!")

    col1, col2 = st.columns(2)

    with col1:
        st.image("images/A.png", use_container_width=True)
        if st.button("Details for Rideshare Solution", key="btn_a"):
            st.session_state.selected_project = "Rideshare Solution"

    with col2:
        st.image("images/B.png", use_container_width=True)
        if st.button("Details for Project B", key="btn_b"):
            st.session_state.selected_project = "Project B"

    data = {
        "Rideshare Solution": {
            "goal": "Innovative business solution Rent-2-Own in modern transportation.",
            "progress": "30% - initial installment phase.",
            "roi": "43%",
            "margin": "13%"
        },
        "Project B": {
            "goal": "Placeholder for future initiative.",
            "progress": "To be filled in.",
            "roi": "0%",
            "margin": "0%"
        }
    }

    if 'selected_project' in st.session_state:
        proj = st.session_state.selected_project

        if proj in data:
            st.divider()
            st.header(f"{proj} Detailed Summary")

            st.write(f"**Goal:** {data[proj]['goal']}")
            st.write(f"**Current Progress:** {data[proj]['progress']}")

            c1, c2 = st.columns(2)
            c1.metric("Expected ROI/APY", data[proj]['roi'])
            c2.metric("Margin Profit", data[proj]['margin'])

            st.divider()

            with st.expander("Interested in this project? Get in touch."):
                with st.form(f"contact_form_{proj}"):
                    name = st.text_input("Your Name")
                    email = st.text_input("Your Email")
                    phone = st.text_input("Your Phone Number")
                    submit = st.form_submit_button("Submit")
                    if submit:
                        st.success(f"Thank you, {name}! I will reach out soon.")
        else:
            st.error("Project data not found.")
else:
    st.info("Please log in to view project details.")