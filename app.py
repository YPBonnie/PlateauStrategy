import streamlit as st
from PIL import Image

# Initialize session state for auth
if 'authorized' not in st.session_state:
    st.session_state.authorized = False

st.title("Prospex Portfolio")

if not st.session_state.authorized:
    st.subheader("Project Access")
    password = st.text_input("Enter Access Code", type="password")
    if st.button("Enter"):
        if password == "1234":
            st.session_state.authorized = True
            st.rerun()
        else:
            st.error("Incorrect code")
else:
    # Gallery View
    col1, col2 = st.columns(2)
    with col1:
        if st.image("images/A.png", caption="Project AutoSharing", width=300):
            st.session_state.project = "A"
    with col2:
        if st.image("images/B.png", caption="Project Restaurant", width=300):
            st.session_state.project = "B"
    
    # Detailed View (if a project is selected)
    if 'project' in st.session_state:
        st.divider()
        st.header(f"Details for Project {st.session_state.project}")
        st.write("Goal: Pricing Optimization and Anomaly Detection.")
        
        # The "Push-down" form
        with st.expander("Interested? Click to connect."):
            with st.form("contact_form"):
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                phone = st.text_input("Your Phone Number")
                submit = st.form_submit_button("Submit")
                if submit:
                    st.success(f"Thanks {name}, I'll reach out!")