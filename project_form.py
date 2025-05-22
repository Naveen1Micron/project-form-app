import streamlit as st
from datetime import date

# Title of the app
st.title("Project Input Form")

# Input fields
Location = st.text_input("Enter the Location")
Disaster_Occured_Date = st.text_input("Enter the Disaster Occured Date")

# Submit button
if st.button("Submit"):
    # Display the summary
    st.success("Here is your project summary:")
    st.write(f"**Location:** {Location}")
    st.write(f"**Disaster Occured Date:** {Disaster_Occured_Date}")
