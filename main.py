import os
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Picnic Pro",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Assets Paths
eduTourImg = r'assets\01.jpg'
funActivityImg = r'assets\02.jpg'
eventsImg = r'assets\03.jpg'

locations = ["New Delhi", "Mumbai", "Lucknow", "Patna", "Jaipur", "Manali", "Kashmir", "Aligarh", "Noida", "Haryana", 'Mussoorie', 'test']


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

left_col, main_col, right_col = st.columns([1,8,1])  

with main_col:
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            if os.path.isfile(eduTourImg):
                image = Image.open(eduTourImg)
                st.image(image, width=300)
                st.markdown(
                    """
                    <div style="text-align: center;">
                        <h4 style="font-size:18px; font-weight:600;">Educational Tour</h4>
                    </div>
                    """,
                    unsafe_allow_html=True
                )     
            else:
                st.error(f"Unable to load the file: {eduTourImg}")

        with col2:
            if os.path.isfile(funActivityImg):
                image = Image.open(funActivityImg)
                st.image(image, width= 300)  
                st.markdown(
                    """
                    <div style="text-align: center;">
                        <h4 style="font-size:18px; font-weight:600;">Fun Activities</h4>
                    </div>
                    """,
                    unsafe_allow_html=True
                )        
            else:
                st.error(f"Unable to load the file: {funActivityImg}")

        with col3:
            if os.path.isfile(eventsImg):
                image = Image.open(eventsImg)
                st.image(image, width= 300)  
                st.markdown(
                    """
                    <div style="text-align: center;">
                        <h4 style="font-size:18px; font-weight:600;">Events For Children</h4>
                    </div>
                    """,
                    unsafe_allow_html=True
                )            
            else:
                st.error(f"Unable to load the file: {eventsImg}")

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
    


