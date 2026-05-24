import streamlit as st

# Custom Layout for Header
header_col1, header_col2 = st.columns([2,1])

with header_col1:
    st.markdown("#### [PlateauStragegy.US](https://plateaustrategy.us)")

with header_col2:
    #Creating a horizontal menu with buttons
    menu_col1, menu_col2 = st.columns(2)
    with menu_col1:
        if st.button("Sign up"):
            st.session_stage.page = "signup"

    with menu_col2:
        if st.button("Login"):
            st.session_state.page = "login"

st.divider()

# Initialize session state
if 'authorized' not in st.session_state:
    st.session_state.authorized = False

st.title("Prospex Portfolio")
# --- Introduction Section ---
with st.container():
    st.markdown("""
    ### Welcome to Prospex
    **Prospex** high-impact initiative investment platform focused on operational efficiency, 
    pricing optimization, and business-driven data strategy. 
    
    *   **What is this:** A curated showcase of advanced analytical frameworks applied to real-world marketplace challenges.
    *   **Who built it:** Bonnie Dou, a Data Scientist with 10+ years of experience in enterprise environments (eBay, Microsoft, Google), specializing in pricing engines and AI deployment.
    *   **The Outcome:** Scalable, robust solutions that balance aggressive revenue growth with disciplined risk management.
    """)
    st.divider()

if 'page' not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "login":
    ## Show your existing password logic here
    password = st.text_input("Enter Access Code", type = "password")

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