import streamlit as st

st.set_page_config(
    page_title="Picnic Pro",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Assets Paths
eduTourImg = 'assets\eduTour.webp'
funActivityImg = 'assets\efunActivity.webp'

locations = ["New Delhi", "Mumbai", "Lucknow", "Patna", "Jaipur", "Manali", "Kashmir", "Aligarh", "Noida", "Haryana", 'Mussoorie', 'test']

# Below block is temporary we will use st.title 
st.markdown(
    """
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1542039174373-4efa3b3a9db8?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>Welcome to Picnic Pro</h1>", unsafe_allow_html=True)

# st.title("Picnic Pro")  

st.write("##### Fun and Exciting Holiday Moments")
st.write("---")

st.write("### Fill in your preferences",)
col1, col2, col3 = st.columns(3)

with col1:
    location = st.selectbox("Location", locations)

with col2:    
    number_of_days = st.number_input("Number of Days", min_value= 1, step= 1)
    
with col3:    
    budget = st.number_input("Budget")

if st.button("GENERATE PLANS"):
    st.write(f"Generating plans for {location} for {number_of_days} days within a budget of {budget}...")

st.write("---")
st.write("## Suggested Activities")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(eduTourImg, caption="Edu Tour")
with col2:
    st.image(funActivityImg, caption="Fun Activities")
with col3:
    st.image(eduTourImg, caption="Events")

# Feedback Form and Contact Us Section
st.write("### Get in Touch")

col1, col2 = st.columns(2)

with col1:
    st.write("#### Contact Us")
    st.write("**Address:** Jamia Nagar, New Delhi, 110025")
    st.write("**Email:** example@ppro.com")
    st.write("**Phone:** +91 8271981162")

with col2:
    st.write("#### We value your feedback!")
    with st.form(key="feedback_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        feedback = st.text_area("Feedback")

        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            st.write(f"Thank you for your feedback, {name}!")
    


