import streamlit as st

# Initialize session state for auth and selection
if 'authorized' not in st.session_state:
    st.session_state.authorized = False

st.title("Prospex Portfolio")

if not st.session_state.authorized:
    # ... (Your existing login logic)
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
        # This button replaces your text and triggers the details view
        if st.button("Details for Project B", key="btn_b"):
            st.session_state.selected_project = "B"
    
    # Detailed View
    if 'selected_project' in st.session_state:
        st.divider()
        proj = st.session_state.selected_project
        st.header(f"Project {proj} Detailed Summary")
        
        # Define project data
        data = {
            "A": {
                "goal": "Innovative business solution Rent-2-Own in morden transporation",
                "progress": "30% - initial installment phase.",
                "annualized return (APY)": "43%",
                "margin profit": "13%"
            },
            "B" : {
                "goal": "fill in details",
                "progress": "to be filled in",
                "expected ROI" : "to be filled in",
                "margin profit": "to be filled in"
            }
        }

        # Display the metrics in a clean row
        st.write(f"**Goal:** {data[proj]['goal']}")
        st.write(f"**Current Progress:** {data[proj]['progress']}")

        c1, c2 = st.columns(2)
        c1.metric("Expected ROI", data[proj]['roi'])
        c2.metric("Margin Profit", data[proj]['margin'])
        
        st.divider()
        
        # The "Push-down" form
        with st.expander("Interested in this project? Get in touch."):
            with st.form(f"contact_form_{proj}"):
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                phone = st.text_input("Your Phone Number")
                submit = st.form_submit_button("Submit")
                if submit: 
                    st.success(f"Thank you, {name}!" I will reach out soon.)
        