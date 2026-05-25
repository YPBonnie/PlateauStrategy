import streamlit as st
import csv
import os
from datetime import datetime

@st.dialog("Sign Up")
def show_signup():
    st.write("Join the Prospex investor list to receive updates.")
    name  = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")

    if st.button("Submit", key="signup_submit"):
        if not name or not email:
            st.warning("Name and email are required.")
        else:
            save_signup(name, email, phone)
            st.success(f"Thank you, {name}! We'll be in touch.")
            st.rerun()

def save_signup(name, email, phone):
    file = "signups.csv"
    file_exists = os.path.isfile(file)
    with open(file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "name", "email", "phone"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "timestamp": datetime.now().isoformat(),
            "name": name,
            "email": email,
            "phone": phone
        })

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "home"

if 'authorized' not in st.session_state:
    st.session_state.authorized = False

# Custom Layout for Header
header_col1, header_col2 = st.columns([2,1])

with header_col1:
    st.markdown("#### [PlateauStrategy.US](https://plateaustrategy-ghy8bs3mwfcmre9idoaujr.streamlit.app/)")

with header_col2:
    #Creating a horizontal menu with buttons
    menu_col1, menu_col2 = st.columns(2)
    with menu_col1:
        if st.button("Sign up"):
            show_signup()

    with menu_col2:
        if st.button("Login"):
            st.session_state.page = "login"

st.divider()



st.title("ProspeX Portfolio")
# --- Introduction Section ---
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



# --- Login logic ---
if not st.session_state.authorized:
    password = st.text_input("Enter Access Code", type="password")
    if st.button("Enter"):
        if password == "1234":
            st.session_state.authorized = True
            st.rerun()
else:
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("images/A.png", use_container_width=True)
        if st.button("Details for Rideshare Solution", key="btn_a"):
            st.session_state.selected_project = "Rideshare Solution"

    with col2:
        st.image("images/B.png", use_container_width=True)
        if st.button("Details for Project B", key="btn_b"):
            st.session_state.selected_project = "Project B"
    
    # Define project data - Keys match the strings used in button clicks
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

    # Detailed View
    if 'selected_project' in st.session_state:
        proj = st.session_state.selected_project
        
        # Check if project exists in data to prevent KeyError
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