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
        if st.button("Details for Project A", key="btn_a"):
            st.session_state.selected_project = "A"

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
        
        # Add your content here
        st.write(f"Goal for Project {proj}: [Insert details]")
        
        with st.expander("Interested? Click to connect."):
            with st.form(f"contact_form_{proj}"):
                st.text_input("Your Name")
                st.text_input("Your Email")
                if st.form_submit_button("Submit"):
                    st.success("Thanks! I'll reach out.")